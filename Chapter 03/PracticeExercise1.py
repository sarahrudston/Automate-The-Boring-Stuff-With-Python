# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1. Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. 

def collatz(number):
    try:
        if number % 2 == 0:
            even = number // 2
            print(even)
            return even
        elif number % 2 == 1:
            odd = 3 * number + 1
            print(odd)
            return odd
    except ValueError:
        print('Please enter an integer.')

answer = input('Please enter a number: ')

while answer != 1:
    answer = collatz(int(answer))



