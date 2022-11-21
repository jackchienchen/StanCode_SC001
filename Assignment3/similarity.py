"""
File: similarity.py
Name: Jack Chen
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    long_sequence: the input str of an DNA sequence(only includes A,T,C,G)
    short_sequence: the input str that match each of the sub sequences of the long sequence.
    The function will find the best sub sequence in the long sequence to match the short sequence.
    The best match will be define as the number of alphabet on the same spot on the sequemce.
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match? ')
    # case-insensitive both sequences
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    best_match = match_process(long_sequence, short_sequence)
    print('The best match is ' + str(best_match))


def match_process(long, short):
    highest_score = 0
    score = 0
    best_match = ''
    for i in range(len(long)-len(short)+1):
        for j in range(len(short)):
            if long[i+j] == short[j]:
                score += 1
        if score > highest_score:
            highest_score = score
            best_match = long[i: i+len(short)]
        score = 0
    return best_match


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == '__main__':
    main()
