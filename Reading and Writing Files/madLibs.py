# TODO: Write the text file and save it.
# TODO: Read the file
# TODO: Find all instances of adjective, noun, adverb or verb
# TODO: Save to variables
# TODO: Prompt user to enter text for each
# TODO: Save to variables

import re

def set_text_variable(text):
    globals()[text] = text

with open('madlib.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')

with open('madlib.txt') as madlib:
    text = madlib.read()

check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

while True:
    result = check.search(text)
    if result == None:
        break
    elif result.group() == 'ADJECTIVE' or result.group == 'ADVERB':
        print('Enter an %s' % (result.group().lower()))
    elif result.group() == 'NOUN' or result.group() == 'VERB':
        print('Enter a %s:' % (result.group()))
    i = input()
    text = check.sub(i, text, 1)

print(text)
print('Name of file:')
name = input()

with open(f'{name}.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(text)



