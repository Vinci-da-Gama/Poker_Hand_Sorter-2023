import os

# Prompt user to enter path to file
test_file = input("Enter Pocker Hand Sorter path to test file: ")

# Open file, read its contents
with open(test_file, 'r') as f:
    file_contents = f.read()

# Print number of lines in the test file
num_lines = len(file_contents.split('\n'))
print(f"File {test_file} has been read. {num_lines} lines have been read.")
