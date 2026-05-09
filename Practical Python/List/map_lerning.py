# Map(function, cokkection) = Applies a function to all items in a collection

def c_to_f(temp):
    return (temp * 9/5) +32

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheit_temps = map(c_to_f, celsius_temps)

print(list(fahrenheit_temps))

# Using lambda function with map

fahrenheit_temps = map(lambda temp: (temp * 9/5) +32, celsius_temps)
print(list(fahrenheit_temps))


servers = ["web-prod-01", "web-prod-02", "web-prod-03", "web-prod-04"]

upper_servers = map(lambda server: server.upper(), servers)
print(list(upper_servers))

"""
🎤 Interview Prep (Functional Programming)
Question: "Why might you prefer map() over a list comprehension in a high-performance data pipeline?"

1% Engineer Answer: "The primary advantage of map() is that it returns an iterator rather than a fully realized list.
In a DevOps pipeline processing millions of log entries, using a list comprehension would force Python to store every single transformed entry in RAM simultaneously, 
which could cause an Out-Of-Memory (OOM) error. map() allows us to process items one by one, saving memory and allowing for 'lazy evaluation' until the data is actually needed."
"""