import requests
import webbrowser
import folium
import PySimpleGUI as sg

def serverlocationchecker(ip_address):
    # get latitude and longitude using online geolocation API
    api_url = f"https://ipinfo.io/{ip_address}/geo"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        latitude, longitude = data['loc'].split(',')

        # create a map centered on the server location
        createmap = folium.Map(location=[float(latitude), float(longitude)], zoom_start=10)

        # mark the server location
        folium.Marker(location=[float(latitude), float(longitude)], popup=f"Server location: {ip_address}").add_to(
            createmap)

        # generate a browser window for the map
        createmap.save('map.html')
        webbrowser.open('map.html')

        # display a popup window asking the user if they want to continue
        # user can see this popup when they go back to the program
        layout = [
            [sg.Text(f"Location for {ip_address} opened in browser")],
            [sg.Button("CLOSE POPUP", button_color='#750000')]
        ]
        window = sg.Window("Location opened", layout)
        event, _ = window.read()

        if event == sg.WIN_CLOSED or event == "CLOSE POPUP":
            # close this window and go back to main menu
            window.close()
            return True
