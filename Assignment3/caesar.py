"""
File: caesar.py
Name: Jack Chen
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    move_right: int, the ALPHABET will be wrap to the right by this input.
    un_ciphered: srt, this is the string after ciphered.
    ciphered: str, this is the string before ciphered.
    This function decipher the string depending on the steps the
    ALPHABET move right.
    """
    move_right = int(input('Secret Number: '))
    ciphered = input("What's the ciphered string? ")
    ciphered = ciphered.upper()
    un_ciphered = decipher_alphabet_process(ciphered, move_right)
    print('The deciphered string is: ' + str(un_ciphered))


def decipher_alphabet_process(n, move):
    """
    :param n: str, the string after cipher.
    :param move: int, the steps the ALPHABET moves right
    :return: the deciphered string
    This function deciphers the un_ciphered string.
    """
    ans = ''
    for alpha in n:
        if alpha in ALPHABET:
            index = ALPHABET.find(alpha)
            if index >= 26-move:
                ans += ALPHABET[index+move-26]
            else:
                ans += ALPHABET[index+move]
        else:
            ans += alpha
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####

if __name__ == '__main__':
    main()
