import random
guess = ''
while guess not in ('heads', 'tails'): # Debugger shows first that guess = ''. Then I enter 'heads' so guess then = 'heads'
    print('Guess the coin toss! Enter heads or tails:')
    guess = input() # Debugger shows that guess = ''
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess: # Now toss = 1 and guess = 'heads'. In this code, they can't match so I'd have to fix that.
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input() # First, guess = 'heads' as that was my original choice. 
    if toss == guess: # Now, toss still = 1 but I've now guessed 'tails'. Still no match.
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')