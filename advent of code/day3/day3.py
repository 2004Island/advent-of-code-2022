# Advent of Code [Dec 3 2022]
# Varun Sreedharan 

with open('day3/input.txt') as f:
    lines = f.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
valkey = {let:int(alphabet.index(let)+1) for let in alphabet}
unique = []
uniquep2 = []

# cool list comprehension that didn't end up working
# for i in lines:
#    [unique.append(x) for x in i[:int((len(i)/2))] if x in i[int((len(i)/2)):]]

# part 1
for i in lines:
    for x in i[:int((len(i)/2))]:
        if x in i[int((len(i)/2)):]:
            unique.append(x)
            break

# part 2
for i in lines[0:len(lines):3]:
    x = lines[lines.index(i): int(lines.index(i))+3]
    x = [i.strip('\n') for i in x]
    for d in x[0]:
        if d in x[1] and d in x[2]:
            uniquep2.append(d)
            break
    
score = sum([valkey[x] for x in unique])
score2 = sum([valkey[x] for x in uniquep2])
print(score)
print(score2)