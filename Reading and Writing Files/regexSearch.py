# TODO: Open all txt files in folder 
# TODO: Read contents to variable
# TODO: Search for regex expression
# TODO: User input to supply expression
# TODO: Print results to screen

import re
import os

cwd = os.getcwd()
files = []

for file in os.listdir(cwd):
    if file.endswith(".txt"):
        files.append(file)

print("Enter regex pattern to match:")
user_input = input()
user_regex = re.compile(user_input)

found = 0

for file in files:
    with open(file, encoding='utf-8') as f:
        text = f.read()
        result = user_regex.search(text)
        if result == None:
            break
        elif result.group() == user_input:
            print("Found matching content at file: " + (os.path.abspath(file)))
            found += 1
            break

if found == 0:
    print("Content not found.")