"""
form a program that will compose random love letters
"""

#import randint

from random import randint

# Construct the salutation

# Choose an adjective
r = randint(1, 3)
if r == 1:
  opening_adj = 'Darling'
elif r == 2:
  opening_adj = 'Unrepaceable'
else:
  opening_adj = 'Stunning'

# Choose a noun
r = randint(1, 2)
if r == 1:
  opening_noun = 'Peach'
else:
  opening_noun = 'Dream'


# Print Greeting
print(f'{opening_adj} {opening_noun},')
print()  # blank line 


### Construct the main body 

# Choose adverbs
r = randint (1,3)
if r == 1:
  adverb = 'enormously'
elif r == 2:
  adverb = 'incredibly'
else:
  adverb = 'absolutely'

r = randint(1,3)
if r == 1: 
  adj_2 = 'polite'
elif r == 2:
  adj_2 = 'happy'
else:
  adj_2 = 'calm'

r = randint(1,3)
if r == 1:
  adj_3 = 'fierce'
elif r == 2:
  adj_3 = 'jolly'
else:
  adj_3 = 'witty'


r = randint(1,3)
if r == 1:
  noun_2 = 'kindess'
elif r == 2:
  noun_2 = 'passion'
else:
  noun_2 = 'patience'

r = randint(1,3) 
if r == 1:
  verb_1 = 'radiates'
elif r == 2:
  verb_1 = 'shines'
else:
  verb_1 = 'beams'

r = randint(1,3)
if r == 1:
  location_1 = 'corridors'
elif r == 2: 
  location_1 = 'halls'
else:
  location_1 = 'streets'


r = randint(1,3)
if r == 1:
  verb_2 = 'dream'
elif r == 2:
  verb_2 = 'hope'
else:
  verb_2 = 'plan'

r = randint(1,3)
if r == 1:
  verb_3 = 'see' 
elif r == 2:
  verb_3 = 'view'
else:
  verb_3 = 'perceive'

r = randint(1,3)
if r == 1:
  time = 'once'
if r == 2:
  time = 'twice'
else:
  time = 'thrice'

# print the main body of text 

print(f'You are {adverb} {adj_2} and {adj_3}.')
print(f'Your {noun_2} {verb_1} through the {location_1}.')
print(f'I {verb_2} to {verb_3} you {time} more.')
print()


# constuct the final goodbye 

r = randint(1,3)
if r == 1:
  final = 'persistently'
elif r == 2:
  final = 'constantly'
else:
  final = 'endlessly'


r = randint(1,3)
if r == 1:
  name = 'byte'
elif r == 2:
  name = 'RAM'
else:
  name = 'pixel'

# print the final goodbye

print(f'Yours {final},')
print(f'                 {name}')