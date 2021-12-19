import numpy as np 

with open('day18/input.txt') as f: 
    lines = f.readlines()

lines = [line[:-1] for line in lines]

def parse_string(string):
    depth = -1

    string_parsed = [] 
    for character in string:
        if character == '[':
            depth += 1
        elif character == ']':
            depth -= 1
        elif character == ',':
            pass
        else: 
            string_parsed.append([int(character), depth])
    return string_parsed


def explode_number(snail_number, i):
    exploded_number = snail_number
    n_0 = exploded_number[i][0]
    n_1 = exploded_number[i+1][0]
    if i - 1 >= 0:
        exploded_number[i-1][0] += n_0
    if i+2 < len(exploded_number):
        exploded_number[i+2][0] += n_1
    exploded_number = exploded_number[:i] + [[0,3]] + exploded_number[i+2:] 

    return exploded_number

def split_number(snail_number, i):
    num = snail_number[i][0]
    depth = snail_number[i][1]
    n_0 = int(np.floor(num/2))
    n_1 = int(np.ceil(num/2))
    
    splitted_number = snail_number[:i] + [[n_0,depth+1], [n_1, depth + 1]] + snail_number[i+1:] 

    return splitted_number


def reduce_number(snail_number, debug = False):
    reduced_number = snail_number
    reduced = False
    while not reduced:
        if debug: 
            print(reduced_number)
        reduction_done = False
        for i in range(len(reduced_number)):
            number, depth = reduced_number[i]
            if depth == 4:
                reduced_number = explode_number(reduced_number, i)
                reduction_done = True
                break
        if not reduction_done: 
            for i in range(len(reduced_number)):
                number, depth = reduced_number[i]
                if number > 9:
                    reduced_number = split_number(reduced_number, i)
                    reduction_done = True
                    break
        reduced = not reduction_done
    return reduced_number

def add_numbers(sn_1, sn_2):
    addition = []

    for i in sn_1:
        addition.append([i[0], i[1]+1])
    for i in sn_2:
        addition.append([i[0], i[1]+1])
    return addition
    

def get_number_magnitude(number):
    magnitude = number
    for max_depth in [3, 2, 1, 0]:

        suming_number = []
        summed = False
        for i in range(len(magnitude)):
            if summed:
                summed = False
            else:
                number, depth = magnitude[i]
                if depth == max_depth:
                    number_2, depth_2 = magnitude[i+1]
                    suming_number.append([3*number + 2*number_2, depth-1])
                    summed=True
                else: 
                    suming_number.append(magnitude[i])
        magnitude = suming_number

    return magnitude[0][0]


parsed_numbers = [parse_string(line) for line in lines]

max_addition = 0

for i in range(len(parsed_numbers)):
    for j in range(len(parsed_numbers)):
        if i != j:
            addition = reduce_number(add_numbers(parsed_numbers[i], parsed_numbers[j]))
            magnitude = get_number_magnitude(addition)
            if magnitude > max_addition:
                max_addition = magnitude

# Part 1 
addition = None 

if True:
    for number in parsed_numbers:
        if addition is None:
            addition = number
        else: 
            addition = reduce_number(add_numbers(addition, number))
        #print(addition)
get_number_magnitude(addition)
#get_number_magnitude(parse_string('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'))

#addition




