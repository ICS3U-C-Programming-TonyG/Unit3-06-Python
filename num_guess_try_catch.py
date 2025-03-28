#!/usr/bin/env python3

# Created By: Tony G
# Date: 2025-03-27
# Asks for user input and tells user if number is correct or not, loops until correct

import random
def main():
    # Greeting message
    print("Greetings! Try to guess the correct number!")
    Random_number = random.randint(0, 9)

    # Infinitely loops program until user guesses correctly
    while True:
        try:
            # User input
            user_input = input("Please enter a number: ")
            # Convert input to an integer
            number = int(user_input)
            if number == Random_number:
                print("Congratulations! Correct!")
                # "breaks" loop if correct
                break
            else:
                print("Incorrect, try again :( Integer was " + str(Random_number))
        # Exception
        except ValueError:
            print(user_input + " is not a integer. Enter an integer.")

if __name__ == "__main__":
    main()