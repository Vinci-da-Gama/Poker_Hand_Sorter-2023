from variables.Cards import cardValues, whoWins, royalFlushValues

# Define func to find the rank of a hand
def findRank(hand):
  values = [cardValues[card[0]] for card in hand]
  suits = [card[1] for card in hand]
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
