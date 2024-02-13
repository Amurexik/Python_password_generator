import string
import random
import sys

prompt = "Choose character types that your password should contain: \n 1. Lowercase letters \n 2. Uppercase letters \n 3. Numbers \n 4. Special characters \n 5. Done with selection \n 6. Quit \n Please enter a number: "

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
special_characters = list(string.punctuation)
max_length = 30
min_length = 8 # Do not change to less than 5. I would like even the most basic password to contain at least 5 characters
char_types_minimum = [] # To ensure having at least 1 character from each selected character type(eg. number, uppercase letter) for stronger password
char_type_selection = []
type_selection = ""
password = []

random.shuffle(lowercase_letters)
random.shuffle(uppercase_letters)
random.shuffle(numbers)
random.shuffle(special_characters)


print("Welcome to password generator! \n")
print("Strong password should contain at least: \n 1 lowercase character \n 1 uppercase character \n 1 number \n 1 special character \n")

while True:
    try:
        user_input = int(input(prompt))
        if user_input == 1:
            char_types_minimum.append(lowercase_letters)
            char_type_selection = char_type_selection + lowercase_letters
            type_selection += "Lowercase letters,"
        elif user_input == 2:
            char_types_minimum.append(uppercase_letters)
            char_type_selection = char_type_selection + uppercase_letters
            type_selection += "Uppercase letters,"
        elif user_input == 3:
            char_types_minimum.append(numbers)
            char_type_selection = char_type_selection + numbers
            type_selection += "Numbers,"
        elif user_input == 4:
            char_types_minimum.append(special_characters)
            char_type_selection = char_type_selection + special_characters
            type_selection += "Special characters,"
        elif user_input == 5:
            if not char_types_minimum:
                print("\nYou need to select at least one character type! \n")
                continue
            type_selection = type_selection.rstrip(",")
            print(f"Selected character types for your password: \033[1m{type_selection}\033[0m") #printing type_selection bold
            break
        elif user_input == 6:
            sys.exit(1)
        else:
            print("\nYou need to type a number from the menu\n")

    except KeyboardInterrupt:
        sys.exit(1)
    except ValueError:
        print("\nYou need to choose a number!\n")


while True:
    try:
        user_input_len = int(input(f"\nPlease enter the length of your password(number between {min_length}-{max_length}): "))
        if user_input_len in range(min_length,max_length+1):
            break
        else:
            print("Wrong input, please try again!")
    except KeyboardInterrupt:
        sys.exit(1)
    except ValueError:
        print("Wrong input! You need to enter a number")

for i in range(1):
    for j in range(len(char_types_minimum)):
        password.append(char_types_minimum[j][0])

while len(password) < user_input_len:
    char = random.choice(char_type_selection)
    password.append(char)

random.shuffle(password)
final_password = "".join(password)
print("\nYour new password is: " + "\033[1m" + final_password +"\033[0m")




