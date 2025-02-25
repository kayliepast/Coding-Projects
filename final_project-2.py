"""
FINAL PROJECT
"""
# import useful tools
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Read the csv file into a dataframe
df = pd.read_csv('SEC_Season_Data.csv')

# create a menu for the users to choose from 
def user_menu():
    """
    Create a menu of choices for the user to choose from
    """
    print('1. View team statistics')
    print('2. View overall conference statistics')
    print('3. Graph team\'s overall record')
    print('0. Quit the program')

# define a list of teams with their index numbers
def team_names():
    """
    print out a list of all the football teams in the SEC
    """
    # establish team names that correspond to their index number
    team_name_list = ['0. Alabama', '1. Arkansas', '2. Auburn', '3. Florida', '4. Georgia', '5. Kentucky', '6. LSU', '7. Mississippi', '8. Missouri', '9. Oklahoma', '10. Ole Miss', '11. South Carolina', '12. Tennesee', '13. Texas A&M', '14. Texas', '15. Vanderbilt']

    # print the list of team names
    for i in team_name_list:
        print(i)

# define the index numbers for each specfifc statistic
def stats():
    """
    print out a list of all the football statistics in the data set
    """
    # establish statistics that correspond to their index number
    statistic_list = [ '1. Points Scored', '2. Points Allowed', '3. Conference Wins', '4. Conference Losses', '5. Overall wins', '6. Overall losses']
    
    #print the list of statistics
    for i in statistic_list:
        print(i)

# define viewing the teams statistics
def view_team_stats():
    """
    Let the user choose their football team and statistic, then print out the matching stat
    """
    # print out the users options
    team_names()

    # get user input
    while True:
        try:
            team_name = int(input('Please select one of the teams: '))
            if 0 <= team_name < 16:
                break
            else:
                print("Invalid team selection. Please choose a number between 0 and 15.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    

    # define names for the printed output
    if team_name == 0:
        print_name = 'University of Alabama'
    elif team_name == 1:
        print_name = 'University of Arkansas'
    elif team_name == 2:
        print_name = 'Auburn University'
    elif team_name == 3:
        print_name = 'University of Florida '
    elif team_name == 4:
        print_name = 'University of Georgia'
    elif team_name == 5:
        print_name = 'University of Kentucky'
    elif team_name == 6:
        print_name = 'Louisiana State University '
    elif team_name == 7:
        print_name = 'Mississippi State University'
    elif team_name == 8:
        print_name = 'University of Missouri'
    elif team_name == 9:
        print_name = 'University of Oklahoma'
    elif team_name == 10:
        print_name = 'University of Mississippi'
    elif team_name == 11:
        print_name = 'University of South Carolina'
    elif team_name == 12:
        print_name = 'University of Tennesee'
    elif team_name == 13:
        print_name = 'Texas A&M'
    elif team_name == 14:
        print_name = 'University of Texas'
    else:
        print_name = 'Vanderbilt University'


    # print out statistics for the user to see 
    stats()

    # get the user to choose the statistic they want to see
    while True:
        try:
            specific_stat = int(input('Please input the specific statistic you want to see: '))
            if 1 <= specific_stat <= 6:
                break
            else:
                print('Invalid statistic selection. Please choose a number between 1 and 6.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')
    
    # assign the users statistic choice to what will be printed out
    if specific_stat == 1:
        print_stat = 'Points Scored'
    elif specific_stat == 2:
        print_stat = 'Points Allowed'
    elif specific_stat == 3:
        print_stat = 'Conference Wins'
    elif specific_stat == 4:
        print_stat = 'Conference Losses'
    elif specific_stat == 5:
        print_stat = 'Overall Wins'
    else:
        print_stat = 'Overall Losses'

    # call to the users team and statistic choice
    specific_stat = df.iat[team_name, specific_stat]

    # print out the users team and statistic choice, and the corresponding statistic
    print(f' The {print_stat} for {print_name} is {specific_stat}')

# define viewing overall statistics
def overall_statistics():
    print(df)  

# define generating teams season records
def graph_overall_record(team_index):
    """
    Create a stacked bar graph showing conference and total wins/losses for a team by index.
    """
    # Make sure the user inputed a number between 0 and 15
    team_names()

    while True:
        try:
            team_index = int(input('Please choose a team to graph: '))
            if 0 <= team_index < len(df):
                break
            else:
                print(f'Error: Invalid team index. Please choose a team number between 0 and {len(df) - 1}')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    # Select the team by index
    team_data = df.iloc[team_index]
    team_name = team_data['Team']

    # Prepare data for plotting
    conf_wins = team_data['ConfWins']
    conf_losses = team_data['ConfLosses']
    total_wins = team_data['TotalWins']
    total_losses = team_data['TotalLosses']

    # Create figure and axis
    plt.figure(figsize=(10, 6))

    # Create stacked bars
    plt.bar(['Conference Wins', 'Conference Losses'], [conf_wins, conf_losses], label='Conference', color='#002D72')
    plt.bar(['Overall Wins', 'Overall Losses'], [total_wins, total_losses], label='Overall', color='#90D5FF')

    # Customize the plot
    plt.xlabel('Record Type')
    plt.ylabel('Number of Games')

    # Define name for title
    if team_index == 0:
        print_name = 'University of Alabama'
    elif team_index == 1:
        print_name = 'University of Arkansas'
    elif team_index == 2:
        print_name = 'Auburn University'
    elif team_index == 3:
        print_name = 'University of Florida'
    elif team_index == 4:
        print_name = 'University of Georgia'
    elif team_index == 5:
        print_name = 'University of Kentucky'
    elif team_index == 6:
        print_name = 'Louisiana State University'
    elif team_index == 7:
        print_name = 'Mississippi State University'
    elif team_index == 8:
        print_name = 'University of Missouri'
    elif team_index == 9:
        print_name = 'University of Oklahoma'
    elif team_index == 10:
        print_name = 'University of Mississippi'
    elif team_index == 11:
        print_name = 'University of South Carolina'
    elif team_index == 12:
        print_name = 'University of Tennessee'
    elif team_index == 13:
        print_name = 'Texas A&M'
    elif team_index == 14:
        print_name = 'University of Texas'
    else:
        print_name = 'Vanderbilt University'

    # Establish images title
    plt.title(f'{print_name} - Conference vs Total Record')

    plt.legend()

    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(f'{print_name} wins losses.jpg')

    # Print out the team's record
    print(f'{print_name} Record:')
    print(f'Conference Record: {conf_wins}-{conf_losses}')
    print(f'Total Record: {total_wins}-{total_losses}')
    print('Your selected teams graph has been saved as a jpg file')


# define the main function that will be called in the main block 


def main():
    while True:
        # Print out the menu
        print('Welcome to the SEC Football Analysis Program!')
        user_menu()
        try:
            user_choice = int(input('Please choose 0,1,2, or 3 from the menu:'))

            if user_choice == 0:
                print('You have quit the SEC Football Analysis program.')
                # Exit the program
                break  
            elif user_choice == 1:
                # Call to the stats program
                view_team_stats() 
            elif user_choice == 2:
                # Display the full dataset
                overall_statistics()  
            elif user_choice == 3:
                team_names()
                team_index = int(input('Please choose a team to graph: '))
                graph_overall_record(team_index)
            else:
                print('Please choose an option from the menu.')
        except ValueError:
            print("Invalid input. Please enter a valid number between 0 and 3.")

### MAIN

# run all of the code in this program properly
main()