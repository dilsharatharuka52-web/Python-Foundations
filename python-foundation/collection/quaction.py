# The Challenge: "The Multi-Cloud Inventory"
# In this scenario, you are writing a script to track which AI models are running on which cloud providers.

# The Task:

# List: Create a list named active_regions containing "us-east-1", "eu-west-1", and "ap-south-1".

# Dictionary: Create a dictionary named model_config with these keys:

# "name": "Llama-3"

# "parameters": "70B"

# "quantization": "4-bit"

# Set: Create a set named unique_errors containing "Timeout", "OutOfMemory", and "Timeout". (Notice how Python handles the duplicate).

# Operations:

# Add a new region "us-west-2" to your list.

# Update the "quantization" in your dictionary to "8-bit".

# Print the total number of items in your unique_errors set using len().



# Crate a list of active regions
active_regions = ["us-east-1", "eu-west-1", "ap-south-1"]

# Crate a dictionary of model configuration

model_config = {
    "name": "Llama-3",
    "parameters": "70B",
    "quantization": "4-bit"
}

# Create a set names unique errors

unique_errors = {"Timeout", "OutOfMemory", "Timeout"}

# Add a new region to the List

active_regions.append("us-west-2")

# Update the quantization in the dictionary

model_config.update({"quantization": "8-bit"})

# Print the total number of items in the unique_errors set

print(f"Total unique errors: {len(unique_errors)}")



# Challenge: The "Cloud Resource" Nested Dictionary
# In professional cloud architecture (like AWS or Azure), data is often nested. This means a dictionary might contain a list, or a list might contain many dictionaries.

# The Task:

# Create a dictionary called infrastructure.

# Inside it, create a key called "servers" which has a list of two strings: "ThinkPad" and "MacBook".

# Inside it, create another key called "status" which is a dictionary with: "online": True and "uptime_days": 15.

# The Goal: Print the value of "uptime_days" by navigating through the infrastructure dictionary.

# Hint: You can "chain" your keys like this: infrastructure["key1"]["key2"].

# How would you structure this nested resource?


# Crate a nested dictionary for infrastructure

infrastructure = {
    "servers" : ["Thinkpad", "MacBook"],
    "status" : {
          "online" : True,
          "uptime_days" : 15,
    }
}

# print the value of uptime_days 

print(f"Uptime Days: {infrastructure['status']['uptime_days']}")


