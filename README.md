# ST-network-map
Creates a map for your zigbee/Z-wave network

Made primarely for my own use, uses European IDE, so you might need to change the URI on line 9

First run:
`pip3 install matplotlib bs4 networkx`

Then run from terminal:
`python3 scrape-st.py`

Extract cookie from session using "application" tab under developer tools (right click -> inspect -> Application -> cookies)
look for the one with name JSESSIONID and copy the value.


![screenshot](https://raw.githubusercontent.com/TekniskSupport/ST-zigbee-network-map/master/screenshot.png "screenshot")
