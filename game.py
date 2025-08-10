import random 
choices = ["rock", "paper", "scissors"]

while True:  
    
    user_choice = input("Type rock, paper, or scissors (or 'quit' to stop): ").lower()

    if user_choice == "quit":
        print("Thanks for playing!")
        break 
    if user_choice not in choices:
        print("That's not a valid choice. Please try again.")
        continue 
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock breaks scissors.")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper covers rock.")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors cut paper.")
    else:
        print("Computer wins!")
