#!/usr/bin/env python3

# Created By: Tony G
# Date: 2025-03-27
# Asks for user input and tells user if number is correct or not, loops until correct

def main():
    # Greeting message
    print("Greetings! Try to guess the correct number!")

    # Infinitely loops program until user guesses correctly
    while True:
        try:
            # User input
            user_input = input("Please enter a number: ")
            # Convert input to an integer
            number = int(user_input)
            if number == 5:
                print("Congratulations! Correct!")
                # "breaks" loop if correct
                break  
            else:
                print("Incorrect, try again :(")
        # Exception
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()