import os
import sys

def list_my_files():
    """ 1 Use sys.argv to get the folder name from the terminal """
    if len(sys.argv) < 2:
        print("❌ Error: You forgot to provide a folder name!")
        print("Usage: python3 work.py <folder_name>")
        sys.exit(1)  # Exit with an error code


    folder_name = sys.argv[1]

    """ 2 Use os.path exists to verify the folder """
    if not os.path.exists(folder_name):
        print(f"❌ Error: The folder '{folder_name}' does not exist.")
        sys.exit(1)

    """ 3 Use os.getcwd to show the starting point """
    print(f"📍 Current Path: {os.getcwd()}")
    print(f"📂 Listing files in: {folder_name}\n" + "="*40)

    # 4. Use os.listdir to see what's inside
    try:
        files = os.listdir(folder_name)
        if not files:
            print("📂 The folder is empty.")
        else:
            for file in files:
                print(f"📄 {file}")
    except PermissionError:
       print("❌ Permission Denied: You don't have rights to view this.")

if __name__ == "__main__":
    list_my_files()