# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
  

file_path = "hello_world.txt"

with open(file_path, "w") as file:
    file.write("Hello, world!")

print(f"File created at: {file_path}")
pass

def task2_read_file():
   # Specify the file path
file_path = "hello_world.txt"  # Make sure this is the correct file path

# Open the file and read its contents
with open(file_path, "r") as file:
    contents = file.read()

# Print the contents of the file
print(contents)
pass

def task3_append_file():
    # Specify the file path
file_path = "hello_world.txt"  # Make sure this is the correct file path

# Open the file in append mode and add a new line of text
with open(file_path, "a") as file:
    file.write("\nThis is a new line of text.")

# Confirm the file has been updated
print(f"New line added to {file_path}")

    pass

def task4_count_lines():
  # Specify the file path
file_path = "hello_world.txt"  # Make sure this is the correct file path

# Open the file and count the number of lines
with open(file_path, "r") as file:
    line_count = sum(1 for line in file)

# Print the number of lines in the file
print(f"The file contains {line_count} lines.")

    pass

def task5_find_word():
    # Specify the file path and the word to search for
file_path = "hello_world.txt"  # Make sure this is the correct file path
search_word = "world"  # Replace with the word you want to search for

# Open the file and search for the word
with open(file_path, "r") as file:
    # Read the contents and count the occurrences of the word
    content = file.read()
    word_count = content.lower().count(search_word.lower())

# Print the result
if word_count > 0:
    print(f"The word '{search_word}' appears {word_count} time(s) in the file.")
else:
    print(f"The word '{search_word}' does not appear in the file.")

    pass

def task6_copy_file():
    # Specify the source and destination file paths
source_file_path = "source_file.txt"  # Replace with your source file
destination_file_path = "destination_file.txt"  # Replace with your destination file

# Open the source file in read mode and the destination file in write mode
with open(source_file_path, "r") as source_file:
    content = source_file.read()

# Write the content to the destination file
with open(destination_file_path, "w") as destination_file:
    destination_file.write(content)

print(f"Contents of '{source_file_path}' have been copied to '{destination_file_path}'.")

    pass

def task7_replace_word():
    # Specify the file path and the words to be replaced
file_path = "hello_world.txt"  # Make sure this is the correct file path
old_word = "world"  # Word to be replaced
new_word = "Python"  # Word to replace with

# Open the file and read its contents
with open(file_path, "r") as file:
    content = file.read()

# Replace the old word with the new word
updated_content = content.replace(old_word, new_word)

# Write the updated content back to the file
with open(file_path, "w") as file:
    file.write(updated_content)

print(f"The word '{old_word}' has been replaced with '{new_word}' in the file.")

    pass

def task8_read_csv():
    import csv

# Specify the file path
file_path = "data.csv"  # Replace with the path to your CSV file

# Open the CSV file and read its contents
with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    
    # Print each row in the CSV file
    for row in csv_reader:
        print(row)

    pass

def task9_write_csv():
   import os
import csv

# Specify the directory you want to list (current directory in this example)
directory_path = "."  # You can change this to any directory path you want

# Get the list of directories in the specified directory
directories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]

# Specify the output CSV file
csv_file_path = "directories_list.csv"

# Write the list of directories to a CSV file
with open(csv_file_path, mode="w", newline="") as file:
    csv_writer = csv.writer(file)
    
    # Write the header (optional)
    csv_writer.writerow(["Directory Name"])
    
    # Write each directory name as a new row in the CSV file
    for directory in directories:
        csv_writer.writerow([directory])

print(f"List of directories has been written to '{csv_file_path}'.")
import os
import csv

# Specify the directory you want to list (current directory in this example)
directory_path = "."  # You can change this to any directory path you want

# Get the list of directories in the specified directory
directories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]

# Specify the output CSV file
csv_file_path = "directories_list.csv"

# Write the list of directories to a CSV file
with open(csv_file_path, mode="w", newline="") as file:
    csv_writer = csv.writer(file)
    
    # Write the header (optional)
    csv_writer.writerow(["Directory Name"])
    
    # Write each directory name as a new row in the CSV file
    for directory in directories:
        csv_writer.writerow([directory])

print(f"List of directories has been written to '{csv_file_path}'.")

    pass

def task10_json_file():
    import json

# Define a Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

# Specify the path for the JSON file
json_file_path = "data.json"

# Write the dictionary to a JSON file
with open(json_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)  # `indent=4` is used to format the JSON nicely

print(f"JSON data has been written to '{json_file_path}'.")

# Read the data back from the JSON file
with open(json_file_path, "r")

    pass
