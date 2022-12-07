# Advent of Code [Dec 5 2022]
# Varun Sreedharan 

with open('day5/input.txt') as f:
    lines = f.readlines()

crates = [['B', 'S', 'V', 'Z', 'G', 'P', 'W'], ['J', 'V', 'B', 'C', 'Z', 'F'], ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'], ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],['G', 'F', 'Q', 'T', 'S', 'L', 'B'],['L', 'G', 'C', 'Z', 'V'],['N', 'L', 'G'],['J', 'F', 'H', 'C']]

crates2 = [['B', 'S', 'V', 'Z', 'G', 'P', 'W'], ['J', 'V', 'B', 'C', 'Z', 'F'], ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'], ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],['G', 'F', 'Q', 'T', 'S', 'L', 'B'],['L', 'G', 'C', 'Z', 'V'],['N', 'L', 'G'],['J', 'F', 'H', 'C']]

for i in lines[10:]:
    inst = i
    inst = inst.strip('move\n')
    inst = inst.replace(' from ', '-')
    inst = inst.replace(' to ', '-')
    inst = inst.split('-')
    inst = [int(x) for x in inst]

    for x in range(inst[0]):
        print(crates[inst[2]-1])
        print(crates[inst[1]-1])
        crates[inst[2]-1].append(crates[inst[1]-1][-1])
        crates[inst[1]-1].pop()

    [crates2[inst[2]-1].append(crates2[inst[1]-1][-1*i]) for i in range(inst[0],0,-1)]
    [crates2[inst[1]-1].pop() for i in range(inst[0])]

[print(x[-1]) for x in crates]
print('\n')
[print(x[-1]) for x in crates2]