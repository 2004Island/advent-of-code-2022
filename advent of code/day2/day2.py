# Advent of Code [Dec 2 2022]
# Varun Sreedharan

with open('day2/input.txt') as f:
    lines = f.readlines()

# Creating dictionaries for all the possible outcomes of RPS and the scores
outcomes = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
outcomesp2 = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}

# Iterates through input.txt and adds the scores to a list. The list is then summed and printed.
score = sum([outcomes[x.strip('\n')] for x in lines])
score2 = sum([outcomesp2[x.strip('\n')] for x in lines])
print(score)
print(score2)