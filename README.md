# SmartThings network map
## Creates a map for your zigbee/Z-wave network

![screenshot](https://raw.githubusercontent.com/TekniskSupport/ST-zigbee-network-map/master/screenshot.png "screenshot")

First run:
`python -m pip install matplotlib bs4 networkx requests`

Then run from terminal:
`python scrape-st.py`

### Optionally pass sessionID as commandline argument
`python scrape-st.py YOUR-JSESSION-ID`

### Extract JSESSIONID value from cookie:
Chrome:

- login to [IDE](https://account.smartthings.com)
- Open developer tools by pressing F12 or right click and inspect
- Navigate to "application" tab and expand cookies
- look for the line with name JSESSIONID and copy the value.

Firefox/Edge:

- login to [IDE](https://account.smartthings.com)
- Open developer tools by pressing F12 or right click and inspect element
to to Storage tab and expand Cookies
- look for the line with name JSESSIONID and copy the value.



____

### Windows instructions

- Download and install python from 
https://www.python.org/downloads/ Make sure you check the box
 "add to path"
- reboot
- Open command prompt and run command: `python -m pip install matplotlib bs4 networkx requests`
- [Download](https://github.com/TekniskSupport/ST-zigbee-network-map/archive/master.zip) and extract files
- double click on "scrape-st"
