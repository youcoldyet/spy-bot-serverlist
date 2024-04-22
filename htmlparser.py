from bs4 import BeautifulSoup
import json

def extract_servers_from_html(file_path):
    # Read the HTML file using UTF-8 encoding to handle Unicode characters
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # List to store server data
    servers = []

    # Find all server blocks
    for server_block in soup.find_all('div', class_='inline-block'):
        a_tag = server_block.find('a')
        if a_tag and '/servers/' in a_tag['href']:
            guid = a_tag['href'].split('/')[-1]
            server_name = server_block.find('div', class_='text-center').div.text.strip()
            servers.append({'server_name': server_name, 'guid': guid})

    return servers

def save_to_json(data, output_file):
    # Write data to a JSON file with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # ensure_ascii=False to save actual Unicode characters

# File path to the HTML file
file_path = 'compiled_output.html'

# Extract server data
server_data = extract_servers_from_html(file_path)

# Output JSON file path
json_file_path = 'servers.json'

# Save the data to a JSON file
save_to_json(server_data, json_file_path)
print(f"Data extracted and saved to {json_file_path}")
