import numpy as np 


with open('day8/input.txt') as f: 
    lines = f.readlines()

clean_lines = [line[:-1].split(' | ')[1].split(' ') for line in lines]

length_numebers = [[len(number) for number in line] for line in clean_lines]

length_numebers = np.array(length_numebers).astype(int) 
list_numbers = [2, 3, 4, 7]
sum_dig = 0 

for number in list_numbers:

    sum_dig += np.sum(length_numebers == number)

# Sol 1

decoders = [line[:-1].split(' | ')[0].split(' ') for line in lines]

n_lines = len(decoders)

def getDecoder(decoder_strings):
    decoder_sets = [set(decoder) for decoder in decoder_strings]
    decoders_done = {}
    while len(decoder_sets) > 0:
        #print(decoder_sets)
        remaining_decoders = decoder_sets
        for decoder in remaining_decoders:
            if len(decoder) == 2: 
                decoders_done[1] = decoder
                decoder_sets.remove(decoder)
            if len(decoder) == 3: 
                decoders_done[7] = decoder
                decoder_sets.remove(decoder)
            if len(decoder) == 4: 
                decoders_done[4] = decoder
                decoder_sets.remove(decoder)
            if len(decoder) == 7: 
                decoders_done[8] = decoder
                decoder_sets.remove(decoder)
            try: 
                if len(decoder) == 5:
                    if decoders_done[1].issubset(decoder):
                        decoders_done[3] = decoder
                        decoder_sets.remove(decoder)
                    elif (decoders_done[4] - decoders_done[1]).issubset(decoder):
                        decoders_done[5] =decoder
                        decoder_sets.remove(decoder)
                    else:
                        decoders_done[2] =decoder
                        decoder_sets.remove(decoder)
                if len(decoder) == 6:
                    if decoders_done[4].issubset(decoder):
                        decoders_done[9] = decoder
                        decoder_sets.remove(decoder)
                    elif (decoders_done[4] - decoders_done[1]).issubset(decoder):
                        decoders_done[6] =decoder
                        decoder_sets.remove(decoder)
                    else:
                        decoders_done[0] =decoder
                        decoder_sets.remove(decoder)
            except: 
                pass 
    return decoders_done

def useDecoder(decoder, clean_line):
    number_string = ''
    for number in clean_line:
        set_number = set(number)
        for key in decoder: 
            if decoder[key] == set_number: 
                number_string += str(key)
    return int(number_string)  



a = getDecoder(decoder_strings = decoders[1])
useDecoder(a, clean_lines[1])

sum_2 = 0 
for i in range(n_lines):
    decoder = getDecoder(decoders[i])
    numbers = useDecoder(decoder, clean_lines[i])
    sum_2 += numbers


