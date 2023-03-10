from jinja2 import Template

def format_data(data):
    formatted_data = []
    for item in data:
        row = []
        for key, value in item.items():
            if isinstance(value, tuple) and len(value) == 1 and isinstance(value[0], tuple):
                formatted_value = ', '.join([f'{k}: {v}' for k, v in value[0]])
            else:
                formatted_value = str(value)
            row.append({'key': key, 'value': formatted_value})
        formatted_data.append(row)
    return formatted_data


def printall(url, result, result2):
    # Load the template
    with open('report_template.html') as file:
        template = Template(file.read())

    # Format the data for the SSL report
    ssl_data = format_data([result])
    ssl_headers = [item['key'] for item in ssl_data[0]]

    # Format the data for the HTTP report
    http_data = format_data([result2])
    http_headers = [item['key'] for item in http_data[0]]

    # Render the template with the data
    output1 = template.render(
        url=url,
        ssl_headers=ssl_headers,
        ssl_data=ssl_data,
        http_headers=http_headers,
        http_data=http_data
    )

    # Save the output to a file
    with open('report.html', 'w') as file:
        file.write(output1)

    print("HTML report generated successfully")

