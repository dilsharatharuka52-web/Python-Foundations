# The Question:
# "We have a legacy system that outputs an inventory 
# file called inventory.csv containing two columns: 
# ServerName and IPAddress. Our new infrastructure 
# automation tool requires this data in JSON format. W
# rite a Python script to read the CSV and output a file 
# called inventory.json. How would you handle a situation where t
# he CSV file doesn't exist?"

# What the Interviewer is looking for:
       # 1. Do you use the CSV and JSON modules ?
       # 2. Do you use the with statement ?
       # 3. Do you handel the FileNoEoundError gracefully ?

import csv
import json
from pathlib import Path

csv_file = Path("Practical Python/File_I_O/inventory.csv")
json_path = Path("Practical Python/File_I_O/inventory.json")

# Check if file exist first
if not csv_file.exists():
  # What it does
  # raise – Manually triggers an exception (stops normal execution and jumps to error handling, if any).
  # FileNotFoundError – A built-in Python exception that signals a missing file or directory.
  # f"Required CSV file {csv_file} is missing." – An f-string that inserts the variable csv_file (the file path) into the message.

    raise FileNotFoundError(f"Required CSV file {csv_file} is missing.")
else:
    data = [] # this a list to store the data from csv file
    with open(csv_file, 'r') as f:
        # What csv.DictReader(f) does
        # csv.DictReader(f) is a class from Python’s built-in csv module. 
        # It reads a CSV file and returns each row as an ordered dictionary (or a regular dict in modern Python), where:
        # Keys = column headers taken from the first row of the CSV file.
        # Values = the data in that row, mapped to the corresponding header.

        reader = csv.DictReader(f)

        #for row in reader – A loop that goes through the CSV file one row at a time,
        #  assigning the current row to the variable row.

        for row in reader:
            data.append(row) # adds the current row (as a dictionary) to the data list.
        with open(json_path, "w") as json_file:
            json.dump(data, json_file, indent=4) # writes the data list to the JSON file in a human-readable format with indentation.       

