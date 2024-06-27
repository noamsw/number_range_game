import math
import random
# create a basic number guessing game


# create  a main if statement
if __name__ == '__main__':
    print("Hello and welcome to the minimum guesses guessing game")
    print("You are to provide two numbers, number A and number B such that number B is bigger than number A")
    print("A random number in the range chosen will be chosen, you must guess this number")
    
    numberA = input('Please enter the first number: ')
    while not numberA.isdigit():
        numberA = input('Please only enter a integer: ')
    numberB =  input('Please enter the second number in the range: ')
    while not numberB.isdigit() or numberB <= numberA: 
        numberB =  input('Please enter a integer which is larger than your first choice: ')
    numberA = int(numberA)
    numberB = int(numberB)
    length_of_range = numberB - numberA + 1
    max_guesses = int(math.log(length_of_range, 2)) + 1
    print(f'You have {max_guesses} guesses to guess the number')
    number = random.randint(numberA, numberB)

    for i in range(max_guesses):
        guess = input('Guess a number: ')
        while not guess.isdigit():
            guess = input('only guess an integer: ')
        guess = int(guess)
        if guess == number:
            print(f'Wow! you guessed the number in {i+1} guesses! very nice')
            quit()
        if guess > number:
            print("the number you guessed is too high, guess again")
        if guess < number:
            print("the number you guessed is too low, guess again")
    print(f"Sorry, no luck this time, the number was {number}")
    quit()