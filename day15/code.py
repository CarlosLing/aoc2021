import numpy as np
import matplotlib.pyplot as plt

file_path = 'day15/input.txt'

def read_advent_15(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    matrix = [[int(number) for number in line[:-1]] for line in lines] 

    return np.array(matrix)

matrix = read_advent_15(file_path)

s_i = np.shape(matrix)[0]
s_j = np.shape(matrix)[1]
matrix2 = np.zeros((s_i*5, s_j*5))

def m_add(matrix, number):
    new_matrix = matrix+number
    conditions = (new_matrix > 9).astype(int)
    new_matrix = (new_matrix % 10) +  conditions
    return new_matrix

max_number = 5
for i in range(max_number):
    for j in range(max_number):
        matrix2[i*100:(i+1)*100, j*100:(j+1)*100] = m_add(matrix, i+j)

matrix = matrix2
s_i = np.shape(matrix)[0]
s_j = np.shape(matrix)[1]

inf = 100000
seen_nodes = np.zeros(np.shape(matrix))

distances = np.ones(np.shape(matrix))*100000 
origin = [0,0]
distances[origin]

distances[0][0] = 0

#distances[99][99] = -1

np.argmin(distances)


while seen_nodes[499][499] ==0:
    eligible_nodes = distances + inf * seen_nodes
    
    index = np.argmin(eligible_nodes)
    #print(index)
    # Get element
    i = int(index / s_i)
    j = index % s_i

    neighbors = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    node = np.array([i, j])
    for neighbor in neighbors:
        node_n = node + neighbor 
        i_n , j_n = node_n
        i_n = max(0, i_n)
        i_n = min(s_i-1, i_n)
        j_n = max(0, j_n)
        j_n = min(s_j-1, j_n)
        new_distance = distances[i][j] + matrix[i_n][j_n]
        if new_distance <  distances[i_n][j_n]:
            distances[i_n][j_n] = new_distance
    seen_nodes[i][j] = 1 




