import random

user_wins = 0
computer_wins = 0

options=["rock","paper","scissors"]

while True:
    user_input =input("Type Rock/Paper/Scissors or Q :").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_no = random.randrange(2)

    computer_pick = options[random_no]
    print("computer_pick", computer_pick, ".")


    if user_input == "rock" and computer_pick == "scissors":
        print("U won it")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("U wont it")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("U won it")
        user_wins += 1
    else:
        print("Computer Won it")
        computer_wins += 1

print("user_wins", user_wins, "times")
print("computer_wins", computer_wins, "times")