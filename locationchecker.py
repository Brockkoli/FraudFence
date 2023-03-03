import webbrowser

import folium
import requests

def serverlocationchecker(ip_address):
    # Use an online IP geolocation service to get the latitude and longitude of the server
    api_url = f"https://ipinfo.io/{ip_address}/geo"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        latitude, longitude = data['loc'].split(',')

        # Create a folium map centered on the server location
        createmap = folium.Map(location=[float(latitude), float(longitude)], zoom_start=10)

        # Add a marker for the server location
        folium.Marker(location=[float(latitude), float(longitude)], popup=f"Server location: {ip_address}").add_to(createmap)

        # Open the map in a new browser window
        createmap.save('map.html')
        webbrowser.open('map.html')


#User input ip address
ip_address = input("Enter server IP address: ")
serverlocationchecker(ip_address)
