import os
from datetime import datetime

from variables.Cards import whoWins
from funcs.MatchHandRank import matchHands

# Define vars for win hands
player1Wins, player2Wins = 0, 0

# Prompt user to enter path to file
testFile = input("Enter Pocker Hand Sorter path to test file: ")

# Open file, read its contents, then compare
with open(testFile, 'r') as readingFile:
  for line in readingFile:
    # Ignore empty lines
    if line.strip() == "":
      continue
    # Parse the hands
    cards = line.strip().split()
    hand1 = cards[:5]
    hand2 = cards[5:]
    print("hand 1:", hand1)
    print("hand 2:", hand2)
    # Compare the hands and update the number of wins
    result = matchHands(hand1, hand2)
    if result == whoWins[0]:
        player1Wins += 1
    elif result == whoWins[1]:
        player2Wins += 1


# Print the results to the terminal
print("\n\nPlayer 1: {}, Player 2: {}".format(player1Wins, player2Wins))

# Create test output directory if it doesn't exist
resultDir = "testOutcome"
os.makedirs(resultDir, exist_ok=True)

# Save result to file, file name: result_date_time.txt
now = datetime.now()
dateTimeStr = now.strftime("%Y-%m-%d_%H-%M-%S")
resultFileName = f"result_{dateTimeStr}.txt"
outputPath = os.path.join(resultDir, resultFileName)

# result dictionary
scores = {whoWins[0]: player1Wins, whoWins[1]: player2Wins}

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
