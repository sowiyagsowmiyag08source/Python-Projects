import random

options = ("rock", "paper", "scissors")
is_running = True

while is_running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (rock,paper,scissors):")
    
    print(f"player:{player}")
    print(f"computer:{computer}")
    
    if player == computer:
        print("it's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("you win!")
    else:
        print("you lose!")
    
    if input("play again? (y/n):").lower() != "y":
        is_running = False

print("Thanks for playing!!!")
