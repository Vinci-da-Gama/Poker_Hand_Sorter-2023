import os

# Prompt user to enter path to file
test_file = input("Enter Pocker Hand Sorter path to test file: ")

# Open file, read its contents
with open(test_file, 'r') as f:
  lines = f.readlines()

# Remove empty lines
lines = [line.strip() for line in lines if line.strip()]

# Print number of lines in the test file
num_lines = len(lines)
total_lines_printout = '''
input number is: {}
total lines number is: {}
'''.format(str(test_file), str(num_lines))
print(total_lines_printout)
