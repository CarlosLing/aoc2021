import numpy as np
import matplotlib.pyplot as plt


def read_advent_13(file_path): 
    with open(file_path) as f: 
        lines = f.readlines()

    clean_lines = [line[:-1].split(',') for line in lines]

    dots = [line for line in clean_lines if len(line) == 2]

    instuctions = [line for line in clean_lines if len(line) == 1][1:]
    instuctions = [line[0].split(' ')[-1].split('=') for line in instuctions]
    
    dots = np.array(dots, int)

    return dots, instuctions


def flip_dot(dot, position, direction): 
    new_dot = dot
    remove_dot = False
    if direction == 'x':
        if new_dot[0] == position: 
            remove_dot = True
        elif new_dot[0] > position:
            new_dot[0] = 2*position - new_dot[0]
        
    elif direction == 'y':
        if new_dot[1] == position: 
            remove_dot = True
        elif new_dot[1] > position:
            new_dot[1] = 2*position - new_dot[1]

    else: 
        raise ValueError(f'Position {position} is not implemented')

    if remove_dot: 
        return None
    else: 
        return new_dot

# def remove_duplicates(): 

def fold_dots(dots, position, direction): 
    new_dots = []
    for dot in dots: 
        nd = flip_dot(dot, position, direction)
        new_dots.append(nd)
    return new_dots
       

def print_dots(dots): 

    base = np.zeros((max(dots[:, 0])+1,max(dots[:, 1])+1))

    for dot in dots: 
        i, j = dot 
        base[i, j] = 1 
    
    print(np.sum(base))
    plt.imshow(base)
    plt.show()



def solve_advent_13(file_path): 

    dots, instructions = read_advent_13('day13/input.txt')
    # i =  
    for i in instructions: 

        dots_new = np.array(fold_dots(dots, int(i[1]), i[0]))
        dots = dots_new
        
        print_dots(dots_new)

