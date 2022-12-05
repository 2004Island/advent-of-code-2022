# Advent of Code [Dec 4 2022]
# Varun Sreedharan 

with open('day4/input.txt') as f:
    lines = f.readlines()

assignmentpaircoun = 0
assignmentpaircounp2 = 0
i = 0 

while i < len(lines):

    elfduty = lines[i].strip('\n')
    elfduty = elfduty.split(',')
    elfduty = [x.split('-') for x in elfduty]
    elfduty = [int(y) for x in elfduty for y in x]

    elfset1 = {x for x in range(elfduty[0], int(elfduty[1] + 1))}
    elfset2 = {x for x in range(elfduty[2], int(elfduty[3] + 1))}

    if elfset1 >= elfset2 or elfset2 >= elfset1:
        assignmentpaircoun += 1

    common = {x for x in elfset1 if x in elfset2}
    common2 = {x for x in elfset2 if x in elfset1}

    if len(common) > 0 or len(common2) > 0:
        assignmentpaircounp2 += 1

    i += 1

print(assignmentpaircoun)
print(assignmentpaircounp2)