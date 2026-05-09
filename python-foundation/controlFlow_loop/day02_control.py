# wite allowed port list

allowed_ports = [22, 80, 443, 8080]

severs = [
        {"name": "Server1", "ports": 22},
        {"name": "Server2", "ports": 80},
        {"name": "Server3", "ports": 443},
        {"name": "Server4", "ports": 8080},
        {"name": "Server5", "ports": 3306},
        {"name": "Server6", "ports": 5432},
        {"name": "Server7", "ports": 6379}
         ]

for sever in severs:
    if sever["ports"] in allowed_ports:
        print(f"{sever["name"]} is onliine {sever["ports"]} is allowed.")
    else:
        print(f"{sever["name"]} is ofline {sever["ports"]} is not allowed.")




    
# Challenge: The "Auto-Healer" Script
# Let's combine these into a mini-project. Imagine you are managing your ThinkPad server.

# The Task:

# Create a list of services: services = ["ssh", "http", "https", "database"].

# Create a dictionary for their status: status = {"ssh": "up", "http": "down", "https": "up", "database": "up"}.

# Use a for loop to go through the services list.

# Inside the loop, use an if/else statement:

# If a service is "down", print: "[ALERT] {service} is offline! Restarting...".

# Else, print: "[OK] {service} is running.".

# Bonus Challenge: Use a while loop to simulate "retrying" the restart of a down service 3 times.

# Would you like to try writing the code for this "Auto-Healer," or should we break down the comparison operators (like ==, !=, >, <) first?




# Crate a list of service

servicres = ["ssh", "http", "https", "database"]

# Ceate a dictionary for their status

status = {
    "ssh": "up",
    "http": "down",
    "https": "up",
    "database": "up"
}

# Use a for loop to go through the servuces list

# for service in servicres: 
#    if status[service] == "down" :
#         print(f"[ALERT] {service} is offline! Restarting...")
#    else:
#         print(f"[OK] {service} is running.")
            


#  Challenge: The "Three-Strike" Restart Rule
# Modify your code so that when a service is "down," the script tries to restart it exactly 3 times 
# using a while loop before moving on to the next service.

# The Logic flow:

# Loop through the services.

# If service is "down":

# Set attempts = 1.

# While attempts <= 3:

# Print "Attempt {attempts}: Restarting {service}...".

# attempts += 1.

# After 3 tries, print "Failed to restart {service}. Escalating to Admin.".  


# set attempts is 1


for service in servicres: 
   if status[service] == "down" :
        
        attempts = 1
        while attempts <= 3 :
             print(f"Attempt {attempts}: Restarting {service}...")
             attempts += 1
        print(f"Failed to restart {service}. Escalating to Admin.")     

else:
        print(f"[OK] {service} is running.")