# Variable = A container for storing data values (int, float, string, etc.)
#          = A Variable behaves as the value that it contains.


#String Variable
first_name = "Tharuka"
food = "Pizza"
email = "tharuka@example.com"

print(first_name)
print(food)
print(email)


print(f"My name is {first_name} and I love {food}. You can contact me at {email}.")
# The f means formatted string literal.
#It lets you insert variables directly inside a string using {}.



#intger Variable
age = 25
year = 2024
number_of_siblings = 2
print(age)
print(year)
print(number_of_siblings)

print(f"I am {age} years old. The current year is {year}. I have {number_of_siblings} siblings.")


#Float Variable
#A float = a number with a decimal point

pi = 3.14159
temperature = 25.5
price = 19.99

print(pi)
print(temperature)
print(price)
print(f"The value of pi is approximately {pi}. The current temperature is {temperature} degrees Celsius. The price of the item is ${price}.")


#Boolean Variable
is_raining = True
is_sunny = False

print(is_raining)
print(is_sunny)
print(f"Is it raining? {is_raining}. Is it sunny? {is_sunny}.")


#tyepe() function = used to determine the type of a variable
print(type(first_name))  # Output: <class 'str'>
print(type(age))         # Output: <class 'int'>
print(type(pi))          # Output: <class 'float'>
print(type(is_raining))  # Output: <class 'bool'>