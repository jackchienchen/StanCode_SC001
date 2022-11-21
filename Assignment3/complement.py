"""
File: complement.py
Name: Jack Chen
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    you can input dna strand ATCG randomly, and the function will
    process the safest complement of the strand.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    # case-insensitive
    dna = dna.upper()
    compliment = build_compliment(dna)
    print('The compliment of ' + str(dna) + ' is ' + str(compliment) + '.')


def build_compliment(dna):
    """
    :param dna: input str (A,T,C,G only)
    nuc: the compliment of the input
    To find the dna's compliment we need to manipulate str
    than loop the compliment of the input character.
    :return ans: will be the compliment of the input.
    """
    ans = ''
    for nuc in dna:
        if nuc == 'C':
            ans += 'G'
        elif nuc == 'G':
            ans += 'C'
        elif nuc == 'T':
            ans += 'A'
        elif nuc == 'A':
            ans += 'T'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == '__main__':
    main()
