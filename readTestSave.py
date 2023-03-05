import os
from datetime import datetime

from variables.Cards import handRanks, cardValues, whoWins

# Print message ensure external vars are imported
externalVarsPrintout = '''
handRanks: {}
cardValues: {}
whoWins: {}
'''.format(handRanks, cardValues, whoWins)
print(externalVarsPrintout)

# Define vars for win hands
player1_wins, player2_wins = 0, 0

# Define func to find the rank of a hand
def findRank(hand):
  values = [cardValues[card[0]] for card in hand]
  print('values: ' + str(values))
  suits = [card[1] for card in hand]
  print('suits: ' + str(suits))
  values.sort()
  if len(set(suits)) == 1 and values == [10, 11, 12, 13, 14]:
    return 9  # Royal flush
  elif len(set(suits)) == 1 and values == list(range(min(values), max(values) + 1)):
    return 8  # Straight flush
  elif len(set(values)) == 2:
    return 7  # Four of a kind or Full house
  elif len(set(suits)) == 1:
    return 6  # Flush
  elif values == list(range(min(values), max(values) + 1)):
    return 5  # Straight
  elif len(set(values)) == 3 and values.count(values[0]) in (2, 3) and values.count(values[2]) in (2, 3):
    return 4  # Two pairs or Three of a kind
  elif len(set(values)) == 3:
    return 3  # Three of a kind or Two pairs
  elif len(set(values)) == 4:
    return 2  # One pair
  else:
    return 1  # High card

# Define func to compare two hands and return the winner
# TODO: find the Rank for hand1 and hand2




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
    # TODO: compare and get winner, if player 1, then player 1 +1, if player 2 then p2 +1

# Print the results to the terminal
print("Player 1: {}, Player 2: {}".format(player1_wins, player2_wins))












# Create test output directory if it doesn't exist
resultDir = "testOutcome"
os.makedirs(resultDir, exist_ok=True)

# Save result to file, file name: result_date_time.txt
now = datetime.now()
dateTimeStr = now.strftime("%Y-%m-%d_%H-%M-%S")
resultFileName = f"result_{dateTimeStr}.txt"
outputPath = os.path.join(resultDir, resultFileName)


# result dictionary
scores = {"Player 1": player1_wins, "Player 2": player2_wins}

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
