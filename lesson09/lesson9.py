# Lesson 9
from random import choice
while True:
    user_choice = input("Rock, paper, or scissors: ")
    user_choice = user_choice.lower()

    if user_choice not in {"rock", "paper", "scissors"}:
        print("Please select a valid choice (rock, paper, or scissors)")
        continue

    else:
        ai_choice = choice(["rock", "paper", "scissors"])
        if ai_choice == "rock":
            if user_choice == "rock":
                print(f"Draw! {user_choice} vs. {ai_choice}.")
            elif user_choice == "paper":
                print(f"Win! {user_choice} vs. {ai_choice}.")
            else:
                print(f"Lose! {user_choice} vs. {ai_choice}.")

        if ai_choice == "paper":
            if user_choice == "paper":
                print(f"Draw! {user_choice} vs. {ai_choice}.")
            elif user_choice == "scissors":
                print(f"Win! {user_choice} vs. {ai_choice}.")
            else:
                print(f"Lose! {user_choice} vs. {ai_choice}.")

        if ai_choice == "scissors":
            if user_choice == "scissors":
                print(f"Draw! {user_choice} vs. {ai_choice}.")
            elif user_choice == "rock":
                print(f"Win! {user_choice} vs. {ai_choice}.")
            else:
                print(f"Lose! {user_choice} vs. {ai_choice}.")
        break