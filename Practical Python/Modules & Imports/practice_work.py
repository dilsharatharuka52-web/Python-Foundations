import sys
import csv
from pathlib import Path
from datetime import data

def update_student_log(topic, hours):
    log_file = Path('student_log.csv')
    header = ['date', 'topic', 'hours']

    # Check if file exists to decide if we need to write the header
    file_exists = log_file.exists()

    # 1. writing to the Log (DictWriter)
    # newline= '' prevents extra blank line on windows/Linux
    with open(log_file, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)

        if not file_exists:
            writer.writeheader() # Write "date, topic hours" only once

            writer.writerow({
                'date': data.today().isoformat(),
                'topic': topic,
                'hours': hours
            })

    # 2. Reading nd Calculating (DictReader)

    total_hours = 0.0
    print(f"\n{'DATE':<12} | {'TOPIC':<25 | {'HOURS'<5}}")
    print("-" * 50)

    with open(log_file, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            h = float(row['hours'])
            total_hours += h
            print(f"{row['date']:<12} | {row['topic']:<25} | {h:<5}")


    print("-" * 50)
    print(f"📊 TOTAL HOURS STUDIED: {total_hours} hrs")

if __name__ == "__main__":
   if len(sys.argv) >= 3:
         update_student_log(sys.argv[1], sys.argv[2])
   else:
        print("Usage: python practice_work.py <topic> <hours>")

