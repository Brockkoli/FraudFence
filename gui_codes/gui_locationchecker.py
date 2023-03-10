import requests
import webbrowser
import folium
import PySimpleGUI as sg

def serverlocationchecker(ip_address):
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

        # Display a pop-up window asking the user if they want to continue
        layout = [[sg.Text(f"Location for {ip_address} opened in browser.\n\nDo you wish to continue?")],
                  [sg.Button("Yes"), sg.Button("No")]]
        window = sg.Window("Continue?", layout)
        event, _ = window.read()
        window.close()

        if event == "Yes":
            return True
        else:
            return False
