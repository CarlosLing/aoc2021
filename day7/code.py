import numpy as np 


with open('day7/input.txt') as f: 
    lines = f.readlines()


crabs = np.array(lines[0][:-1].split(',')).astype(int)

fuels = []


for i in range(np.max(crabs)):

    distance = np.abs(crabs - i)
    fuel = np.sum((1+distance)/2*distance)
    fuels.append(fuel)

np.min(fuels)