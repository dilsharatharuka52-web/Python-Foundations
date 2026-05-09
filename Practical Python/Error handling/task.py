import json
from pathlib import Path

# 1. SETUP: Use pathlib for cross-platform compatibility (Linux/Windows)
# This points to a file in your current directory
file_path = Path("servers.json")

def initialize_inventory():
    """Initializes the file with a starting list of servers."""
    servers = [
        {"id": 1, "hostname": "web-prod-01", "ip": "192.168.1.10"},
        {"id": 2, "hostname": "db-prod-01", "ip": "192.168.1.11"}
    ]
    
    print(f"--- Initializing {file_path} ---")
    with open(file_path, "w") as f:
        # indent=4 makes the file human-readable
        json.dump(servers, f, indent=4)
    print("Initial save complete.\n")

def add_server(new_hostname, new_ip):
    """Reloads the list, appends a new server, and saves again."""
    
    # 2. RELOAD: Read the existing JSON data
    if not file_path.exists():
        print("Error: Inventory file not found. Initialize it first.")
        return

    print(f"--- Reloading data from {file_path} ---")
    with open(file_path, "r") as f:
        current_inventory = json.load(f)

    # 3. MODIFY: Create new server object and add it to the list
    new_id = len(current_inventory) + 1
    new_server = {
        "id": new_id,
        "hostname": new_hostname,
        "ip": new_ip
    }
    current_inventory.append(new_server)
    print(f"Added: {new_hostname} ({new_ip})")

    # 4. SAVE AGAIN: Overwrite the file with the updated list
    with open(file_path, "w") as f:
        json.dump(current_inventory, f, indent=4)
    print("Update saved successfully.\n")

def display_inventory():
    """Reads and prints the current status of the file."""
    with open(file_path, "r") as f:
        data = json.load(f)
        print("Current Server Inventory:")
        for server in data:
            print(f"ID: {server['id']} | Host: {server['hostname']} | IP: {server['ip']}")

# --- EXECUTION FLOW ---

# Step 1: Create the file
initialize_inventory()

# Step 2: Add a new server dynamically
add_server("app-prod-01", "192.168.1.12")

# Step 3: Add another one to show appending works
add_server("cache-prod-01", "192.168.1.13")

# Step 4: Show the final result
display_inventory()