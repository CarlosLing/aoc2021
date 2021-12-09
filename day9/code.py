import numpy as np 
import matplotlib.pyplot as plt

with open('day9/input.txt') as f: 
    lines = f.readlines()

clean_lines = np.array([[int(a) for a in line[:-1]] for line in lines])

padded_map = np.pad(clean_lines, 1, 'constant', constant_values=(9))

lenght = len(padded_map)
width = len(padded_map[0])

sum = 0

covered = np.zeros((lenght, width))
lowest_point = (100, 81)
def get_basin_size(lowest_point, padded_map):
    basin = set([lowest_point])
    not_finished = True 
    while not_finished: 
        appended_basin = basin.copy()
        for element in basin: 
            i, j = element
            covered[i][j] = 1
            adjacent_elements = [
                [i, j+1],
                [i, j-1],
                [i+1, j],
                [i-1, j]]
            for a_element in adjacent_elements: 
                i_a, j_a = a_element
                if (padded_map[i][j] <= padded_map[i_a][j_a]) and padded_map[i_a][j_a] < 9: 
                    appended_basin.add(tuple(a_element))
                

        not_finished = appended_basin != basin
        print(appended_basin)
        print(basin)
        basin = appended_basin
    return len(basin)

basins = []



for i in range(1, lenght-1):
    for j in range(1, width-1):
        if padded_map[i][j] == 9:
                    covered[i][j] = 1
        min_adjacents = min([padded_map[i-1][j], padded_map[i+1][j], padded_map[i][j-1], padded_map[i][j+1]])
        if min_adjacents > padded_map[i][j]:
            basins.append(get_basin_size(tuple([i, j]), padded_map))

plt.imshow(padded_map)
plt.show()
plt.imshow(covered)
plt.show()

np.sort(basins)
