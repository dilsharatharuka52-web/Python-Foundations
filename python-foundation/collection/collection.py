# Collection = a data structure that can hold multiple values. It is a container for storing and organizing data. Collections are used to group related data together and provide various operations to manipulate that data.
# Types of Collections:
# 1. List = [] - An ordered, mutable collection of items. It can contain duplicate values and can hold different data types.
# 2. Tuple = () - An ordered, immutable collection of items. It can contain duplicate values and can hold different data types.
# 3. Set = {} - An unordered, mutable collection of unique items. It does not allow duplicate values and can hold different data types.
# 4. Dictionary = {} - An unordered, mutable collection of key-value pairs. It does not


# ------- List -------
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

print(fruits[0])  # Output: apple Thsi access the first item in the list use indexing

print(fruits[::2])  # Output: ['apple', 'cherry', 'elderberry'] This access every second item in the list use slicing

print(dir(fruits))  # Output: List of all the methods available for list data type

#print(help(fruits))  # Output: Detailed documentation about the list data type and its methods

print(len(fruits))  # Output: 5 This gives the number of items in the list

print("apple" in fruits)  # Output: True This checks if "apple" is in the list and returns a boolean value

print("mango" in fruits)  # Output: False This checks if "mango" is in the list and returns a boolean value

fruits[0] = "avocado"  # This changes the first item in the list to "avocado"

print(fruits)  # Output: ['avocado', 'banana', 'cherry', 'date', 'elderberry']

fruits.append("fig")  # This adds "fig" to the end of the list

print(fruits)  # Output: ['avocado', 'banana', 'cherry',

fruits.remove("banana")  # This removes "banana" from the list

print(fruits)  # Output: ['avocado', 'cherry', 'date',

fruits.insert(0, "grape") # This inserts "grape" at index 0 (the beginning of the list)

print(fruits)  # Output: ['grape', 'avocado', 'cherry', 'date', 'elderberry']

fruits.sort()  # This sorts the list in alphabetical order

print(fruits)  # Output: ['avocado', 'cherry', 'date', 'elderberry', 'grape']

fruits.reverse()  # This reverses the order of the list

print(fruits)  # Output: ['grape', 'elderberry', '

#fruits.clear()  # This removes all items from the list

#print(fruits)  # Output: []

print(fruits.index("date"))  # Output: 2 This returns the index of the first occurrence of "date" in the list

print(fruits.count("cherry"))  # Output: 1 This counts the number of


# -------- Set --------
unique_numbers = {1, 2, 3, 4, 5,4,3,2,1}  # This creates a set with duplicate values

print(unique_numbers)  # Output: {1, 2, 3, 4, 5} This shows that the duplicate values are removed and only unique values are stored in the

#set cant be accessed by index because it is an unordered collection
#Suport top most of the same methods as list but not all because of the unique and unordered nature of sets

unique_numbers.add(6)  # This adds 6 to the set

print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

unique_numbers.remove(3)  # This removes 3 from the set

print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

print(4 in unique_numbers)  # Output: True This checks if 4 is in the set and returns a boolean value

print(7 in unique_numbers)  # Output: False This checks if 7 is in the set and returns a boolean value


# -------- Tuple --------
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(fruits)  # Output: ('apple', 'banana', 'cherry', 'date', 'elderberry')
# Tuples are ordered and unchangeable, so you cannot modify the items in a tuple after it is created. You can access items in a tuple using indexing and slicing, but you cannot add, remove, or change items in a tuple.


# -------- Dictionary --------

capitals = {
            "USA": "Washington, D.C.", 
            "France": "Paris", 
            "Japan": "Tokyo"
            }

print(capitals)  # Output: {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo'}

print(dir(capitals))  # Output: List of all the methods available for dictionary data type

print(capitals.get("USA"))  # Output: 'Washington, D.C.' This returns the value associated with the key "USA"

capitals.update({"Germany": "Berlin"})  # This adds a new key-value pair to the dictionary

print(capitals)  # Output: {'USA': 'Washington, D.C.', 'France ': 'Paris', 'Japan': 'Tokyo', 'Germany': 'Berlin'}

capitals.update({"USA": "Detroit"})  # This updates the value associated with the key "USA"

print(capitals)  # Output: {'USA': 'Detroit', 'France': 'Paris', 'Japan': 'Tokyo', 'Germany': 'Berlin'}

capitals.pop("France")  # This removes the key-value pair with the key "France" from the dictionary

print(capitals)  # Output: {'USA': 'Detroit', 'Japan': 'Tokyo', 'Germany': 'Berlin'}

capitals.popitem()  # This removes the last inserted key-value pair from the dictionary

print(capitals)  # Output: {'USA': 'Detroit', 'Japan': 'Tokyo

#capitals.clear()  # This removes all key-value pairs from the dictionary

print(capitals)  # Output: {}

print(capitals.keys())  # Output: dict_keys(['USA', 'Japan'])
print(capitals.values())  # Output: dict_values(['Detroit', 'Tokyo'])
print(capitals.items())  # Output: dict_items([('USA', 'Detroit'), ('Japan', 'Tokyo')])



