# 1. The Core Mechanics: try / except / finally
"""
  Think of this like a safety net for your code.

   ry: You put the "risky" code here (code that might fail).
   except: This block runs only if an error occurs. You should catch specific errors, not everything.
   finally: This block runs no matter what (success or failure). This is where you close database connections or log "Cleanup complete."
"""

#2. Custom Exceptions: class ServerNotFoundError(Exception)

"""
Sometimes standard Python errors aren't descriptive enough.
 In DevOps, you might want a specific error for when a server doesn't respond, 
 even if the code itself is technically "correct."

 # Defining a custom exception
class ServerNotFoundError(Exception):
    #Raised when a specific server is missing from our inventory.#
    pass
"""

import json
from pathlib import Path

class ServerNotFoundError(Exception): # custom exception for when a server is not found in the inventory
     pass

def get_server_ip(server_name):
     file_path = Path("Practical Python/Error handling/inventory.json")

     try:
            # 1. Catching FileNotFoundError
            with open(file_path) as f:
                data = json.load(f)
            
            # 2. Catching ValueError (if servr is not in the list)
            if server_name not in data:
                 raise ServerNotFoundError(f"Server '{server_name}' not found in inventory.")
            return data[server_name]
     
     except FileNotFoundError:
          print(f"CRITICAL ERROR: {file_path} is missing. Cannot proceed.")
     except json.JSONDecodeError:
          print(f"ERROR: {file_path} is corrupted. Check the JSON syntax.")
     except ServerNotFoundError as e:
           print(f"LOG ALERT: {e}")
     except Exception as e:
        # The 'catch-all' — use sparingly!
           print(f"AN UNEXPECTED ERROR OCCURRED: {e}")
     finally:
            print("Inventory check operation attempted.")

print(get_server_ip("web-prod-01"))

"""
🚀 Interview & Real-World Problem
The Interview Question:

"If you are writing a Python script that deletes old logs from a
 production server, what is the most dangerous error to ignore, and how
 would you handle it?

 The Answer:
The most dangerous error is a PermissionError. 
If your script thinks it deleted the logs but didn't (because it lacked permissions), 
the disk will eventually hit 100%, crashing the whole server. 
You handle it by catching PermissionError and immediately triggering an alert to the DevOps team.
"""