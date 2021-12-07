import numpy as np 

from collections import Counter

with open('day6/input.txt') as f: 
    lines = f.readlines()


lanterns = np.array(lines[0][:-1].split(',')).astype(int)

a = dict(Counter(lanterns))

lanterns_vector = np.zeros(9).astype(np.longlong)

for key in a:
    lanterns_vector[key] = a[key]

n_days = 256
for i in range(n_days):
    new_lanterns = lanterns_vector[0]
    lanterns_vector[:-1] = lanterns_vector[1:]
    lanterns_vector[-1] = 0
    lanterns_vector[6] += new_lanterns
    lanterns_vector[8] += new_lanterns

sum(lanterns_vector)