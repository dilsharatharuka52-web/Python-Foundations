# Challenge 1: The Server Status Dashboard (Variables & Logic)
#              In DevOps, you often collect data from multiple servers.

#        Task: Create three variables representing three different servers: server_1, server_2, and server_3.

#        Assign them the string values "Online", "Offline", and "Maintenance".

#         Create a fourth variable called total_online that calculates how many servers are currently "Online".

#         Goal: Practice using variables to track system states.


# Define server status variables
server_1 = "online"
server_2 = "online"
server_3 = "maintenance"

# Calculate total online servers
total_online = 0

# for server in [server_1, server_2, server_3]:
#     if server == "online":
#         total_online += 1


 #In Python, if you want to count items in a list that match a specific value, there is a very fast "shorthand" method:

server = [server_1, server_2, server_3]
total_online = server.count("online")

# Print the results
print(f"Server 1 Status: {server_1}")
print(f"Server 2 Status: {server_2}")
print(f"Server 3 Status: {server_3}")
print(f"Total Online Servers: {total_online}")




#Challenge 2?
# Now, let's try the Infrastructure Cost Estimator. This one is crucial for LLMOps because GPU costs are very high, and you’ll often need to script budget reports.

# The Task:

# Set gpu_hourly_rate = 2.45

# Set number_of_gpus = 8

# Set hours_per_month = 720

# Calculate total_cost and print it using an f-string.

# Bonus Tip: In your f-string, you can format the price to two decimal places like this: f"{total_cost:.2f}".

# Give it a shot!


# Define cost variables
gpu_hourly_rate = 2.45
number_of_gpus = 8
hourly_per_month = 720

# Calculate total cost
total_cost = gpu_hourly_rate * number_of_gpus * hourly_per_month

# Print the total cost with formatting
print(f"Total Monthly GPU Cost: ${total_cost:.2f}")


# This final challenge combines your Python skills with your interest in LLMOps. In a real-world scenario, you might have a Python script that monitors your AI models and reports their status.

# The Task:

# Create these variables:

# model_name = "Llama-3"

# is_active = True (Boolean)

# accuracy_score = 0.9458 (Float)

# The Goal: Print a summary message using an f-string.

# The Requirement: Format the accuracy_score as a percentage with one decimal place (e.g., 94.6%).

# Hint: In an f-string, you can convert a decimal to a percentage automatically using :.1%. For example: {0.5: .1%} becomes 50.0%.

# How would you write the print statement for this AI report?


# Define model variables
model_name = "Llama-3"
is_active = True
accuracy_score = 0.9458

# Print the summary message with formatted accuracy score
print(f"Model Name: {model_name}")
print(f"Active Status: {'Active' if is_active else 'Inactive'}")
print(f"Accuracy Score: {accuracy_score:.1%}")

