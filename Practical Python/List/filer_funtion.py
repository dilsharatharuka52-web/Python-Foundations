# filter(funtion, collection) = return all elements that pass condition

def is_passing(grade):
    return grade >= 60

grades = [85, 43, 90, 78, 92, 67, 88]

passing_grades = filter(is_passing, grades)

print(list(passing_grades))

# Using lambda function with filter
passing_grades = filter(lambda grade: grade >= 60, grades)
print(list(passing_grades))


logs = [
    "INFO: System stared",
    "ERROR: Failed to connect to database",
    "INFO: User logged in",
    "ERROR: Disk space low",
    "INFO: System shutdown"
]

def is_error(log):
    return "ERROR" in log
error_logs = filter(is_error, logs)
print(list(error_logs))

"""
🎤 Interview Prep (Topic: Filtering Logic)
Question: "When would you use filter() instead of a list comprehension with an if clause?"

1% Engineer Answer: 
"From a performance standpoint, they are very similar. 
However, filter() is often cleaner when you already have a 
pre-defined validation function or when you want to use it as part
 of a functional pipeline. For example, if I'm chaining operations—filtering logs, 
 then mapping them to a specific format—filter() makes the sequence of events very clear to the next engineer reading my code."
"""