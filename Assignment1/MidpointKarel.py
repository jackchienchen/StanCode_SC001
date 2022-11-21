"""
File: MidpointKarel.py
Name: Jack Chen
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    The Project aims to find the mid point for Karel.
    """
    if not front_is_clear():  # 1x1 world
        put_beeper()
    else:
        put_beeper()
        first_move()  # Get to second row
        while front_is_clear():
            move()
            if front_is_clear():  # 第二行走兩步，第一行走一步
                move()
                put_beeper()
                install_first_row_beeper()
                pick_beeper()
        turn_right()
        move()
        turn_right()
        while not on_beeper():
            move()


def install_first_row_beeper():
    turn_right()
    move()
    turn_right()
    while not on_beeper():  # 走到最近的第一行Beeper上
        move()
    turn_around()
    move()
    put_beeper()  # 到放下一行第一個Beeper
    turn_left()
    move()
    turn_right()
    while not on_beeper():  # 到第二行Beeper上
        move()


def first_move():
    turn_left()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)