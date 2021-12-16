import numpy as np
from numpy.lib.type_check import imag 

with open('day11/input.txt') as f: 
    lines = f.readlines()

clean_lines = np.array([ [int(num) for num in line[:-1]] for line in lines])

def explode_octopus(octopus): 
    new_octopus = octopus
    max_octopus = np.max(octopus)
    exploded_octopus = np.zeros(np.shape(octopus))
    while max_octopus > 9: 
        explosion_additions = np.zeros(np.shape(octopus))
        new_explosions = (new_octopus > 9) * (np.logical_not(exploded_octopus))
        for i in range(np.shape(new_explosions)[0]):
            for j in range(np.shape(new_explosions)[1]): 
                if new_explosions[i][j]:
                    i_mi = max(i-1, 0)
                    j_mi = max(j-1, 0)
                    i_ma = min(i+2, np.shape(new_explosions)[0])
                    j_ma = min(j+2, np.shape(new_explosions)[1])
                    explosion_additions[i_mi:i_ma,j_mi:j_ma] += 1
                    exploded_octopus[i,j] = True
        new_octopus = new_octopus + explosion_additions 
        max_octopus = np.max(new_octopus * (np.logical_not(exploded_octopus)))
    final_octopus = new_octopus * (np.logical_not(exploded_octopus))
    return final_octopus, np.sum(exploded_octopus)
        

n_steps = 100
status = clean_lines
total_flashes = 0
i = 0
sum_octopus = 1
while sum_octopus > 0:
    i += 1
    step = np.ones(np.shape(clean_lines), int)
    
    updated_status = step + status

    status, flashes = explode_octopus(updated_status)
    total_flashes += flashes
    sum_octopus = np.sum(status)





