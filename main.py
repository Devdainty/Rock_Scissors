import random

player = input("Enter a choice(R , P , or S) : ").upper() #collects input from user

possible_options = ["Rock", "Paper", "Scissors"] #List of options

CPU_actions = random.choice(possible_options) #computer makes its choice from random numbers

while True:
    if player == "R":
        player = "Rock"

    elif player == "P":
        player = "Paper"
    
    elif player == "S":
        player = "Scissors"
    
    elif player not in possible_options:
        print("You entered an invalid option")
        player = input("Enter a choice(R , P , or S) : ").upper()

    elif player == CPU_actions:
        print(f"Player({player}): CPU({CPU_actions})")
        print(f"Both players selected {player}, therefore its a tie")
        print("Replay")
        player = input("Enter a choice(R , P , or S) : ").upper()
        CPU_actions = random.choice(possible_options)
        continue

    else:
        print(f"Player({player}): CPU({CPU_actions})")

        if player == "Rock":
            if CPU_actions == "Scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose!")

        elif player == "Paper":
            if CPU_actions == "Rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose!")
        
        elif player == "Scissors":
            if CPU_actions == "Paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose!")
        
        print("Game Over")
        break




