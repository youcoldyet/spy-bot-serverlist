import requests
import json
import time

def read_json_file(file_path):
    """Utility function to read a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def fetch_server_data(server_guids, delay=1):
    """Fetch data for each server GUID from the API and extract only the id and username."""
    base_url = "https://kickthespy.pet/getBot?id="
    server_data = {}
    errors = []
    for server in server_guids:
        response = requests.get(f"{base_url}{server['guid']}")
        if response.status_code == 200:
            data = response.json()
            # Extracting and storing the id and username along with server details
            server_data[server['guid']] = {
                'server_name': server['server_name'],
                'serverid': server['guid'],  # 'serverid' same as GUID
                'username': data.get('username'),
                'userid': data.get('id')  # 'userid' fetched from API
            }
            print(f"Data received for GUID {server['guid']}:")
            print(json.dumps(data, indent=4))  # Print each response in a formatted manner
        else:
            error_message = f"Failed to fetch data for GUID {server['guid']}: {response.text}"
            print(error_message)
            errors.append({
                'guid': server['guid'],
                'error': response.text
            })
        time.sleep(delay)  # Wait before making the next request to handle rate limits
    return server_data, errors

def match_users_to_servers(server_data, user_ids):
    """Match user IDs to servers based on the id field from server data."""
    user_server_map = {}
    for user_id in user_ids:
        for guid, info in server_data.items():
            if info['userid'] == user_id:
                if user_id not in user_server_map:
                    user_server_map[user_id] = []
                user_server_map[user_id].append(info)
    return user_server_map

def save_to_json(data, output_file):
    """Save data to a JSON file."""
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Load data from JSON files
servers = read_json_file('servers.json')
user_ids = read_json_file('ids.json')

# Fetch data for each server using their GUIDs with a delay
server_data, errors = fetch_server_data(servers, delay=0)  # Adjust delay as needed

# Save the fetched server data and any errors
save_to_json(server_data, 'server_data.json')
save_to_json(errors, 'fetch_errors.json')

# Match user IDs to servers
user_server_associations = match_users_to_servers(server_data, user_ids)

# Save the matched user-server associations
save_to_json(user_server_associations, 'user_server_associations2.json')

print("Data extracted and saved successfully.")
