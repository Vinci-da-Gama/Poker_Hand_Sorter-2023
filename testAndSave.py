import os
from datetime import datetime

# Prompt user to enter path to file
testFile = input("Enter Pocker Hand Sorter path to test file: ")

# Open file, read its contents
with open(testFile, 'r') as f:
  lines = f.readlines()

# Remove empty lines
lines = [line.strip() for line in lines if line.strip()]

# Print number of lines in the test file
numLines = len(lines)

totalLinesPrintout = '''
input number is: {}
total lines number is: {}
'''.format(testFile, str(numLines))
print(totalLinesPrintout)

# Create test output directory if it doesn't exist
resultDir = "testOutcome"
os.makedirs(resultDir, exist_ok=True)

# Save result to file, file name: result_date_time.txt
now = datetime.now()
dateTimeStr = now.strftime("%Y-%m-%d_%H-%M-%S")
resultFileName = f"result_{dateTimeStr}.txt"
outputPath = os.path.join(resultDir, resultFileName)
with open(outputPath, 'w') as f:
    for line in lines:
        f.write(line + '\n')

# Print message confirming output file has been saved
totalLinesPrintout = '''
file save to: {}
date and time: {}
'''.format(outputPath, dateTimeStr)
print(totalLinesPrintout)
