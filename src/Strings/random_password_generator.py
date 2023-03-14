import random


letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
specials = '!@#$%^&*()_+|'


def make_upper(input_char):
    is_upper = random.randint(0,1)
    if is_upper:
        input_char = input_char.upper()
    return input_char


def get_input_chars(has_digits, has_specials):
    
    input_string = letters
    if has_digits:
        input_string += digits
    if has_specials:
        input_string += specials
   
    return input_string


def generate_pass(pass_length=10, has_uppers=False, has_digits=False, has_specials=False):
   
    pass_word = ''
    chars_for_choice = get_input_chars(has_digits, has_specials)

    for i in range(pass_length):
        ch = random.choice(chars_for_choice)
        if has_uppers and ch.isalpha():
            ch = make_upper(ch)

        pass_word += ch

    return pass_word


def main_menu():
    while True:
        print('\n-- Password generator --')
        print('Choose option:')
        print('1: generate password')
        print('2: exit the program')
        choice = input('Your choice: ')

        if choice == '1':
            pass_menu()

        elif choice == '2':
            print('Bye!')
            break

        else:
            print('Please enter a correct value')


def pass_menu():
    pass_length = int(input('Provide password length: '))
    has_uppers = input('Use uppercase letters? (y/n): ').lower().strip() == 'y'
    has_digits = input('Use digits? (y/n): ').lower().strip() == 'y'
    has_specials = input('Use special characters? (y/n):').lower().strip() == 'y'
    print('\nGenerated password:', generate_pass(pass_length, has_uppers, has_digits, has_specials))


main_menu()
