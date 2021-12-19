import numpy as np 

with open('day16/hexadecimal.txt') as f: 
    lines = f.readlines()

lines
dict_hexadec = {}
for line in lines:
    key, binary = line[:-1].split(' = ')
    dict_hexadec[key] = binary 

with open('day16/input.txt') as f: 
    line = f.readlines()

binary = ''
for character in line[0][:-1]:
    binary += dict_hexadec[character]

def binary_to_decimal(binary_input):
    decimal_output = 0
    for i in range(len(binary_input)):
        decimal_output += 2**i * (int(binary_input[(-i-1)])) 
    return decimal_output

packages = []
while len(binary) > 0:
    version_packet = binary[:3]
    type_packet = binary[3:6]
    type_packet = binary_to_decimal(type_packet)
    if type_packet == 4:
        a = binary[7:11]
        b = binary[12:16]
        c = binary[17:21]
        packages.append(binary_to_decimal(a+b+c))
        binary = binary[24:]
    else: 
        l_type = binary[7]
        if l_type == '1':
            length_p = binary[7:22]