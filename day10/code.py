import numpy as np 

with open('day10/input.txt') as f: 
    lines = f.readlines()

clean_lines = [line[:-1] for line in lines]

c_dict = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
c_dict_reverse = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

c_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

c_errors = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0,
}
c_fill_values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
c_dict.keys()

incomplete_scores = []
c_dict.values()
for line in clean_lines:
    open_characters = []
    corrupted = False
    for i in range(len(line)):
        if line[i] in c_dict.values():
            open_characters.append(line[i])
        else:
            if open_characters[-1] == c_dict[line[i]]:
                open_characters = open_characters[:-1]
            else:
                c_errors[line[i]] +=1
                corrupted = True
                break
    
    # incompleted lines
    if (not corrupted) and (len(open_characters) > 0):
        score = 0 
        open_characters.reverse()
        for char in open_characters: 
            score *= 5
            score += c_fill_values[c_dict_reverse[char]]
        incomplete_scores.append(score)


score = 0
for key in c_values:
    score += c_errors[key] * c_values[key]

np.median(incomplete_scores)