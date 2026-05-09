# 3. Working with Structured Data: JSON & CSV
# Plain text is fine, but most data comes in specific formats.
# JSON (json.load / json.dump)
# JSON is essentially a Python dictionary stored as text.

          # json.load(file): Reads a JSON file and turns it into a Python object (dict/list).
          # json.dump(data, file): Takes a Python object and writes it into a file as JSON.
          # json.dumps This "dumps" a Python dictionary or list into a formatted string.
          # json.loads This "loads" a JSON-formatted string back into a Python object.

import json
from pathlib import Path # 1. Import the json module and Path from pathlib.
                         # this allows us to work with JSON data and handle file paths easily.


# 2. Define the file path using pathlub

file_path = Path("Practical Python/File_I_O/servers.json")

# 3 Initial state: A list of server dictionaries

initial_servers = [
    {"hostname": "web-01", "ip": "10.0.0.5", "role": "frontend"},
    {"hostname": "db-01", "ip": "10.0.0.6", "role": "backend"}
]

# 4. SAVE: write the initial list to JSON
print("Saving initial server list......")

#The with statement creates a context manager that automatically closes 
# the file after the indented block executes – even if an error occurs inside the block.

#Without with, you’d need to manually call f.close(), w
# hich is easy to forget and can lead to resource leaks or corrupted files

with open(file_path, "w") as f :
     # indent = 4 makes the JOSN file human-readable
       json.dump(initial_servers, f, indent = 4)

# 5. RELOAD: Read the JSON back into a Python variable
print("Reloading server list from JSON file...")
with open(file_path, "r") as f:
        current_servers = json.load(f)
        print(current_servers) 

 # 6. ADD A SERVER: Append to the Python list
print("Adding a new server to the list...")     
new_server = {"hostname" : "cache-01", "ip": "10.0.0.7", "role": "redis"} 
current_servers.append(new_server) # This modifies the in-memory list but does not change the JSON file yet.
print(current_servers)

# 7. SAVE AGAIN: Overwrite the file the updated list
print("Saving updated server list....")
with open(file_path, "w") as f:
        json.dump(current_servers, f, indent = 4)
print("Done!")        
