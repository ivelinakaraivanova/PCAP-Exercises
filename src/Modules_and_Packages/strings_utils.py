import string_utils

def halve_strings(string_list):
    result_list = []
    for in_string in string_list:
        result_list.append(string_utils.halve_string(in_string))
    return result_list

print(halve_strings(['Mark', 'Lydia']))