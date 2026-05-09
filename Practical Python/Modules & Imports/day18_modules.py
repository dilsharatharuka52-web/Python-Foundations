# 🏗️ The os Module: The Operating System Interface

# The os module provides a way of using operating 
# system dependent functionality like reading or writing to the file system, handling paths, and more.
#Key DevOps Use Cases:
      #Environment Variables: Accessing API keys, database URLs, or "PROD/DEV" flags without hard-coding them.  
      #Directory Management: Creating, deleting, or moving folders (though pathlib is now preferred for paths).  
      #Process Information: Getting the Current Working Directory (CWD) or the Process ID (PID).





# code Example:

import os
# 1. Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# 2. check if a folder exists and crate it if not (idempotency)
# if not os.path.exists("logs"):
#     os.mkdir("logs")
#     print("Created 'logs' directory.")
# else:
#     print("'logs' directory already exists.") 



# 3. 👉 “Show all files and folders inside this location.”

files = os.listdir(".")
print("Files and folders in current directory:")
print(files)

# 4. os.path.exists(path) to check if a file or folder exists

check = os.path.exists("logs")
print(f"Does 'logs' directory exist? {check}")


# 4. os.makdirs(folder/subfolder name) to create nested directories in one go (idempotent)
os.makedirs("logs/2024/June", exist_ok=True)
print("Nested directories created (or already exist).")

# 5. Get an environment variable (Critical for security!)
api_key =  os.getenv("AWS_SECRET_KEY", "default_if_missing")
print(f"API Key: {api_key}")












# ⚙️ The sys Module: The Interpreter Interface
# sys module is your bridge to the Python Interpreter itself. it cares about how Python
#  is running your script and what the user typed in the terminal to start it.

# Key DevOps Use Cases:
        # Command-Line Arguments (sys.argv): Making your scripts interactive by taking inputs from the terminal.
        # Script Control: Stopping the script manually with an exit code (sys.exit).
        # Runtime Info: Checking the version of Python or where Python looks for libraries (sys.path).


# 1. Access terminal arguments
# RUN this as: python script.py my_server_name
# 👉 “Get words typed in the terminal.”


import sys
print(f"Command-line arguments: {sys.argv}")


# python script.py my_server_name
# Output: Command-line arguments: ['script.py', 'my_server_name']

# print(f"Script Name: {sys.argv[0]}")
# print(f"User Input: {sys.argv[1]}")

# 2. Exit the script with a custom message and code
# sys.exit("Exiting the script due to an error.")

print("Starting the script...")
# sys.exit()
print("End of the script (this will not print due to sys.exit).")

database_connected = False

if not database_connected:
    print("Database connection failed")
    sys.exit()
print("Continue working")