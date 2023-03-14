# print('How\tmany strings\nwill you see?'.split())
# # ['How', 'many', 'strings', 'will', 'you', 'see?']

'''
def get_longest_word(input_string):
    words = input_string.replace('.', ' ').replace(',', ' ').split()
    temp_max_word = ''
 
    for word in words:
      if len(word) > len(temp_max_word):
        temp_max_word = word
    
    return temp_max_word
'''

def get_longest_word(input_string):
    # separators = [' ', ',', '\n', '.']
    result_list = input_string.replace(',', ' ').replace('.', ' ').replace('\n', ' ').split()
    result_word = sorted(result_list, key=lambda x: len(x), reverse=True)[0]
    return result_word

print(get_longest_word('i\'m a worker, are you.\n newworker incorrect too'))