

import time

def typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def get_valid_rounds():
    while True:
        try:
            rounds = input("How many rounds would you like to play (1-10)? ")
            rounds = int(rounds)
            if 1 <= rounds <= 10:
                return rounds
            else:
                print("Invalid input! Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_player_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("Name cannot be empty! Please enter a valid name.")
