import webbrowser
import socket
import folium
import requests
import colorama

colorama.init()


def conversion_url(url):
    if url.startswith("https://"):
        url = url.replace("https://", "", 1)
    elif url.startswith("http://"):
        url = url.replace("http://", "", 1)
    ip_address = socket.gethostbyname(url)
    return ip_address


def serverlocationchecker(url):
    # Use conversion_url function to get the IP address of the server
    ip_address = conversion_url(url)

    # Use online IP geolocation service to get the latlong of the server
    api_url = f"https://ipinfo.io/{ip_address}/geo"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        latitude, longitude = data['loc'].split(',')

        # Create a folium map centered on the server location
        createmap = folium.Map(location=[float(latitude), float(longitude)], zoom_start=10)

        # Add a marker for the server location
        folium.Marker(location=[float(latitude), float(longitude)], popup=f"Server location: {ip_address}").add_to(
            createmap)

        # Open the map in a new browser window
        createmap.save('map.html')
        webbrowser.open('map.html')

        print("-" * 50)
        print(f"Location for " + colorama.Fore.YELLOW + ip_address + colorama.Style.RESET_ALL + " opened in browser.\n")

