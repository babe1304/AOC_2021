import re

lst = [str(x) for x in open("AOC/Day2/input.txt")]
pair = [0, 0]

for string in lst:
    com = re.split('\s', string)
    if com[0] == 'forward':
         pair[0] += int(com[1])
    elif com[0] == 'down':
        pair[1] += int(com[1])
    elif com[0] == 'up':
        pair[1] -= int(com[1])
print(pair[0] * pair[1])

pair = [0, 0]
pair2 = [0, 0]
for string in lst:
    com = re.split('\s', string)
    if com[0] == 'forward':
         pair[0] += int(com[1])
         pair2[1] += (pair2[0] * int(com[1]))
    elif com[0] == 'down':
        pair[1] += int(com[1])
        pair2[0] += int(com[1])
    elif com[0] == 'up':
        pair[1] -= int(com[1])
        pair2[0] -= int(com[1])
print(pair[0] * pair2[1])