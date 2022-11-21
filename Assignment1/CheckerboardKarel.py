"""
File: CheckerboardKarel.py
Name: Jack Chen
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    build_odd()
    while left_is_clear():
        if on_beeper():
            move_to_next()
            move()
            build_odd()
        else:
            move_to_next()
            build_odd()


def move_to_next():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()


def build_odd():
    if not front_is_clear:
        put_beeper()
    else:
        while front_is_clear():
            put_beeper()
            move()
            if front_is_clear():
                move()
        check_obob()


def back():
    while front_is_clear():
        move()
    turn_left()
    turn_left()


def check_obob():
    turn_left()
    turn_left()
    move()
    if on_beeper():
        back()
    else:
        turn_left()
        turn_left()
        move()
        put_beeper()
        turn_left()
        turn_left()
        back()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)