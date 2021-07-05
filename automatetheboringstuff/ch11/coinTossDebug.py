# Practice Project
# Solved by SeungWon Bae

import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()

# toss = random.randint(0, 1) # 0 is tails, 1 is heads  ## Original Bug
# toss = random.randint(0, 1) == 0 ? 'tails' : 'heads'  # Not working in Python
toss = 'tails' if random.randint(0, 1) == 0 else 'heads' # 0 is tails, 1 is heads

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # guesss = input()  ## Original Bug
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')