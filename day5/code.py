import numpy as np 

with open('day5/input.txt') as f: 
    lines = f.readlines()

clean_lines = [[element.split(',') for element in line[:-1].split(' -> ')] for line in lines]

coordinates = np.array(clean_lines).astype(int)

base_dim = np.max(coordinates)+1

base = np.zeros((base_dim, base_dim))

for element in coordinates:
    if (element[0][0] == element[1][0]):
        max_range = max(element[0][1], element[1][1]) +1
        min_range = min(element[0][1], element[1][1])
        for i in range(min_range,max_range):
            base[element[0][0], i] += 1
    else: 
        if (element[0][1] == element[1][1]):
            max_range = max(element[0][0], element[1][0]) +1
            min_range = min(element[0][0], element[1][0])
            for i in range(min_range,max_range):
                base[i, element[1][1]] += 1
        else: 
            max_range = max(element[0][0], element[1][0]) +1
            min_range = min(element[0][0], element[1][0])
            if min_range == element[0][0]:
                min_coordinates = element[0]
                max_coordinates = element[1]
            else: 
                min_coordinates = element[1]
                max_coordinates = element[0]
            if min_coordinates[1] < max_coordinates[1]:
                factor = 1
            else: 
                factor = -1
            for i in range(max_range - min_range):
                base[min_coordinates[0]+i, min_coordinates[1]+(i*factor)] += 1
            

np.sum(base >= 2)

# eligible_coordinates = [element for element in coordinates if (element[0][0] == element[1][0]) or (element[0][1] == element[1][1])]
