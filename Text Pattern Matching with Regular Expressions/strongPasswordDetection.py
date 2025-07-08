import re

length_regex = re.compile('.{8,}')
lower_case_regex = re.compile('[a-z]+')
upper_case_regex = re.compile('[A-Z]+')
digit_regex = re.compile('[\\d]+')

def strong_password(password):
    if length_regex.search(password) == None:
        print('Password must be at least 8 characters long.')
        return False
    if lower_case_regex.search(password) == None:
        print('Password must have lower case letters.')
        return False
    if upper_case_regex.search(password) == None:
        print('Password must have upper case letters.')
        return False
    if digit_regex.search(password) == None:
        print('Password must have at least one digit.')
        return False
    else:
        print('Password is valid.')

pw = input('Please type a password:\n')
strong_password(pw)