text1 = input('Enter the first text: ')
text2 = input('Enter the second text: ')

if text1 == '' and text2 == '':
    print('Not anagrams')

text1 = text1.replace(' ', '').lower()
text2 = text2.replace(' ', '').lower()

if sorted(text1) == sorted(text2):
    print('Anagrams')
else:
    print('Not anagrams')

# list1 = [text1[i] for i in range(len(text1))]

# list2 = [text2[i] for i in range(len(text2))]

# if list1.sort() == list2.sort():
#     print('Anagrams')
# else:
#     print('Not anagrams')
