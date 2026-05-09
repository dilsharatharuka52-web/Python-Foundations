# function = A block of reusable code place () after the funtion name to invoke it
#            A function can take arguments (input) and return a value (output)






# 1. def (The Definition)

   #def is the keyword used to define a function. Think of a function as a "recipe" or a "stored procedure." 
   # It doesn't run when you define it; it only runs when you call it.

def name():
    print("Tharuka Dilshara 1")
    print("Tharuka Dilshara 2")
    print("Tharuka Dilshara 3")
    print("Tharuka Dilshara 4")
    print("Tharuka Dilshara 5")
    print()


name()
name()


# 2. args (The Inputs/Arguments)
   #Arguments are the data you pass into the function so it can do its job. In DevOps, this is usually a server IP, a filename, or a threshold.
   #Standard Args: Positional inputs.
   #Default Args: Inputs that have a fallback value if you don't provide one.

def invoice(billNo, ammount, date = "1/2"):
    print(f"Bill Number is {billNo}")
    print(f"Ammount of bill is {ammount} and date is {date}")
    print()

invoice(2,3000,"2/9")
invoice(3,3000,)


# 3. return (The Output)
    #return is how a function sends data back to the main part of your script. 
    #Without return, a function just performs an action and "dies."


def hadd_heltch():
       usage = 80
       return usage


curent_usage = hadd_heltch()

if curent_usage >= 80:
    print("HDD is full  now")


 # 4. Scope (The "Boundary")

# Scope determines where a variable can be seen or used.

#    Local Scope: A variable created inside a function stays inside.

#    Global Scope: A variable created outside is visible to everyone.
# this case use Scope resolution = (LEGB) Loacl -> Enclosed -> Global -> Built-in
 
server_name = "ThinkPad-Server" # GLOBAL (Available everywhere)

def rename_server():
    new_name = "ThinkPad-Alpha" # LOCAL (Only exists inside this function)
    print(f"Internal name: {new_name}")

rename_server()
# print(new_name)  <-- This would ERROR because 'new_name' is local to the function.