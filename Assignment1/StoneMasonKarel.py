from karel.stanfordkarel import *
"""
File: StoneMasonKarel.py
Name: Jack Chen
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    pre-condition: Karel is at (1,1) preparing to build pillars.
    post-condition: Karel will finish building various pillars
                    and end up facing east at bottom right of the world.
    """
    while front_is_clear():
        repair_pillar()
        go_back()
        move_forward()
    repair_pillar()  # Prevent OBOB
    go_back()


def repair_pillar():
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        put_beeper()


def go_back():
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    turn_left()


def move_forward():
    for i in range(4):
        move()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)