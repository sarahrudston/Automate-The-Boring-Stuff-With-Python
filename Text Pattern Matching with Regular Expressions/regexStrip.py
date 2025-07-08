import re

def regexStrip(text, char='\\s'):
    if text == '':
        print('No text entered.')
        return False
    if text != '':
        result = re.sub(f'^{char}+', '', text)
        result = re.sub(f'{char}+$', '', result)
        print(result)

test = input('Please enter some text:')
remove = input('Please enter the character to remove from the start and end of the text:')
regexStrip(test, remove)