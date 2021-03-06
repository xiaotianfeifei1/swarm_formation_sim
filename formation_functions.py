# common functions for the formation simulations

import math
import time

# reset radian angle to [-pi, pi)
def reset_radian(radian):
    while radian >= math.pi:
        radian = radian - 2*math.pi
    while radian < -math.pi:
        radian = radian + 2*math.pi
    return radian

# convert positions in physics coordinates to display coordinates
def world_to_display(input_pos, world_size, display_size):
    pos_display = [0, 0]
    pos_display[0] = int(input_pos[0]/world_size[0] * display_size[0])
    pos_display[1] = int((1-input_pos[1]/world_size[1]) * display_size[1])
    return pos_display

# return date and time in a string, connected with dash, for filename
def get_date_time():
    return (time.strftime('%Y') + '-' +
            time.strftime('%m') + '-' +
            time.strftime('%d') + '-' +
            time.strftime('%H') + '-' +
            time.strftime('%M') + '-' +
            time.strftime('%S'))


