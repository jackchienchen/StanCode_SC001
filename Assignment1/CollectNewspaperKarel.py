"""
File: CollectNewspaperKarel.py
Name: Jack Chen
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    # Comments
    pre-condition: Karel should be at the north-west side of his house.
    post-condition: Karel should be at the same place as pre-condition, however with the newspaper in his hand.
    """
    get_news()  # Functions
    back_home()


def get_news():
    """
    pre-condition: Karel should be at the north-west side of his house.
    post-condition: Karel should pick up the news at (3,6) facing east.
    """
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()
    pick_beeper()


def turn_right():
    """
    this function makes Karel turn left 3 times.
    """
    for i in range(3):
        turn_left()


def back_home():
    """
    pre-condition: Karel should be at (3,6) facing east.
    post-condition: Karel should be at the upper left of his house facing east.
    """
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_around():
    """
    this function makes Karel turns left 2 times.
    """
    turn_left()
    turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
