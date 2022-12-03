# Advent of Code [Dec 1 2022]
# Varun Sreedharan

with open('day1/input.txt') as f:
    lines = f.readlines()
f.close()
templist = []
elfcal = []

# Iterates through lines and creates a temporary list which stores calories 
# for each elf. It then appends the sum of each elve's calories to a elfcal list
for x in lines:
    if x != '\n':
        templist.append(int(x.strip('\n')))
    else:
        elfcal.append(sum(templist))
        templist = []

# prints out elf with biggest calories and the top 3 elves
print(max(elfcal))

elfcal.sort()

print(sum(elfcal[-3:]))