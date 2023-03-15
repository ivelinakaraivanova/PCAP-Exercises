'''
Function that modifies all string properties of any object 
by turning them into empty strings
'''

def empty_strings(user_object):
    for prop_name in user_object.__dict__.keys():
        prop_value = getattr(user_object, prop_name)
        if isinstance(prop_value, str):
            setattr(user_object, prop_name, '')
