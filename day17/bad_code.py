import numpy as np 

x_range = [111, 161]
y_range = [-154, -101]


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
        y_speed = y_speed - 1
        lost = (x_distance > x_range[1]) or (y_distance < y_range[0])
        if lost: 
            break
        if (x_distance >= x_range[0]) and (y_distance <= y_range[1]):
            in_square = True
            lost = True
    return in_square




total_trajectories = 0
for x in range(10, 163): 
    for y in range(-200, 200): 
        if will_land_in_area(x, y):
            total_trajectories += 1

