import random
while True:
    user_action = input("Enter a choice (R for Rock, P for Paper, S for Scissors): \n")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    userSelection = ""
    if user_action == "R":
        userSelection += "Rock"
    elif user_action == "P":
        userSelection += "Paper"
    elif user_action == "S":
        userSelection += "Scissors"
    computerSelection = ""
    if computer_action == "R":
        computerSelection += "Rock"
    elif computer_action == "P":
        computerSelection += "Paper"
    elif computer_action == "S":
        computerSelection += "Scissors"
    print(f"\nPlayer ({userSelection}) : CPU ({computerSelection}).\n")
    if user_action == computer_action:
        print(f"Both players selected {userSelection}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Paper covers rock! You lose.")
            break
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
            break
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
            break