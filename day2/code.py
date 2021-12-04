import numpy as np

with open('day2/input.txt') as f: 
    lines = f.readlines()

lines_clean = [l[:-1].split(' ') for l in lines]

actions = ['forward', 'up', 'down']

list_values = []

for action in actions:
    values = [int(line[1]) for line in lines_clean if line[0] == action]
    
    list_values.append(np.sum(values))

list_values[0] * (list_values[2] -list_values[1])

aim = 0
depth = 0 
position = 0
for line in lines_clean: 
    if line[0] == 'forward': 
        position += int(line[1])
        depth += int(line[1])*aim 
    
    
    if line[0] == 'up':
        aim -= int(line[1]) 
    
    if line[0] == 'down': 
        aim += int(line[1])
