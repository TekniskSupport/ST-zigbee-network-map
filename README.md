# ST-network-map
Creates a map for your zigbee/Z-wave network

![screenshot](https://raw.githubusercontent.com/TekniskSupport/ST-zigbee-network-map/master/screenshot.png "screenshot")

Made primarely for my own use, uses European IDE, so you might need to change the URI on line 9

First run:
`pip3 install matplotlib bs4 networkx requests`

Then run from terminal:
`python3 scrape-st.py`

Extract cookie from session using "application" tab under developer tools (right click -> inspect -> Application -> cookies)
look for the one with name JSESSIONID and copy the value.
____

### Windows instructions

- Download and install python from 
https://www.python.org/downloads/ Make sure you check the box
 "add to path"
- reboot
- Open command prompt and run command: `python -m pip install matplotlib bs4 networkx requests`
- [Download](https://github.com/TekniskSupport/ST-zigbee-network-map/archive/master.zip) and extract files
- double click on "scrape-st"
