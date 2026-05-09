# List comprehension  = A concise to crate list in python
#                       Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]



double =[]
for i in range(1, 11): # range is a built in function that generates a sequence of numbers
    double.append(i*2)
print(double)

# double - [expression for value in iterable if condition]
double = [i * 2 for i in range(1, 11)]
print(double)

# List comprehension in String

fruites = ["apple", "banana", "cherry", "mango"]
fruites_upper = [fruit.upper() for fruit in fruites]
print(fruites_upper)

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)

negative_nums = [num for num in numbers if num < 0]
print(negative_nums)

even_num = {num for num in numbers if num % 2 == 0}
print(even_num)


servers = [
    {"name": "server1", "status": "active"},
    {"name": "server2", "status": "inactive"},
    {"name": "server3", "status": "active"},
    {"name": "server4", "status": "inactive"},
]
active_servers = [server["name"] for server in servers if server["status"] == "active"]
print(active_servers)

user = [{
       "id": 1,
       "name": "John Doe",
       "role": "admin "
     },
     {
         "id": 2,
         "name": "Jane Smith",
         "role": "user"
     },
     {
            "id": 3,
            "name": "Alice Johnson",
            "role": "admin"
     }
     ]

user_id = [user["id"] for user in user]
print(user_id)

"""
🎤 Interview Prep (Topic: Pythonic Code)
    Question: "Why are list comprehensions generally faster
    than a standard for-loop with .append()?"

    1% Engineer Answer: "List comprehensions
    are executed at C-speed inside the Python interpreter.
    When you use .append(), Python has to look up the 'append' 
    attribute of the list object and call it as a function in every single iteration.
    Comprehensions avoid this repeated function call overhead, 
    making them significantly more efficient for large datasets."
"""

