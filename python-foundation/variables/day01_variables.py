# --- Day 01 : variables and data types ---
# 1. Variables Assignments (basic Types)

project_name = "python-foundation" #String variable
version = 1                      #Integer variable
success_rate = 0.95                #Float variable
is_active = True                #Boolean variable


#. Using f-strings to print variables
#f-string = formatted string literal so Use f-string to include variables in a string
print("-------- Project Status --------")
print(f"Project Name: {project_name}")
print(f"Version: {version}")
print(f"Success Rate: {success_rate}")
print(f"Is Active: {is_active}")


# 3. Type Conversion
# Somtimes data comes as text (from a file or user) and need to be a number
string_id = "12345"
integer_id = int(string_id)  # Convert string to integer
print(f"String ID: {string_id} (type: {type(string_id)})")

pi_value = "3.14159"
float_pi = float(pi_value)   # Convert string to float
print(f"Pi Value: {float_pi} (type: {type(float_pi)})")

# 4.Operations and Logic 

new_version = version + 1
statud_msg = "Upgrade to Vesion " + str(new_version)  # Convert integer to string for concatenation

print(f"\n---- Data Conversion & Logic ----")
print(f"Converted ID: {integer_id} (type: {type(integer_id)})")
print(f"Pi as a string: {pi_value} (type: {type(pi_value)})")
print(f"New Version: {new_version} (type: {type(new_version)})")
print(f"Status Message: {statud_msg}")

#5. Type Checking
print(f"\n---- Type Checking ----")
print(f"Type of project_name: {type(project_name)}")
print(f"Type of version: {type(version)}")
print(f"Type of success_rate: {type(success_rate)}")
print(f"Type of is_active: {type(is_active)}")



#
host = int(input("Enter the host: "))
print(f"You entered: {host} (type: {type(host)})")

#A real DevOps script never waits for a human to type something — it runs automatically, unattended, in a pipeline or cron job at 3am with no one watching.