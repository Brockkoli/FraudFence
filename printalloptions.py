import folium
from jinja2 import Template
import datetime

def format_data(data):
    formatted_data = []
    for item in data:
        if isinstance(item, dict):
            row = []
            for key, value in item.items():
                try:
                    if value is None:
                        formatted_value = "N/A"
                    elif isinstance(value, list):
                        formatted_value = ", ".join(value)
                    elif isinstance(value, tuple) and len(value) == 1 and isinstance(value[0], tuple):
                        formatted_value = ', '.join([f'{k}: {v}' for k, v in value[0]])
                    elif key == "expires":
                        formatted_value = datetime.datetime.strptime(value, "%Y%m%d%H%M%S").strftime("%d-%m-%Y")
                    else:
                        formatted_value = str(value)
                except:
                    pass
                row.append({'key': key, 'value': formatted_value})
            formatted_data.append(row)
        elif isinstance(item, list):
            formatted_data.append(format_data(item))
    return formatted_data


def printall(url, portscan_result, ssl_result, header_result,dns_result,location_result,tracer_result,directory_result,whois_result, webrisk_result):
    # Format the data for the Location report
    latitude, longitude = location_result.split(",")
    # Use latitude and longitude to create a folium map
    map = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker(location=[latitude, longitude], popup="Server location").add_to(map)
    map_html = map.get_root().render()

    # Load the template
    with open('report_template.html') as file:
        template = Template(file.read())

    # Format the data for the portscan report
    portscan_data = format_data([portscan_result])
    if portscan_data:
        portscan_headers = [item['key'] for item in portscan_data[0]]
    else:
        portscan_headers = []

    # Format the data for the SSL report
    ssl_data = format_data([ssl_result])
    if ssl_data:
        ssl_headers = [item['key'] for item in ssl_data[0]]
    else:
        ssl_headers = []

    # Format the data for the header report
    http_data = format_data([header_result])
    if http_data:
        http_headers = [item['key'] for item in http_data[0]]
    else:
        http_headers = []

    # Format the data for the DNS report
    dns_data = format_data([dns_result])
    if dns_data:
        dns_headers = [item['key'] for item in dns_data[0]]
    else:
        dns_headers = []

    # Format the data for the Traceroute report
    tracer_data = format_data(tracer_result)
    if tracer_data:
        tracer_headers = [item['key'] for item in tracer_data[0]]
    else:
        tracer_headers = []
     #Format the data for the Directory report
    directory_data = format_data([directory_result])
    if directory_data:
        directory_headers = [item['value'] for item in directory_data[0]]
    else:
        directory_headers = []
        
    #Format the data for the Whois report
    whois_data = format_data([whois_result])
    whois_headers = [item['key'] for item in whois_data[0]]

    # Render the template with the data
    output1 = template.render(
        url=url,
        portscan_headers = portscan_headers,
        portscan_data = portscan_data,
        ssl_headers=ssl_headers,
        ssl_data=ssl_data,
        http_headers=http_headers,
        http_data=http_data,
        dns_headers = dns_headers,
        dns_data = dns_data,
        map = map_html,
        tracer_headers=tracer_headers,
        tracer_data=tracer_data,
        directory_headers = directory_headers,
        directory_data = directory_data,
        whois_headers=whois_headers,
        whois_data=whois_data,
        webrisk_headers = webrisk_headers,
        webrisk_data = webrisk_data
    )

    # Save the output to a file
    with open('report.html', 'w') as file:
        file.write(output1)

    print("HTML report generated successfully")
