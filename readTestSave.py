import os
from datetime import datetime

from variables.Cards import cardValues, whoWins, royalFlushValues

# Print message ensure external vars are imported
externalVarsPrintout = '''
cardValues: {}
whoWins: {}
royalFlushValues: {}
'''.format(cardValues, whoWins, royalFlushValues)
print(externalVarsPrintout)

# Define vars for win hands
player1Wins, player2Wins = 0, 0

# Define func to find the rank of a hand
def findRank(hand):
  values = [cardValues[card[0]] for card in hand]
  print('values: ' + str(values))
  suits = [card[1] for card in hand]
  print('suits: ' + str(suits))
  values.sort()
  if len(set(suits)) == 1 and values == royalFlushValues:
    return 9  # Royal Flush
  elif len(set(suits)) == 1 and values == list(range(min(values), max(values) + 1)):
    return 8  # Straight flush
  elif len(set(values)) == 2:
    return 7  # Four of a kind or Full house
  elif len(set(suits)) == 1:
    return 6  # Flush
  elif values == list(range(min(values), max(values) + 1)):
    return 5  # Straight
  elif len(set(values)) == 3 and values.count(values[0]) in (2, 3) and values.count(values[2]) in (2, 3):
    return 4  # Two pairs and Three of a kind
  elif len(set(values)) == 3:
    return 3  # Three of a kind, maybe Two pairs
  elif len(set(values)) == 4:
    return 2  # One pair
  else:
    return 1  # High card

# Define func to compare two hands and return the winner
def matchHands(hand1, hand2):
  rank1, rank2 = findRank(hand1), findRank(hand2)
  if rank1 > rank2:
    return whoWins[0]
  elif rank1 < rank2:
    return whoWins[1]
  else:
    values1, values2 = [cardValues[card[0]] for card in hand1], [cardValues[card[0]] for card in hand2]
    values1.sort(reverse=True), values2.sort(reverse=True)
    for i in range(5):
      if values1[i] > values2[i]:
        return whoWins[0]
      elif values1[i] < values2[i]:
        return whoWins[1]
    return whoWins[2]

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
