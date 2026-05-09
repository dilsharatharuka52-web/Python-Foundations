# Type casting  = the process of converting a veribale form one data type to
#.                 another str(), int(), bool()



name = "Tharuka Dilshara"
age = 25
gpa = 3.5
is_students = True


print(type(name)) # type is use chaeck what data type

gpa = int(gpa) # this type casting change one type to other type

print(gpa)

age = float(age) # this type casting change one type to other type
print(age)

age = str(age) # this type casting change one type to other type
print(type(age))



# The "Type Casting" Challenge
# Let's see if you can handle a real-world scenario. You are writing a script that takes user input for a cloud budget.

# The Task:

# Create a variable input_price = "49.99" (keep it as a string).

# Create a variable input_quantity = "3" (keep it as a string).

# Cast input_price to a float.

# Cast input_quantity to an int.

# Calculate the total (Price × Quantity).

# Print the result: "The total cost is: $" + the total.

# Watch out: For step 6, remember that you cannot add a string and a number. You will need to cast the total back into a string to print it using the + sign, or just use an f-string!



# Define input variables as strings
input_price = "49.99"
input_quantity = "3"

# Cast input_price to float and input_quantity to int
price = float(input_price)
quantity = int(input_quantity)

# Calculate total cost
total_cost = price * quantity
# Print the result using an f-string
print(f"The total cost is: ${total_cost:.2f}")


# he Final Challenge: The Log File Cleaner
# You are reading a log file from your ThinkPad server. The log gives you a string that looks like this: data = "  150 MB  ".

# To use this in your automation, you need to extract the number 150 and add 50 to it to calculate a new limit.

# The Task:

# Start with data = "  150 MB  ".

# Use .strip() to remove the spaces: data.strip().

# Use .replace(" MB", "") to remove the letters: data.replace(" MB", "").

# Cast the result to an integer.

# Add 50 to it and print the final result.

# Why this matters: When you scrape data from your SaaS projects or your local Ollama logs, the data is almost always "dirty" like this.

# How would you write the script to "clean" and "cast" this data?


# Define the raw data string
data = " 150 MB "
# Clean the data by stripping spaces and removing " MB"
cleaned_data = data.strip().replace(" MB", "")  # strip removes leading and trailing spaces, replace removes the " MB" part
#replace() method is used to replace a specified phrase with another specified phrase. In this case, we are replacing " MB" with an empty string "" to remove it from the data.

# Cast the cleaned data to an integer

number = int(cleaned_data)  # Convert the cleaned string to an integer

# add 50 to the number
new_limit = number + 50
# Print the final result
print(f"The new limit is: {new_limit} MB")