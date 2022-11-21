"""
File: hangman.py
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

# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    answer: The word picked from the function random_word.
    dash: The function that counts the number of words answer have, and turns it into '-'.
    lives: The lives that the man have.(the errors that you can make)
    The main function uses while loop to display the game of hangman.
    The game randomly selected one word that you should guess.
    Every guess that is not in the word cross out one of your lives.
    """
    ans = random_word()  # the correct word
    dashes_old = len(ans) * '-'
    dashes_new = dashes_old
    lives = N_TURNS
    print('The word looks like ' + dashes_old)
    print('You have ' + str(lives) + ' wrong guesses left.')
    while lives > 0 and dashes_new != ans:
        guess = input('Your guess: ')
        guess = guess.upper()
        if guess.isalpha() and len(guess) == 1:  # limit illegal format
            index = ans.find(guess)
            if index == -1:  # Guess wrong
                lives -= 1
                print('There is no ' + guess + "'s in the word.")
                print('The word looks like ' + dashes_new)
                print('You have ' + str(lives) + ' wrong guesses left.')
            else:
                print('You are correct!')
                dashes_old = ''
                for i in range(len(ans)):
                    if guess == ans[i]:
                        dashes_old += guess
                    else:
                        dashes_old += dashes_new[i]
                dashes_new = dashes_old
                print('The word looks like ' + dashes_new)
                print('You have ' + str(lives) + ' wrong guesses left.')
        else:
            print('Illegal format.')
    if lives == 0:
        print('You are completely hung : (')
        print('The word was: ' + ans)
    if dashes_new == ans:
        print('You are correct!')
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


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
