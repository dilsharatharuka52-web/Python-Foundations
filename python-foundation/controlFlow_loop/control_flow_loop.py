# IF - Do some code only If some condition is True
#      Else do somthing else

age = int(input("Enter your age"))

if age >= 18:
      print("You can singned up")
elif age <= 0:
      print("Enter valid age")
else:
      print("You age must be 18+ to sign up")


# Exsample 1

response = input("Wouid you like food? (Y/N)")

if response == "Y":
      print("Have some food for you")
else:
      print("No food for you")

#exsample 2
name = input("Eneter your name")

if name == "":
      print("You can't enter your name")
else:
      print(f"your name is {name}")           

#exsample 3
for_sale = False
if for_sale == True:
      print("You can buy somthing in the store")
else:
      print("You can't buy ")     


# for loops = execute a block of code a fixed number of time
#             You can iterate over a range, String, Sequence, etc

for x in reversed(range(1, 11)): # This will print the numbers from 10 to 1 in reverse order
      print(x) # Output: 10 9 8 7 6 5 4 3 2 1

print("Happy New Year!") # Output: Happy New Year! This will print after the loop is finished


for y in range(1,11,3): # This will print the numbers from 1 to 10 with a step of 3
      print(y) # Output: 1 4 7 10



for Z in range(1, 21):
 if Z == 13:
             continue # This will skip the number 13 and continue with the next iteration
 print(Z) # Output: 1 2 3 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20

# while loops = execute a block of code as long as a condition is true

name = input("Enter your name: ")

while name =="":
    print("You can't enter an empty name. Please try again.")
    name = input("Enter your name: ")
print(f"Your name is {name}")    


# exsample 1

age = int(input("Enter your age: "))
while age <= 0:
    print("Please enter a valid age.")
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")   


# exsample 2

food = input("Enter your favorite food: exit 'Q' ")

while not food == "Q":
    print(f"Your favorite food is {food}")
    food = input("Enter your favorite food: exit 'Q' ")
print("Goodbye!")


# exsample 3

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"Please enter a valid number between 1 and 10. {num}")
    num = int(input("Enter a number between 1 and 10: "))
print(f"You entered: {num}")