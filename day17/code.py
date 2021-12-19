import numpy as np 

x_range = [111, 161]
y_range = [-154, -101]


# Solve this equation
#(x + 1)*x/2 = 161
161*2

x = 15
(x + 1)*x/2

x_steps_to_ys = {}
for x in range(18):
    ys = []
    for y in range(-100,200):
        extra = 0
        keep_falling = True
        falling_distance = 0
        while keep_falling: 

            extra += 1
            steps = x + extra

            previous_distance = falling_distance
            falling_distance = (2*y-(steps-1))*steps/2
            keep_falling = falling_distance >= -154

        if (previous_distance <= -101):
            ys.append(y)
    
    x_steps_to_ys[x] = ys

to_zero_sum = len(x_steps_to_ys[15] + [-7, -6, -5, -4, -3]) + len(x_steps_to_ys[16] + [-9, -8, -7, -6, -5, -4, -3, -2] ) + len(x_steps_to_ys[17] + [-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])

#x = 17
#steps_back = 8
#(x + 1)*x/2 - np.sum(range(steps_back+1))
#x-steps_back
#111

exact_x_num = {}

for x in range(0,18):
    exact_x_num[x] = set()
    for y in range(-154, 10):
        falling_distance = (2*y-(x-1))*x/2
        if (falling_distance >= -154) and (falling_distance <= -101):
            exact_x_num[x].add(y)

sum_exact = 0
len()
for x in range(18, 162):
    possible_y = set()
    for steps in range(1,18):

        distance_x = np.sum(x - np.array(range(steps)))

        if (distance_x >= 111) and (distance_x <= 161):
            
            possible_y = set.union(exact_x_num[steps], possible_y)
    sum_exact += len(possible_y)

    

sum_exact + to_zero_sum

def will_land_in_area(x, y):
    x_distance = 0
    y_distance = 0
    x_speed = x
    y_speed = y
    lost = False 
    in_square = False
    while not lost:
        x_distance += x_speed
        y_distance += y_speed 
        x_speed = max(0, x_speed -1)
        y_speed = y_speed
        lost = (x_distance > x_range[1]) or (y_distance > y_range[1])
        if lost: 
            break
        if (x_distance >= x_range[0]) and (y_distance >= y_range[0]):
            in_square = True
            lost = True
    return in_square




total_trajectories = 0
for x in range(10, 163): 
    for y in range(-200, 200): 
        if will_land_in_area(x, y):
            total_trajectories += 1

