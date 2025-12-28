import random
low=1
high=100
guesses=0
answer=random.randint(low,high)
is_running=True
while is_running:
    guess=(input(f"Enter your guessing number {low}-{high}:"))
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<low or guess>high:
            print("That number is out of range")
            print(f"Please enter the valid guess number between {low} and {high}")
        elif guess<answer:
            print("Too low! Try again!!")
        elif guess>answer:
            print("Too high! Try again!!")
        else:
            print("----------------------------------------------------")
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            print(f"This round took you {guesses} guesses")
            is_running=False
    else:
        print("Invalid guess")
        print(f"please select a number between {low} and {high}")
    
