#Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam

spam = 1

if spam == 1:
    #print('Hello')
    for num in range(10):
        print(num)
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')