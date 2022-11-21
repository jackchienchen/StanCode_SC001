"""
File: hangman.py
Name: Jack
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random

LIVES = 7


def main():
    ans = random_word()
    dashes = len(ans) * '-'
    dash_tool = len(ans) * '-'
    lives = LIVES  # 7
    print('Your word looks like: ' + dashes)
    print('You have ' + str(lives) + ' guesses left.')

    while "-" in dashes and lives > 0:
        guess = input('Your guess: ')
        guess = guess.upper()
        if guess.isalpha() and len(guess) == 1:  # To avoid illegal format
            if guess in ans:  # Got the correct word
                dashes = ''
                print('You are correct!')
                for i in range(len(ans)):
                    if ans[i] == guess:
                        dashes += guess
                    else:
                        dashes += dash_tool[i]
                print('The word looks like: ' + dashes)
                dash_tool = dashes
            else:
                print('There is no ' + guess.upper() + "'s in the word.")
                lives -= 1
            print('You have ' + str(lives) + ' lives left.')
        else:
            print('illegal format.')

    if lives == 0:  # LOSE!!!
        print('You are completely hung : (')

    if '-' not in dashes:  # WIN!!!
        print('You win!')
        print('The word was: ' + ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()





