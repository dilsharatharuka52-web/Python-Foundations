import csv

# 1 csv.DictWiter() writes a list of dictionaries to a csv file
with open('csv_dict_writer.csv', 'w', newline='') as file:

    headers = ['name', 'age', 'city']
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30, 'city': 'New York'})
    writer.writerow({'name': 'Bob', 'age': 25, 'city': 'Los Angeles'})
    writer.writerow({'name': 'Charlie', 'age': 35, 'city': 'Chicago'})


# 2 csv.DictReader() reads a csv file and returns a list of dictionaries
with open('csv_dict_writer.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


# 3 csv.writer() writes a list of lists to a csv file
with open('csv_writer.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
    writer.writerow(['Charlie', 35, 'Chicago'])