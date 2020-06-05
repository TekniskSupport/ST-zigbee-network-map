import networkx as nx
import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

G       = nx.Graph()
cookies = {'JSESSIONID': input("COOKIE:")}
host    = 'https://graph-eu01-euwest1.api.smartthings.com'
r       = requests.get(host+'/device/list', cookies=cookies)

G.add_node('0',details='{\'name\': \'Hub\'}')

soup = BeautifulSoup(r.content, "html.parser")
translationDict = {}
for device in soup.select('#device-table > tbody > tr'):
    link = device.select('td:nth-of-type(1) > a')[0]
    deviceName        = link.text.strip()
    deviceDetailsLink = link.get('href')
    deviceType        = device.select('td:nth-of-type(2)')[0].text.strip()
    hubName           = device.select('td:nth-of-type(4)')[0].text.strip()
    deviceId          = device.select('td:nth-of-type(5)')[0].text.strip()
    deviceNetworkId   = device.select('td:nth-of-type(6)')[0].text.strip()
    deviceStatus      = device.select('td:nth-of-type(7)')[0].text.strip()

    deviceDetails = requests.get(host+deviceDetailsLink, cookies=cookies)
    details = BeautifulSoup(deviceDetails.content, "html.parser")
    translationDict[deviceNetworkId] = deviceName
    deviceData = {
        'name':   deviceName,
        'Type':   deviceType,
        'ID':     deviceId,
        'NID':    deviceNetworkId,
        'Status': deviceStatus
    }
    G.add_node(deviceNetworkId, details=deviceData)
    routes = details.select('#meshRoute-label + td a')
    deviceRoute = []
    for route in routes:
        rex = re.search('.*\((.+)\).*', route.text)
        if route == routes[1]:
            print(deviceNetworkId + ' ' + deviceName + ' is connected to:')

        if rex and rex.group(1) != deviceNetworkId:
            deviceRoute.append(rex.group(1))
            print(rex.group(1))
        if route.text == hubName:
            deviceRoute.append('0')
            print(route.text)
        if route == routes[-1]:
            print("\n")

    previousroute = None
    for route in deviceRoute:
        if not previousroute:
            G.add_edge(deviceNetworkId, route)
        else:
            G.add_edge(route, previousroute)
        previousroute = route


options = {
    'font_size': 10,
    'node_size': 50,
    'width': 2,
    'with_labels': True,
    'labels': translationDict
}

nx.draw(G,**options)
fig = plt.gcf()
fig.set_size_inches(180, 100, forward=True)
plt.show()
