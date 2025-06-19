# Start with an existing list value. Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with 'and' inserted before the last item.

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_function(food):
   output = ''
   for i in range(len(food)):
      if i == len(food) - 1:
         output += 'and ' + food[i]
      else:
         output += food[i] + ', '
   return output

result = comma_function(spam)
print(result)