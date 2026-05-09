#4. Real-World Practice Question for You
# Scenario: Log Rotation and Extraction
# You are managing a web server. Every day, it generates a massive log file called server_logs.txt.
# Each line looks like this:
# [2026-04-25 10:15:30] INFO User logged in
# [2026-04-25 10:16:12] ERROR Database connection timed out
# [2026-04-25 10:18:05] INFO Page loaded

# Your Task:
# Write a Python script that reads server_logs.txt line by line. If a line contains the word "ERROR", append that line to a new file called critical_errors.txt.

from pathlib import Path

server_logs_file = Path("Practical Python/File_I_O/server_logs.txt")
server_log_errors_file = Path("Practical Python/File_I_O/critical_errors.txt")

if not server_logs_file.exists():
    raise FileNotFoundError(f"Required CSV file {server_logs_file} is missing.")
else:
    data = []
    with open(server_logs_file, 'r') as log_file, \
         open(server_log_errors_file, 'a') as errors_file:
          
          for line in log_file:
               if "ERROR" in line:
                    errors_file.write(line)

"""
from pathlib import Path
import sys

# Define paths
server_logs_file = Path("Practical Python/File_I_O/server_logs.txt")
server_log_errors_file = Path("Practical Python/File_I_O/critical_errors.txt")

# 1. Validation
if not server_logs_file.exists():
    # Corrected 'CSV' to 'log' in the error message
    print(f"Error: Required log file {server_logs_file} is missing.")
    sys.exit(1) # 1 meen no sucesss  Exit with error code for automation tools

# 2. Efficient Processing
try:
    with open(server_logs_file, 'r') as log_file, \
         open(server_log_errors_file, 'a') as errors_file:
          
          for line in log_file:
               if "ERROR" in line:
                    errors_file.write(line)
                    
    print("Success: Critical errors extracted.")

except PermissionError:
    print("Error: Insufficient permissions to read/write files.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


    #1. except PermissionError:
        Catches a specific error: PermissionError.
         his happens when your script doesn’t have the right to:
         Read server_logs.txt (file might be read‑only or owned by another user).
         Write/append to critical_errors.txt (e.g., file is write‑protected or in a system folder).
         When this error occurs, it prints a friendly message and the script continues (no crash).

     #2. except Exception as e:
         Catches any other unexpected error (e.g., disk full, invalid file name, encoding issues).
         Exception is the base class for most built‑in errors.
         as e saves the error object into the variable e.
         {e} prints the actual error message (e.g., "No space left on device").
"""