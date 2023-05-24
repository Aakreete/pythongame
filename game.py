import random  # this random module allows for generating random numbers.


def guess_the_number():  # 'guess the number' function is defined here.
    # It serves as the main logic for the 'guess the numbers'.
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    # inside the function, the program generates
    secret_number = random.randint(1, 100)
    # a random number between 1 and 100 using 'random.randint(1,100)'.
    # This number is a secret number that the player needs to guess.
    attempts = 0  # The 'attempts' variable is initialized to keep track of the number
    # of attempts the player has made to guess the number.

    while True:  # The 'while' loop is used to repeatedly prompt the player for their
        # guess until they guess the correct number
        # Inside the loop, the player's guess is
        guess = int(input("Take a guess: "))
        # obtained through 'input', and it is converted to an integer using 'int()'.
        attempts += 1  # here "attempt +=1 is an example of an assignment statement
        # that  increases the value of variable 'attempt' by 1"

        if guess < secret_number:
            # If the player's 'guess' is less than the 'secret_number',
            #The program will print the message 'The number is too low!'
            # to inform the player that their guess is lower than the
            # secret number.
            print("This number is too low!")
        elif guess > secret_number:
            print("This number is too high!")
            # If the player's 'guess' matches the 'secret number', the
            # program will print the message Thiss number is too high!'
            # to inform the player that their guess is higher than the
            # secret number.
        else:
            print("Congratulations!!! You guessed the number in",
                  attempts, "attempts.")
            # If the player's 'guess' matches the 'secret number', the program
            # will print the message 'congratulations in [attempts]attempts.' This
            # message congratulates the player for guessing the correct number and
            # displays thetotal numberr of attempts it took them to do so.
            break  # The 'break' statement is crucial in this case to ensure that the
        # game loop is terminated once the player guesses the correct number. allowing
        # the program toproceeds to the end of the game logic.


guess_the_number()  # after defining this logic the 'guess_the_number()' function
# is called.