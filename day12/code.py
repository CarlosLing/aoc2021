import numpy as np
from collections import Counter

with open('day12/input.txt') as f: 
    lines = f.readlines()

clean_lines = np.array([line[:-1].split('-') for line in lines])

connections = {}

for edge in clean_lines:
    try: 
        connections[edge[0]].append(edge[1])
    except:
        connections[edge[0]] = [edge[1]]
    
    try: 
        connections[edge[1]].append(edge[0])
    except:
        connections[edge[1]] = [edge[0]]

keys = list(connections.keys())

a = keys[3]
a.isupper()


sequence = ['start']

def get_sequences_end(sequence, extra_visit):
    final_node = sequence[-1]
    sequences = [] 
    for key in connections[final_node]:
        if key.isupper():
            sequences += get_sequences_end(sequence + [key], extra_visit)
        else: 
            if key == 'end': 
                sequences += [sequence + [key]]
            elif not (key in sequence):
                sequences += get_sequences_end(sequence + [key], extra_visit)
            else:
                if key == 'start':
                    pass
                elif not extra_visit:
                    sequences += get_sequences_end(sequence + [key], extra_visit=True)
                else:
                    pass
        
    return sequences

seq = get_sequences_end(sequence, False)
len(seq)

def get_sequences_end(sequence):
    final_node = sequence[-1]
    sequences = [] 
    for key in connections[final_node]:
        if key.isupper():
            sequences += get_sequences_end(sequence + [key])
        else: 
            if key == 'end': 
                sequences += [sequence + [key]]
            elif not (key in sequence):
                sequences += get_sequences_end(sequence + [key])
            else:
                pass
        
    return sequences