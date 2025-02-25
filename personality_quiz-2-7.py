"""
Which Trolls village are you?
"""

# Declare variables for each outcome

pop_village_score = 0 
rock_city_score = 0 
vibe_city_score = 0 
techno_reef_score = 0 
symphonyville_score = 0 
lonsome_flats_score = 0 

# Print the first question and assign answers to the different villages

print('what is your favorite color?')
print('1. Pink') #pop
print('2. Orange') #lonsome 
print('3. Yellow') #symphony
print('4. Red') #rock
print('5. Blue') #techno
print('6. Purple')  #vibe city

choice = int(input('Enter your answer: '))

if choice == 1:
    pop_village_score += 1
elif choice == 2:
    lonsome_flats_score += 1
elif choice == 3:
    symphonyville_score += 1
elif choice == 4:
    rock_city_score += 1
elif choice == 5:
    techno_reef_score += 1
elif choice == 6:
    vibe_city_score += 1
else:
    print('That\'s not an option.')
    # Don't quit; continue without scoring a point

# Print the second question and assign answers to the different villages

print('What is your favorite genre of music?')
print('1. classic')
print('2. rock')
print('3. techno')
print('4. country')
print('5. pop')
print('6. funk')

choice = int(input('Enter your answer: '))

if choice == 5:
    pop_village_score += 1
elif choice == 4:
    lonsome_flats_score += 1
elif choice == 1:
    symphonyville_score += 1
elif choice == 2:
    rock_city_score += 1
elif choice == 3:
    techno_reef_score += 1
elif choice == 6:
    vibe_city_score += 1
else:
    print('That\'s not an option.')
    # Don't quit; continue without scoring a point

# Print the third question and assign answers to the different villages

print('If you could play any instrument, what would it be?')
print('1. an electric guitar') # rock
print('2. a harp') # classic
print('3. a piano') #pop
print('4. a synthesizer') #techno
print('5. the drums') # funk
print('6. a kazoo') #country

choice = int(input('Enter your answer: '))

if choice == 3:
    pop_village_score += 1
elif choice == 6:
    lonsome_flats_score += 1
elif choice == 2:
    symphonyville_score += 1
elif choice == 1:
    rock_city_score += 1
elif choice == 4:
    techno_reef_score += 1
elif choice == 5:
    vibe_city_score += 1
else:
    print('That\'s not an option.')
    # Don't quit; continue without scoring a point

# Print the fourth question and assign answers to the different villages

print('What design style is your favorite?')
print('1. Modern') # pop
print('2. Farmhouse') # country
print('3. Midcentury') # classic
print('4. Art Deco') # techno
print('5. Maximalist') # funk
print('6. Vintage') # rock

choice = int(input('Enter your answer: '))

if choice == 1:
    pop_village_score += 1
elif choice == 2:
    lonsome_flats_score += 1
elif choice == 3:
    symphonyville_score += 1
elif choice == 6:
    rock_city_score += 1
elif choice == 4:
    techno_reef_score += 1
elif choice == 5:
    vibe_city_score += 1
else:
    print('That\'s not an option.')
    # Don't quit; continue without scoring a point

# Print the fifth question and assign answers to the different villages

print('What is your dream vacation?')
print('1. A resort on the ocean') # classic
print('2. A national parks roadtrip') #country
print('3. A staycation') #funk
print('4. A Europe trip') # pop
print('5. Gambling in Las Vegas') # rock
print('6. Skiing in Aspen') # techno

choice = int(input('Enter your answer: '))

if choice == 4:
    pop_village_score += 1
elif choice == 2:
    lonsome_flats_score += 1
elif choice == 1:
    symphonyville_score += 1
elif choice == 5:
    rock_city_score += 1
elif choice == 6:
    techno_reef_score += 1
elif choice == 3:
    vibe_city_score += 1
else:
    print('That\'s not an option.')
    # Don't quit; continue without scoring a point

# Print the sixth question and assign answers to the different villages

print('What type of friend do you prefer?')
print('1. Best friends') # pop
print('2. Social friends') # techno
print('3. Work friends') # classic
print('4. Frenemies') # rock
print('5. Close friends') # funk
print('6. Family') # country

choice = int(input('Enter your answer: '))

if choice == 1:
    pop_village_score += 1
elif choice == 6:
    lonsome_flats_score += 1
elif choice == 3:
    symphonyville_score += 1
elif choice == 4:
    rock_city_score += 1
elif choice == 2:
    techno_reef_score += 1
elif choice == 5:
    vibe_city_score += 1
else:
    print('That\'s not an option.')
    # Don't quit; continue without scoring a point


# determine the max score
max_score = max(pop_village_score, lonsome_flats_score, symphonyville_score, rock_city_score, techno_reef_score, vibe_city_score)


# Relate the max score the users best fit village, if tie, the user gets both nations printed

if pop_village_score == max_score:
    print('You belong to the Pop Village!')
    
if lonsome_flats_score == max_score:
    print('You belong to the Lonsome Flats!')

if symphonyville_score == max_score:
    print('You belong to Syphonyville!')

if rock_city_score == max_score:
    print('You belong to Rock City!')

if techno_reef_score == max_score:
    print('You belong to the Techno Reef!')

if vibe_city_score == max_score:
    print('You belong to Vibe City!')

