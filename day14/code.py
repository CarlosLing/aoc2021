import numpy as np
import matplotlib.pyplot as plt

file_path = 'day14/input.txt'
def read_advent_14(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    initial_sequence = lines[0][:-1]
    
    insertion_rules = [line[:-1].split(' -> ') for line in lines[2:]]

    insertion_rules_dict = {}

    for rule in insertion_rules: 
        initial, outcome = rule
        insertion_rules_dict[initial] = outcome
    
    initial_state = {}
    set_letters = set()
    for key in insertion_rules_dict.keys():
        set_letters.add(key[0])
        set_letters.add(key[1])
        initial_state[key] = 0

    letters_count = {}

    for letter in set_letters:
        letters_count[letter] = 0
    
    for character in initial_sequence:
        letters_count[character] += 1

    for i in range(len(initial_sequence)-1):
        initial_state[initial_sequence[i:2+i]] += 1
    

    return insertion_rules_dict, initial_state, letters_count

def perform_step(current_state, insertions_rules, letters_count): 
    new_state = current_state.copy()
    new_count = letters_count.copy()
    for rule in insertions_rules:
        occurences = current_state[rule]
        new_element = insertions_rules[rule]
        new_count[new_element] += occurences
        new_state[rule] -= occurences
        new_state[rule[0]+new_element] += occurences 
        new_state[new_element+rule[1]] += occurences
    return new_state, new_count


file_path = 'day14/input.txt'
#file_path = 'day14/sample.txt'

insertions_rules, current_state, letters_count = read_advent_14(file_path)

steps = 40
for i in range(steps): 

    new_state, new_count = perform_step(current_state, insertions_rules, letters_count)
    letters_count = new_count
    current_state = new_state

values = []
for letter in letters_count:
    values.append(letters_count[letter])
np.max(values) - np.min(values)
