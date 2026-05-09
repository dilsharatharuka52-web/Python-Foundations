import sys
from pathlib import Path
from datetime import datetime, date

def audit_pythone_files():
    # --- GOAL CALCULATIOOR ---
    # According to your roadmap, you plan to get a job by next year (May)
    # But let's set the target for April 1st, 2027 as requested

    goal_date = date(2027, 4, 1)
    today = date.today()

    # Subtract tow dates crates a 'timedelte' object
    days_remaining = (goal_date - today).days

    # --- TIMESTAMPS ---
    now = datetime.now()

    # strftime fromats the object into a professional string
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"🕒 Audit Started: {timestamp}")
    print(f"📅 Days remaining until April 1st, 2027: {days_remaining} days")
    print("=" * 60)

    # 1. Capture the current directory from CLI
    if len(sys.argv) < 2:
        print("Usage: python3 datetime_work.py <directory_path>")
        sys.exit(1)

    target_path = Path(sys.argv[1])

    if not target_path.exists():
        print(f"Error: The path '{target_path}' does not exist.")
        sys.exit(1)

    print(f"🔍 Auditing Python files in: {target_path}")
    print(f"{'File Path':<50} {'Last Modified':<10}")
    print("-" * 60)

    # Search for all .py files
    python_files = list(target_path.rglob("*.py"))

    if not python_files:
        print("No Python files found.")
        return
    
    for file in python_files:
        if file.is_file():
            size_kb = file.stat().st_size / 1024
            relative_name = str(file.relative_to(target_path))

            # fixed f-string alignment  form our previous lesson
            print(f"{relative_name:<50} {size_kb:>10.2f} KB")
    
    print("-" * 60)
    print(f"Audit Complete at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    audit_pythone_files()