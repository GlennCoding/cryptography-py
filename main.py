import encryption
import decryption

def check_input(a, b, message):
    while True:
        user_input = input(message)
        if user_input == a or user_input == b:
            return user_input
        elif user_input == 'back':
            break
        else:
            print('Please only enter the desired characters.')

def run():
    # Navigation Menu
    ask_purpose = check_input('e', 'd', 'Type \'e\' to encrypt and \'d\' to decrypt: ')
    if ask_purpose == 'e':
        ask_method = check_input('c', 'v', 'Type \'c\' for caesar encyption and \'v\' for vigenere encyption: ')
        if ask_method == 'c':
            encryption.caesar_cipher()
        else:
            encryption.vigenere_cipher()
    else:
        ask_method = check_input('c', 'v', 'Type \'c\' for caesar decryption and \'v\' for vigenere decryption: ')
        if ask_method == 'c':
            decryption.caesar_decrypt()
        else:
            decryption.vigenere_decrypt()



if __name__ == '__main__':
    end_program = False
    while not end_program:
        run()

        continue_program = '-'
        while continue_program != 'y' and continue_program != 'n' \
                and continue_program != '':
            continue_program = input('Do you want start over again?(Y/n)')

        if continue_program == 'n':
            end_program = True
