text = input('Enter the text to check: ')

if text == '':
    print("It's not a palindrome")

text = text.replace(' ', '').lower()

if text == text[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
