import os
from datetime import datetime

from variables.Cards import whoWins, resultDir
from funcs.MatchHandRank import matchHands

# result dictionary
scores = {whoWins[0]: 0, whoWins[1]: 0}

# Prompt user to enter path to file
testFile = input("Enter Pocker Hand Sorter path to test file: ")

# Open file, read its contents, then compare
with open(testFile, 'r', encoding='utf-8') as readingFile:
  for line in readingFile:
    # Ignore empty lines
    if line.strip() == "":
      continue
    # Split the line into 2 lists for 2 players
    cards = line.strip().split()
    hand1 = cards[:5]
    hand2 = cards[5:]
    # Compare the hands and update the number of wins
    RESULT = matchHands(hand1, hand2)
    if RESULT != whoWins[2]:
      scores[RESULT] += 1

# Print the results to the terminal
print(f"\nPlayer 1: {scores[whoWins[0]]}, Player 2: {scores[whoWins[1]]}")

# Create test output directory if it doesn't exist
os.makedirs(resultDir, exist_ok=True)

# Save result to file, file name: result_date_time.txt
dateTimeStr = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
resultFileName = f"result_{dateTimeStr}.txt"
outputPath = os.path.join(resultDir, resultFileName)

with open(outputPath, 'w', encoding='utf-8') as resultFile:
  for player, score in scores.items():
    resultFile.write(f"{player}: {score}\n")

# finish and close file
resultFile.close()

# Print message confirming output file has been saved
outputFilePrintout = '''
File save to: {}
Date and time: {}
'''.format(outputPath, dateTimeStr)
print(outputFilePrintout)
