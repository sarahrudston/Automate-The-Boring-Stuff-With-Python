spam = ['apples', 'bananas', 'tofu', 'cats']
empty_list = []
pizza = ['pineapple', 'cheese', 'jalapeno peppers', 'tomatoes']

def shopping(items):
    if items:
        for index, item in enumerate(items):
            if index != len(items) -1:
                item = item + ','
                print(item, end=' ')
            elif index == len(items) - 1:
                item = 'and ' + item
                print(item)
    elif not items:
        print('List is empty')

shopping(pizza)