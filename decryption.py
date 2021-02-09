import collections
import encryption
from encryption import alphabet_upper, alphabet_lower


def get_key_caesar(c):
    c_pos = alphabet_lower.index(c.lower())
    key = 0
    if c_pos < alphabet_lower.index('e'):
        key = alphabet_lower.index('e') - c_pos
    if c_pos > alphabet_lower.index('e'):
        key = (alphabet_lower.index('e') - c_pos) + len(alphabet_lower)
    return key


def caesar_decrypt():
    message = input('Enter your encrypted message: ')
    chars = [c for c in message if c in alphabet_lower or c in alphabet_upper]
    most_common_chars = collections.Counter(chars).most_common(2)

    if (most_common_chars[0][1] / len(message) - most_common_chars[1][1] / len(message)) > 0.03:
        decrypted = encryption.relocate_alphabet(
            message, get_key_caesar(most_common_chars[0][0]))
        print('Here is your decrypted message: {}'.format(decrypted))
    else:
        print('The hack is not working. (A reason for that could be that the exncrypted text is just too short to decrypt.)')

        # Add function to manually enter key
        #
        #

        main.check_input('y', 'n', 'Do you want to enter the key manually?(Y/n)'')

def vigenere_decrypt():
    message = input('Enter the encrypted message: ')
    # loop until keyword is valid
    while True:
        keyword = input('Enter the keyword: ')
        key_int = encryption.string_to_num(keyword)
        if key_int != []:
            break
        else:
            print('Error! Your keyword isn\'t valid.')

    # reverts the key
    for n, i in enumerate(key_int):
        key_int[n] = len(alphabet_lower) - i

    # decrypted message
    decrypted = ""
    x = 0
    for c in message:
        if c in alphabet_lower or c in alphabet_upper:
            key = key_int[x % len(key_int)] % 26 # rotates key trough keyword
            x += 1
        decrypted += encryption.relocate_alphabet(c, key) # work here
    print('Here is your decrypted message: {}'.format(decrypted))
