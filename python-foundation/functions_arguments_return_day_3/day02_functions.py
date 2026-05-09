# server data
servers = [
    {"name": "web-1", "host": "localhost", "port": 80},
    {"name": "ssh-1", "host": "localhost", "port": 22},
    {"name": "db-1", "host": "localhost", "port": 3306},
]

# fake check function (simulation)
def check_port(port):
    # assume common ports are "online"
    if port in [80, 22]:
        return True
    else:
        return False

print("Name     Port   Status")
print("-----------------------")

for s in servers:
    status = "online" if check_port(s["port"]) else "offline"
    print(f"{s['name']}   {s['port']}   {status}")


# The Challenge: The "AI API Validator"
# Imagine you are building a gateway for your SafeScale Web SaaS. You need a function that checks if an incoming API request is valid before sending it to your Llama-3 model.

# The Task:

# Define a function named validate_request that takes two parameters: api_key and request_size.

# Inside the function:

# Create a list of authorized keys: authorized_keys = ["dev-123", "prod-456", "admin-789"].

# Use an if/else statement with the and operator:

# If the api_key is in the authorized_keys list AND the request_size is less than 50 (MB), return "Authorized".

# Otherwise, return "Access Denied".

# The Loop: Create a list of test requests (each request is a small dictionary):

# Python

# test_data = [
#     {"key": "dev-123", "size": 10},
#     {"key": "wrong-key", "size": 5},
#     {"key": "admin-789", "size": 100}
# ]
# Action: Loop through test_data, call your function for each one, and print the result.


def validate_requse(api_key, request_size):
          authoizes_keys = ["dev-123", "prod-456", "admin-789"]

          if api_key in authoizes_keys and request_size < 50:
               return "Authorized"
          else:
               return "Access Denied"


test_data = [
    {"key": "dev-123", "size": 10},
    {"key": "wrong-key", "size": 5},
    {"key": "admin-789", "size": 100}
 ]

for data in test_data:
   status = validate_requse(data["key"], data["size"])
   print(status)


# hallenge
# You are building a security tool for your InvoiceMarshal SaaS. 
# You need to process a list of login attempts, but the data is "dirty"—some logs have missing values or the wrong data types.

# The Task:

# The Data: Create a list called raw_logs:

# The Function: Define process_security(logs).

# Inside the function:

# Loop through the logs.

# Use a try/except block to convert attempts to an int.

# If successful: If attempts > 3, print "[BLOCK] {user} has too many attempts."

# If a ValueError occurs: Print "[ERROR] Invalid data for user {user}. Skipping..."



raw_logs = [
    {"user": "alice", "attempts": "5"},
    {"user": "bob", "attempts": 2},
    {"user": "charlie", "attempts": "three"},
    {"user": "david", "attempts": 4}
]

def process_security(logs):
     for log in logs:
          user = log["user"]
          try:
               attempts = int(log["attempts"])

               if attempts > 3 :
                    print(f"BLOCK] {user} has too many attempts.")
          except:
               print(f"ERROR] Invalid data for user {user}. Skipping...")
  

process_security(raw_logs)