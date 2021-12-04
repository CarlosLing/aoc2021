import numpy as np 

with open('day3/input.txt') as f: 
    lines = f.readlines()

lines_clean = [[int(i) for i in l[:-1]] for l in lines]

data = np.array(lines_clean)
l = len(data)
count_columns = np.sum(data, axis=0)
gamma = count_columns > l/2
gamma = gamma.astype(int)
epsilon = count_columns < l/2
epsilon = epsilon.astype(int)
dim = len(data[0])
powers_2 = np.power(2, np.linspace(dim-1, 0, dim))
np.sum(epsilon * powers_2) * np.sum(gamma * powers_2)


import numpy as np 

with open('day3/input.txt') as f: 
    lines = f.readlines()

lines_clean = [[int(i) for i in l[:-1]] for l in lines]

data = np.array(lines_clean)
l = len(data)
dim = len(data[0])

def to_decimal(input):
    dim = len(input)
    powers_2 = np.power(2, np.linspace(dim-1, 0, dim))
    return np.sum(input * powers_2)

data_temp = data
for i in range(dim):
    l = len(data_temp)
    count_columns = np.sum(data_temp, axis=0)
    if l == 1: 
        break
    digit = int(count_columns[i] < l/2)
    data_temp = np.array([dl for dl in data_temp if dl[i] == digit ])

CO2 = to_decimal(data_temp[0])

data_temp = data
for i in range(dim):
    l = len(data_temp)
    count_columns = np.sum(data_temp, axis=0)
    if l == 1: 
        break
    digit = int(count_columns[i] >= l/2)
    data_temp = np.array([dl for dl in data_temp if dl[i] == digit ])

O2 = to_decimal(data_temp[0])

