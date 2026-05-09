# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#.         useful to break up a large programe reuseable separate files



#x = help("math")
#print(x) # this case will print a list of all the modules available in your Python environment, along with a brief description of each.


# import in mmodules.py
import math
y = math.pi
print(y) # 3.141592653589793

# you can also import specific functions or variables from a module
import math as m

print(m.sqrt(16)) # 4.0

# you can also import specific functions or variables from a module
from math import sqrt, pi
print(sqrt(25)) # 5.0
print(pi) # 3.141592653589793



# crate a module called exsample.py and import it here
import exsample
print(exsample.pi) # 3.14159
print(exsample.square(4)) # 16
print(exsample.cube(3)) # 27
print(exsample.circumferenece(5)) # 31.4159
print(exsample.area(5)) # 78.53975