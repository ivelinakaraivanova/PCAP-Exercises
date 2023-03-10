
def halve_string(input_string):
    first_half = ''
    second_half = ''
    if len(input_string) % 2 == 0:
        first_half, second_half = input_string[:len(input_string)//2], input_string[len(input_string)//2:]
    else:
        first_half, second_half = input_string[:len(input_string)//2 + 1], input_string[len(input_string)//2 + 1:]
    return (first_half, second_half)


# print(halve_string('Mark'))
# print(halve_string('Lydia'))


# input_string = input()
# first_half, second_half = input_string[:len(input_string)//2+1], input_string[len(input_string)//2+1:]
# print(first_half)
# print(second_half)