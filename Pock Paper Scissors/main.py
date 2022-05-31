from random import choice

options = ["R", "P", "S"]

player_choice = input("(R)ock, (P)aper, or (S)cissors?: ")

game_on = True

while game_on:
    if choice(options) == "R" and player_choice.upper() == options[2]:
        print("Player (Scissors) : CPU (Rock)")
        print("You win!")
        game_on = False
    elif choice(options) == "P" and player_choice.upper() == options[2]:
        print("Player (Scissors) : CPU (Paper)")
        print("Computer Wins")
        game_on = False
    elif choice(options) == "S" and player_choice.upper() == options[2]:
        print("Player (Scissors) : CPU (Scissors)")
        print("It's a draw. Play again")
        game_on = True
        player_choice = input("(R)ock, (P)aper, or (S)cissors?: ")
    elif choice(options) == "R" and player_choice.upper() == options[1]:
        print("Player (Paper) : CPU (Rock)")
        print("You Win")
        game_on = False
    elif choice(options) == "P" and player_choice.upper() == options[1]:
        print("Player (Paper) : CPU (Paper)")
        print("It's a draw. Play again")
        game_on = True
        player_choice = input("(R)ock, (P)aper, or (S)cissors?: ")
    elif choice(options) == "S" and player_choice.upper() == options[1]:
        print("Player (Paper) : CPU (Scissors)")
        print("Computer Wins")
        game_on = False
    elif choice(options) == "R" and player_choice.upper() == options[0]:
        print("Player (Rock) : CPU (Rock)")
        print("It's a draw. Play again")
        game_on = True
        player_choice = input("(R)ock, (P)aper, or (S)cissors?: ")
    elif choice(options) == "P" and player_choice.upper() == options[0]:
        print("Player (Rock) : CPU (Paper)")
        print("Computer Wins")
        game_on = False
    elif choice(options) == "S" and player_choice.upper() == options[0]:
        print("Player (Rock) : CPU (Scissors)")
        print("You Win")
        game_on = False
    elif player_choice not in options:
        player_choice = input("Please enter R for Rock, P for Paper, and S for Scissors: ")


