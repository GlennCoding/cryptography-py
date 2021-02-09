import string
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def relocate_alphabet(message, key):
    encrypted = ''
    # keeps lower/uppercase and special characters
    for c in message:
        if c in alphabet_lower:
            # alphabet relocation
            encrypted += alphabet_lower[(alphabet_lower.index(c) + key) %
                                        len(alphabet_lower)]
        elif c in alphabet_upper:
            encrypted += alphabet_upper[(alphabet_upper.index(c) + key) %
                                        len(alphabet_upper)]
        else:
            encrypted += c
    return encrypted


def string_to_num(keyword):
    key_int = []
    for key_letter in keyword:
        if key_letter in alphabet_upper or key_letter in alphabet_lower:
            key_letter = key_letter.lower()
            key_int.append(alphabet_lower.index(key_letter))
        else:
            key_int = []
            break
    return key_int


def vigenere_cipher():
    message = input('Enter your message: ')
    # loop until keyword is valid
    while True:
        keyword = input('Enter the keyword: ')
        key_int = string_to_num(keyword)
        if key_int != []:
            break
        else:
            print('Error! Your keyword isn\'t valid.')

    # encrypt message
    encrypted = ""
    x = 0
    for c in message:
        if c in alphabet_lower or c in alphabet_upper:
            key = key_int[x % len(key_int)]  # rotates key trough keyword
            x += 1
        encrypted += relocate_alphabet(c, key)
    print('Here is your encrypted message: {}'.format(encrypted))


def caesar_cipher():
    message = input('Enter your message: ')
    # loop until key is valid
    while True:
        key = input('Enter the key: ')
        try:
            key = int(key)
            break
        except:
            if len(key) == 1:
                key = string_to_num(key)
                if key != []:
                    key = key[0]
                    break
                else:
                    print('Error! Your key isn\'t valid.')
            else:
                print('Error! Your key isn\'t valid.')

    encrypted = relocate_alphabet(message, key)
    print('Here is your encrypted message: {}'.format(encrypted))
