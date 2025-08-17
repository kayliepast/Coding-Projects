"""
Write a fantasy exploration game with the help of GPT 
"""
# import anything that is needed for this program
from openai import OpenAI
client = OpenAI()

from random import randint

from random import choice


# Define the three different mini games
def dice_and_wheel_game():
    print("Welcome to the dice and wheel game")

    # establish the die rolls and the wheel spin values
    die_1 = randint(1, 6)
    die_2 = randint(1,6)
    die_total = die_1 + die_2
    wheel_spin = randint(1,12)

    #print the context for the users 
    print('The purple creatures enjoy this game, it shows if you have telepathic powers similar to their own')
    print('They have spun a wheel ranging from 1 to 12 and rolled 2 classic die for you.')
    print('Do you think the dice or the spin will be higher?:')
    print('1. The dice will be higher')
    print('2. The spin will be highter')
    user_choice = int(input('Select your bet: '))
    
    #Error message
    if user_choice != 1 and user_choice != 2:
        print('ERROR: Please select 1 or 2. They have sent you back for disobeying them')
        quit()
    else:
        print()
    
    # print totals
    print(f'The dice are {die_1} and {die_2}. The sum is {die_total}.')
    print(f'The wheel spun to {wheel_spin}.')

    # conditionals to determine if the user won
    if die_total > wheel_spin and user_choice == 1:
        print('The die total is higher.')
        print('You won!')
    elif die_total < wheel_spin and user_choice == 2:
        print('The wheel spin is higher.')
        print('You won!')
    elif die_total > wheel_spin and user_choice == 2:
        print('The die total is higher.')
        print('You lost!')
    elif die_total < wheel_spin and user_choice == 1:
        print('The wheel spin is higher.')
        print('You lose!')
    else:
        print('The die total and the wheel spin are equal.')
        print('Draw.')

    #goodbye message
    print('They have sent you back to where your were in your adventure')


def telepathy_game():
    TARGET = 5
    
    #welcome message
    print('Welcome to the mind game! the purple creatures are telepathic, and want to see if you are too')
    user_guess = int(input('Guess a number from 1 to 5:'))

    # conditionals to determine if the user won
    if user_guess > TARGET:
        print('Too high... maybe they will call upon you once more... or not')
    elif user_guess < TARGET:
        print('Too low... maybe they will call upon you once more... or not')
    elif user_guess != 1 and user_guess != 2 and user_guess != 3 and user_guess !=4 and user_guess !=5:
        print('ERROR: Please select 1,2,3,4, or 5. They have sent you back for disobeying instruction')
        quit()
    else:
        print('Correct! You are just like one of them')
    
    # goodbye message 
    print('They have sent you back to where your were in your adventure')


def hand_game():

    #welcome message and instructions
    print('Welcome to the hand game!')
    print('There are a mystery amount of gems to take from, ranging from 1-100')
    print('These gems are tiny, so you will be taking some gems with each hand')
    print('Whichever hand you take the final gem with, you get to keep what you are holding')
    print('Your left hand is hand number 1 and your right hand is hand number 2!')
    gems = randint (1,100)
    hand = 1

    looping = True
    while looping:
        print()
        print(f'It is hand {hand}\'s turn.')

        # Use a while loop to force the user to give valid input
        getting_input = True
        while getting_input:

            try:
                remove = int(input('Take 1, 2, or 3 stones: '))

                #if the user inputs anything other than 1,2, or 3, an error message will appear
                if remove < 1 or remove > 3 or remove > stones:
                    print('That is not a valid choice.')
                else:
                    getting_input = False
            except ValueError:
                print('Enter 1, 2 or 3.')

        # Reduce the number of gems
        stones -= remove

        # The hand who takes the last stone wins 
        if stones == 0:
            print(f'Hand {hand} wins!')
            looping = False
        else:
            # Switch to the other hand
            hand = (hand % 2) + 1
    # goodbye message
    print('They have sent you back to where your were in your adventure')

# Randomly choose a mini-game
def play_random_mini_game():
    mini_games = [dice_and_wheel_game, telepathy_game, hand_game]
    choice(mini_games)()


def chat_request(user_messages, nararrator_messages):
    """
    Chat interaction using both user and narrarator histories to continue the gamer history 
    """

    # Starting messages list with system prompt
    messages = [{"role": "system", "content": "You are guiding the user through a storytelling based game. This is the inital prompt and story: You open your eyes to see a cave full of pink and purple crytals  It is cold and dry, you hear chatter in the distance You begin walking and fall down into a bright room with florescent lights and club music playing There are small, purple creatures surronding you, they are telepathic, you don\'t know where you are, but you have a few options 1. Talk to the purple person beside you 2. Try and find an exit 3. Dance!'You will give the user 2-5 lines of scene setting for each new area they explore. You will give them 3-5 new options to explore from each time they interact with you. If the user does not pick one of the given choices, please repeat the storyline until they choose once of the proper options, only give options to continue in the numerical list"}]

    # nararator reponses
    for i in range(len(nararrator_messages)):
        messages.append({"role": "user", "content": user_messages[i]})
        messages.append({"role": "assistant", "content": nararrator_messages[i]})

    # Append the most recent user message as the final element of the messages list
    messages.append({"role": "user", "content": user_messages[-1]})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return completion.choices[0].message.content


### MAIN
# give the player a starting scene 
print('Welcome!!!')
print('*if at any point you would like to stop your adventure please enter "quit".*')
print('You open your eyes to see a cave full of pink and purple crytals ')
print('It is cold and dry, you hear chatter in the distance')
print('You begin walking and fall down into a bright room with florescent lights and club music playing')
print('There are small, purple creatures surrounding you, you don\'t know where you are, but you have a few options')
print('1. Talk to the purple person beside you')
print('2. Try and find an exit')
print('3. Dance!' )

# prompt the player to enter the action they want to take 
print("Which option do you want to choose?")

user_history = []
nararrator_history = []

# GPT response and continuation of the story
while True:
    user_input = input('\nYou:\n\n\t')
    if user_input.lower() == 'quit':
        break

    user_history.append(user_input)
    response = chat_request(user_history, nararrator_history)
    print('\nNarrator:\n\t', response)
    nararrator_history.append(response)

    # min-game add in 

    # Random chance of a mini-game
    if randint(1, 5) == 1:  # 1 in 5 chance to trigger a mini-game
        print("\nYou have been called upon by the purple creatures to complete a mini game!\n")
        mini_game_result = play_random_mini_game() 
        #mini game will be played 

        # Add mini-game result to user history for the AI model
        user_history.append(f"Mini-game result: {mini_game_result}")

        # Wait for the user to allow the story to go on 
        input("Press Enter and enter one of the previous options from the last narration to continue your adventure...")
