import re
import os

cwd = os.getcwd()
files = []

for file in os.listdir(cwd):
    if file.endswith(".txt"):
        files.append(file)

print("Enter regex pattern to match:")
user_input = input()

try:
    user_regex = re.compile(user_input)
except re.error:
    print("Invalid regex pattern.")
    exit(1)

found = 0

for file in files:
    with open(file, encoding='utf-8') as f:
        text = f.read()
        result = user_regex.search(text)
        if result:
            print("Found matching content at file: " + (os.path.abspath(file)))
            print(result)
            found += 1

if found == 0:
    print("Content not found.")