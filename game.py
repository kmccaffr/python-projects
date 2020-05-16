# Import modules and libraries for function use
import random

# Initialize exit condition as false
exit_condition = False

# Initialize variables
score_value = 0
enabled_list = []


# User / Computer comparison function for determining outcome, printing outcome, and updating score
def comparison_classification(choice_input, computer_input, ref_list):
    # Determine index in ref_list for user choice
    n_index = int(ref_list.index(choice_input))
    # Define value range for how left/right is split
    rot_range = int((len(ref_list) - 1) / 2)
    # Rotate the ref_list so that user choice is centered at middle
    ref_list = (ref_list[-(rot_range - n_index):] + ref_list[:-(rot_range - n_index)]) # Left - Win / Right - Loss
    c_index = int(ref_list.index(computer_input)) # Determine computer index of ref_list for left/right/center checks

    # Defined as win, check if within left half of ref_list
    if 0 <= c_index <= (rot_range - 1):
        print("Well done. Computer chose {option} and failed".format(option=computer_input))
        return score_value + 100
    # Defined as draw, check if option is centered
    elif c_index == rot_range:
        print("There is a draw ({option})".format(option=computer_input))
        return score_value + 50
    # Defined as loss, check if within right half of ref_list
    elif (rot_range + 1) <= c_index <= (rot_range * 2):
        print("Sorry, but computer chose {option}".format(option=computer_input))
        return score_value


# Starting Section
print("Welcome to Rock - Paper - Whatever!\nYou can play in classic mode, advanced, and configured mode.")
print("The object of the game is to beat the computer! Let's start with your name.")
# Input for name to check rating.txt file
username_input = input("Enter your name: ")
print("Hello, {name}".format(name=username_input))

# Input for mode
print("Modes of game:")
print("- Classic Mode: Standard Rock-Paper-Scissors")
print("- Advanced Mode: Rock-Gun-Lightning-Devil-Dragon-Water-Air-Paper-Sponge-Wolf-Tree-Human-Snake-Scissors-Fire")
print("\t-> Please see reference image on which option beats which.")
print("- Configured Mode: Choose an odd number of possible options for user/computer to pick!")
print("\t-> The options from left to right will define an ordered circle...")
print("\t-> your choice will lose against everything on the clockwise half and win against the counter-clockwise half.")

mode_option = input('Choose a Mode (classic/advanced/configured): ')

# Input for enabled choices
valid_selection = False

while not valid_selection:
    if mode_option == 'classic':
        enabled_list = ['rock', 'paper', 'scissors']
        print("Classic mode has been selected!")
        valid_selection = True
    elif mode_option == 'advanced':
        enabled_list = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']
        print("Advanced mode has been selected!")
        valid_selection = True
    elif mode_option == 'configured':
        print("You have selected configured mode, please enter your list with only commas separating them.")
        print("Example -> Input List: cat,thunder,dog,chair")
        enabled_options = input('Input List: ')
        enabled_list = enabled_options.split(',')
        valid_selection = True
    else:
        print("Invalid Mode Selected =(! Try again.")
print("Okay, let's start\n")

# Read rating.txt file and format
thisdict = {}  # Dictionary for corresponding keyword names to scores
ratings_file = open('rating.txt', 'rt')
ratings_list = ratings_file.readlines()  # Reducing file error risk by reading all at once before formatting in for loop
ratings_file.close()

# Loop through ratings_list and format for our previously declared dictionary
for _x in ratings_list:
    _temp = _x.strip('\n')  # Remove the new line added to end of every element
    _temp = _temp.split(": ")  # Split into name (_temp[0]) and score (_temp[1])
    thisdict["{name}".format(name=_temp[0])] = "{score}".format(score=_temp[1])

# Check for existence of player and score
if username_input in thisdict:
    score_value = int(thisdict["{name_}".format(name_=username_input)])

# Loop introduction
print("Input an option from your list to play the game or input tool commands!")
print("Tool Commands:")
print("list\t- This will output a list of enabled game choices.")
print("!exit\t- This will exit the game and save your score.")
print("!rating\t - This will output your current score.")

# Main loop for playing the game, checks for exit condition and if True will exit
while not exit_condition:

    # Selection of option from enabled list
    user_input = input('User Input: ')
    # Initializing computer choice as blank
    computer_choice = ''

    # If option is valid, select random option from enabled list for computer and use comparison function
    if user_input in enabled_list:
        computer_choice = random.choice(enabled_list)
        score_value = comparison_classification(user_input, computer_choice, enabled_list)

    # If input is !exit, save, update exit condition and print statement
    elif user_input == '!exit':
        exit_condition = True
        print('Saving Score...')
        thisdict[username_input] = str(score_value)
        names_list = []
        score_list = []
        for key in thisdict:
            names_list.append(key)
        for token in names_list:
            score_list.append(thisdict[token])
        output_list = []
        for i in range(len(names_list)):
            output_list.append('{name_f}: {score_f}\n'.format(name_f=names_list[i], score_f=score_list[i]))
        ratings_file = open('rating.txt', 'w+')
        ratings_list = ratings_file.writelines(output_list)
        ratings_file.close()
        print('Bye!')

    # If input is !rating, output current score for configured user
    elif user_input == '!rating':
        print(str(score_value))

    elif user_input == 'list':
        print("The game options that are enabled are:\n")
        print(enabled_list)

    # All other inputs will be considered invalid
    else:
        print('Invalid input')
