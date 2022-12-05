# Advent of Code [Dec 5 2022]
# Varun Sreedharan 

with open('day5/input.txt') as f:
    lines = f.readlines()

crates = [['B', 'S', 'V', 'Z', 'G', 'P', 'W'], ['J', 'V', 'B', 'C', 'Z', 'F'], ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'], ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],['G', 'F', 'Q', 'T', 'S', 'L', 'B'],['L', 'G', 'C', 'Z', 'V'],['N', 'L', 'G'],['J', 'F', 'H', 'C']]

inst = lines[10]
inst = inst.strip('move\n')
inst = inst.replace(' from ', '-')
inst = inst.replace(' to ', '-')
inst = inst.split('-')
print(inst)