from datetime import datetime, date

current_date = datetime.now()
print("Current date and time:", current_date)

# 2. date.today()

today = date.today()
print("Today's date:", today)

# 3. strftime() - Formatting dates
now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted)

text_date = "2024-06-01"
parsed_date = datetime.strptime(text_date, "%Y-%m-%d")
print("Parsed date:", parsed_date)