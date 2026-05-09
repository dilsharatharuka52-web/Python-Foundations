"""
you must stop treating file paths as simple "strings." In the past, we used os.path,
 which treated paths like text. pathlib (introduced in Python 3.4) treats paths as objects.

This is the standard for modern DevOps because it handles the difference between Windows (\) 
and Linux/macOS (/) automatically.

"""

from pathlib import Path

# 1. Create a Path object pointing to a file in the current directory
my_path = Path("log")
print(my_path) # log


# 2. Path.cwd() to get the current working directory
current_dir = Path.cwd()
print(f"Current Working Directory: {current_dir}")

# 3. Path.home get the user's home directory
home_dir = Path.home()
print(f"Home Directory: {home_dir}")

# 4. .exists() to check if a file or folder exists

file = Path("logs")
print(file.exists()) # True if log exists, False otherwise

# 5. .is_file() and .is_dir() to check if it's a file or a directory
item = Path("logs")
print(f"Is 'log' a file? {item.is_file()}")
print(f"Is 'log' a directory? {item.is_dir()}")

# 6. .mkdir() to create a new directory (idempotent with exist_ok=True)
new_folder = Path("logs/2024/June")
new_folder.mkdir(parents=True, exist_ok=True)
print("Nested directories created (or already exist).")

# 7. .glob("**/*.py") to find all Python files in the current directory and subdirectories

python_files = list(Path(".").glob("**/*.py"))
print("Python files in current directory and subdirectories:")
for file in python_files:
    print(file)


# 8. .write_text() and .read_text() to write and read text files easily
log_file = Path("logs/2024/June/log.txt")
log_file.write_text("This is a log entry for June 2024.")
print("Log file created and written to.")


# 9. read_text() to read the contents of the file
content = log_file.read_text()
print(f"Content of log file:\n{content}")