# poker-hand-soter-argenti-2023

- ✨sort and compare ✨

### Installation

Requires [Python3](https://www.python.org/downloads/)

### Run

```sh
git clone https://github.com/Vinci-da-Gama/Poker_Hand_Sorter-2023.git
cd Poker_Hand_Sorter-2023

```
### Development steps:

> Step 1
Read the File, then count how many lines are in that file, if the line is empty, then clear the empty line, and then keep reading the rest to the end of the file. When the read is completed, then print out how many lines are read.

> Step 2
Save the result about the total number of lines into a specific folder(testOutcome) and file(result_{date}_{time}.txt).
The result should be like, providing `temporary fake scores` for these 2 players.:
```sh
Player 1: {num}
Player 2: {num}
```

> Step 3
Learn and understand the poker hand rules. Split 1 line into 2 lists.
['AH', '9S', '4D', 'TD', '8S'] -- Player 1
['4H', 'JS', '3C', 'TC', '8D'] -- Player 2

> Step 4
Take 1 line [AH 9S 4D TD 8S 4H JS 3C TC 8D], split that line into 2 arrays, then compare according to the poker hand sorter rules, then record the result, and also display the result in the terminal and file.

1. split 1 line
2. find the rank for each hand
3. return hand rank to find who is the winner
4. +1 for the winning hand for each winner
5. print the result into terminal

> Step 5
Try 3 lines, and move funcs to an external file.

> Step 6
Test the file provided -- poker-hands.txt
result is --> Player 1: 255, Player 2: 245

> Step 7
Remove unnecessary printout and optimize the code.
