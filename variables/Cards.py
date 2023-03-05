# Define the possible hand ranks
handRanks = {
    'High Card': 1,
    'Pair': 2,
    'Two Pair': 3,
    'Three of a Kind': 4,
    'Straight': 5,
    'Flush': 6,
    'Full House': 7,
    'Four of a Kind': 8,
    'Straight Flush': 9,
    'Royal Flush': 10
}

# Define the card values
cardValues = {
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "T": 10,
  "J": 11,
  "Q": 12,
  "K": 13,
  "A": 14
}

# Define the card suits
# It is useless -- Note - suits are not taken into account to break a tie for this exercise - only the value of the card determines a winner.
# cardSuits = {
#   "D": "Diamonds",
#   "H": "Hearts",
#   "S": "Spades",
#   "C": "Clubs"
# }

# Define the winner
whoWins = {
  "P1": "Player 1",
  "P2": "Player 2",
  "T": "Tie"
}
