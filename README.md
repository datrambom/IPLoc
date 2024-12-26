# IPLoc

IPLoc is a graphical desktop application built using `customtkinter` that allows users to look up geographical and ISP information for a given IP address. This lightweight tool uses the IP-API service to fetch details and displays them in an intuitive interface.

## Features
- User-friendly GUI built with `customtkinter`.
- Real-time IP lookup for timezone, country, region, city, ZIP code, and ISP.
- Error handling for invalid inputs and failed API requests.
- Simple and modern design with theme support.

## Prerequisites
- Python 3.8 or higher
- Internet connection

## Installation

1. Download the latest release from the [Releases](https://github.com/datrambom/IPLoc/releases) page
2. Open **IPLoc.exe**

## Usage
1. Launch the application.
2. Enter a valid IP address in the input field.
3. Click the **Lookup** button.
4. View the results displayed in the output box.

## Screenshot
![IPLoc_KznhRInrRq](https://github.com/user-attachments/assets/735ce352-c9bc-407b-8ad4-0711ad5dcad1)

## How It Works
IPLoc fetches data from the [IP-API](http://ip-api.com/) JSON endpoint. For a given IP address, it retrieves and displays the following details:
- IP Address
- Timezone
- Country
- Region
- City
- ZIP Code
- ISP

## Dependencies
- Python
- `customtkinter`

## Acknowledgements
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [IP-API](http://ip-api.com/)
