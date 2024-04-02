import random
import os 
# def guess_number():
#     """
#     This function generates a random number between 1 and 100,
#     and asks the user to guess it. The user can indicate whether
#     the guess is higher or lower than the correct number, and the
#     function will update the range of possible numbers accordingly.
#     The function will stop when the user correctly guesses the number.
#     """
#     low = 1
#     high = 100
#     guess = random.randint(low, high)
    
#     while True:
#         print(f"Is it {guess}?")
#         # Ask the user for input
#         user_input = input("Enter 'b' for bigger, 'l' for lower, or 'c' for correct: ")
        
#         if user_input == 'b':
#             # The guess is too high. Update the low end of the range.
#             low = guess + 1
#             guess = random.randint(low, high)
#         elif user_input == 'l':
#             # The guess is too low. Update the high end of the range.
#             high = guess - 1
#             guess = random.randint(low, high)
#         elif user_input == 'c':
#             print("Computer guessed the number correctly!")
#             break
#         else:
#             print("Invalid input. Please enter 'b', 'l', or 'c'.")
    
# guess_number()

def guess_number() :
    low = 1
    high = 99
    guess = random.randint(low,high)
    
    while True:
        print(f"it is {guess}?")
        user_input = input("Enter 'b' for bigger, 'l' for lower, or 'c' for correct:")
        
        if user_input == 'b':
            low = guess + 1
            guess = random.randint(low,high)
        elif user_input == 'l':
            high = guess - 1
            guess = random.randint(low,high)        
        elif user_input == 'c':
            print("Computer guessed the number correctly!")  
            break
        else:
            print("Invalid input. Please enter 'b', 'l', or 'c'.")
guess_number()