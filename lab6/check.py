import os

def delete_file(path):
    try:
        if os.path.exists(path):
            print(f"The path '{path}' exists.")
            if os.path.isfile(path):
                print(f"'{path}' is a file.")
                if os.access(path, os.W_OK):
                    print(f"You have permission to delete '{path}'.")
                    os.remove(path)
                    print(f"File '{path}' deleted successfully.")
                else:
                    print(f"You do not have permission to delete '{path}'.")
            else:
                print(f"'{path}' is not a file.")
        else:
            print(f"The path '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "example.txt" 
delete_file(file_path)