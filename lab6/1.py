#builtin-function
#1
from functools import reduce
import operator

def multiply_list_numbers(numbers):
    return reduce(operator.mul, numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply_list_numbers(numbers)
print(f"The product of the numbers in the list is: {result}")

#2
def count_upper_lower_case(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

input_string = "Hello World! Python Programming"
upper, lower = count_upper_lower_case(input_string)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

#3
def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

input_string = "A man, a plan, a canal, Panama"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

#4
import time
import math

def delayed_square_root(number, delay_ms):
    delay_seconds = delay_ms / 1000
    return math.sqrt(number)

number = 25100
delay_ms = 2123

print(f"Calculating the square root of {number} after {delay_ms} milliseconds...")
result = delayed_square_root(number, delay_ms)
print(f"The square root of {number} is: {result}")

#5
def all_elements_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = ()

print(f"All elements in {tuple1} are true: {all_elements_true(tuple1)}")
print(f"All elements in {tuple2} are true: {all_elements_true(tuple2)}")
print(f"All elements in {tuple3} are true: {all_elements_true(tuple3)}")

#dir-and-files
#1
import os

def list_directories(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def list_files(path):
    print("Files:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all(path):
    print("All items (directories and files):")
    for item in os.listdir(path):
        print(item)
path = "."
list_directories(path)
list_files(path)
list_all(path)

#2
import os

def check_path_access(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        if os.access(path, os.R_OK):
            print(f"The path '{path}' is readable.")
        else:
            print(f"The path '{path}' is not readable.")
        
        if os.access(path, os.W_OK):
            print(f"The path '{path}' is writable.")
        else:
            print(f"The path '{path}' is not writable.")
        
        if os.access(path, os.X_OK):
            print(f"The path '{path}' is executable.")
        else:
            print(f"The path '{path}' is not executable.")
    else:
        print(f"The path '{path}' does not exist.")
path = "example.txt"  
check_path_access(path)

#3
import os

def check_path_and_extract_details(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        directory = os.path.dirname(path)
        print(f"Directory portion: {directory}")
    
        filename = os.path.basename(path)
        print(f"Filename portion: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path = "example.txt"  
check_path_and_extract_details(path)

#4
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return None

filename = "example.txt"  
line_count = count_lines(filename)

if line_count is not None:
    print(f"The file '{filename}' contains {line_count} lines.")

#5
def write_list_to_file(filename, list_data):
    try:
        with open(filename, 'w') as file:
            for item in list_data:
                file.write(f"{item}\n")
        print(f"List successfully written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "output.txt" 
list_data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"] 

write_list_to_file(filename, list_data)

#6
import os

def generate_text_files():
    try:
        for ascii_value in range(ord('A'), ord('Z') + 1):
            letter = chr(ascii_value)
            filename = f"{letter}.txt"
            with open(filename, 'w') as file:
                file.write(f"This is the content of {filename}.")
            print(f"Created file: {filename}")
        print("All files generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

generate_text_files()

#7
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(contents)
        
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = "example.txt" 
destination_file = "destination.txt" 
copy_file(source_file, destination_file)

#8
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