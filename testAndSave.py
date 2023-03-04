import os
from datetime import datetime

from variables.Cards import handRanks, cardValues, cardSuits

# Prompt user to enter path to file
testFile = input("Enter Pocker Hand Sorter path to test file: ")

# Open file, read its contents
with open(testFile, 'r') as readingFile:
  lines = readingFile.readlines()

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

# Print message ensure external vars are imported
externalVarsPrintout = '''
handRanks: {}
cardValues: {}
cardSuits: {}
'''.format(handRanks, cardValues, cardSuits)
print(externalVarsPrintout)

# tmp fake scores
scores = {"Player 1": 1, "Player 2": 2}

with open(outputPath, 'w') as resultFile:
  for player, score in scores.items():
    resultFile.write(f"{player}: {score}\n")

# finish and close file
resultFile.close()

# Print message confirming output file has been saved
outputFilePrintout = '''
file save to: {}
date and time: {}
'''.format(outputPath, dateTimeStr)
print(outputFilePrintout)
