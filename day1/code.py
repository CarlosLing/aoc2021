import numpy as np

with open('day1/input.txt') as f: 
    lines = f.readlines()

lines_clean = [int(l[:-1]) for l in lines]

numbers = np.array(lines_clean)

numbers_x3 = numbers[:-2]+numbers[1:-1]+numbers[2:]
numbers = numbers_x3
numbers_1 = numbers[1:]
numbers_0 = numbers[:-1]

diff = numbers_1 - numbers_0

sum(diff < 0) 