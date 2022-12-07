# Advent of Code [Dec 6 2022]
# Varun Sreedharan 

with open('day6/input.txt') as f:
    lines = f.readlines()

letters = [x for x in lines[0]]
lists = []
lists2 = []

for i in range(len(letters)):
    sec = {x:letters.index(x) for x in letters[i:i+4]}
    sec2 = {x:letters.index(x) for x in letters[i:i+14]}
    lists.append(sec)
    lists2.append(sec2)

four = [i for i in lists if len(i) == 4]
print(four[0])
string = "".join([str(i) for i in four[0]])
print(lines[0].find(string) + 4)

fourteen = [i for i in lists2 if len(i) == 14]
print(fourteen[0])
string = "".join([str(i) for i in fourteen[0]])
print(lines[0].find(string) + 14)