text = input("Enter your message: ")
shift_value = input('Enter shift_value (an integer number from the range 1..25): ')

cipher = ''

if not shift_value.isdigit():
    print("You have entered invalid charcters")
elif int(shift_value) < 1 or int(shift_value) > 25:
    print("Shift value entered is out of range")
else:
   
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            cipher += chr((ord(char) + int(shift_value) - 65) % 26 + 65)

        elif char.islower():
            cipher += chr((ord(char) + int(shift_value) - 97) % 26 + 97)

        else:
            cipher += char
    

print(cipher)