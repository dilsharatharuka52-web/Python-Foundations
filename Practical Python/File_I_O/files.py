# R = Read
# A = Append
# W = Write
# X = Create


# Read - file
import os

base_dir = os.path.dirname(__file__)          #👉 What it means:
                                              #__file__ → gives the full path of your current Python file
                                              #os.path.dirname(...) → extracts the folder (directory)

file_path = os.path.join(base_dir, "name.txt") #It builds a correct file path safely.

f = open(file_path)
# print(f.read())
# print(f.read(4)) # read 4 caracters
print(f.readline()) # read first line
print(f.readline())


# safe and good way of open file
file_path_2 = os.path.join(base_dir, "sample.txt") #It builds a correct file path safely.

try:
    f = open(file_path_2)
    #print(f.read())
except:
     print("The file you want to read doesn't exist")
finally:
     f.close()

# Append - creates the file if it doesn't exist

try:
     f = open(file_path,"a")
     f.write("Dilhaara\n")
     f.close()
     
     f = open(file_path,"r")
     print(f.read())
except:
     print("can't wite file ")     

finally:
     f.close()

# Write (overwrite)
try:
     f = open(file_path,"w")
     f.write("I delete all thing of code")
     f.close()
     
     f = open(file_path,"r")
     print(f.read())
except:
     print("can't wite file ")     

finally:
     f.close()


# Two ways to create a new file
# Opens a file for writing, creates the fille if it
# dors no exit

f = open("Practical Python/File_I_O/name_list.txt", "w")
f.close()


# Create the specified file, but returns an error
# if the file exists


file_path = "Practical Python/File_I_O/name_tharuka.txt"

if not os.path.exists(file_path):
     f = open(file_path, "x")     # "x" → safe create only 🟢
     f.close()

# Delete a file
# avoid an error if it doesn't exist

if os.path.exists(file_path):
     os.remove(file_path)
else:
     print("The file you wish to delete does not" \
     "exist")    



file_name = "Practical Python/File_I_O/name_list.txt"
file_nams = "Practical Python/File_I_O/name.txt"

with open(file_name) as f:
     content = f.read()

with open(file_nams, "w") as f:
       f.write(content)