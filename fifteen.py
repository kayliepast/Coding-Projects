"""
Simulate the dice game 'Fifteen'
"""

# get random number generator
from random import randint

# Print welcome messages
print('Welcome to the Fifteen game!')
print('Rolling three dice rn...')

# Generate 3 random numbers for the 3 die
die_1 = randint(1,6)
die_2 = randint(1,6)
die_3 = randint(1,6)

# preform first calculation
total = die_1 + die_2 + die_3 

# print the dice values and sum 
print(f'The dice are {die_1}, {die_2}, and {die_3}.')
print(f'The sum is {total}')

# create if statement for first total
if total == 15:
    print('You win!')
    print('Thanks for playing!')
    quit()
elif total > 15:
    print('You lose :(')
    print('Thanks for playing! ')
    quit()
else:
    print('Would you like to roll again?')
    print('1. Yes!')
    print('2. No')

user_choice = int(input('Enter your choice:'))

# create if statement for the users choice 

if user_choice == 1:
    die_4 = randint(1,6)
    print(f'You rolled a {die_4}.')
elif user_choice == 2:
    print('You lose!')
    print('Thanks for playing!')
    quit()
else:
    print('You must enter 1 or 2')
    print('rerun to play again')
    quit()

# announce the players score and print the corresponding messages

total_2 = die_4 + die_3 + die_2 + die_1
print(f'Your total score is {total_2}')

if total_2 == 15:
    print('You win! Perfect score')
elif total_2 > 15:
    print('You lose! You went over 15')
else:
    print('You lose, you rolled too low')

print('Thank you for playing!')