import sys
from pathlib import Path

def audit_python_files():
    # 1. Capture target directory from CLI
    if len(sys.argv) < 2:
        print("Usage: python3 day18_modules_pathlib.py <target_directory>")
        sys.exit(1)

    # 2. Convert string input into a Path object
    target_path = Path(sys.argv[1])

    if not target_path.exists():
        print(f"Error: The directory '{target_path}' does not exist.")
        sys.exit(1)

    print(f"🔍 Auditing Python files in: {target_path.resolve()}") # get full path of file or folder
    print(f"{'File Name':<40} | {'Size (KB)':>10}")# make a header with left and right alignment
    print("-" * 55)

    # 3. Use .glob('**/*.py') - Recursive search for all .py files
    # We use .rglob('*.py) as a shortcut for recursive globbing
    python_files = list(target_path.rglob('*.py'))

    if not python_files:
        print("No .py files found.")
        return
    
    total_size  = 0

    for file in python_files:
        if file.is_file(): 
            size_kb = file.stat().st_size / 1024 
            total_size += size_kb
            
            # FIXED LINE: Added colon, removed spaces, kept relative path
            relative_name = str(file.relative_to(target_path))
            print(f"{relative_name:<40} | {size_kb:>10.2f} KB")


    print("-" * 55)
    print(f"✅ Total Python Codebase Size: {total_size:.2f} KB")



if __name__ == "__main__":
    audit_python_files()


