"""
Game logic for PyDice.
Handles PvP, PvC, dice rolling mechanics, and result calculations.
"""

import random
from utils import get_player_name, get_valid_rounds

def show_round_result(p1_name, p1_roll, p2_name, p2_roll, round_num=1):
    """Displays the winner of the round."""
    print("-" * 40)
    print(f"{p1_name}  rolled : {p1_roll}")
    print(f"{p2_name}  rolled : {p2_roll}")
    
    if p1_roll == p2_roll:
        print(" Its a Tie!")
        print("-" * 40)
        return 0
    elif p1_roll > p2_roll:
        print(f"Winner  : {p1_name}")
        print("-" * 40)
        return 1
    else:
        print(f"Winner  : {p2_name}")
        print("-" * 40)
        return 2

def show_final_result(p1_name, p1_wins, p2_name, p2_wins, ties):
    """Displays the final game over screen and overall winner."""
    print("        GAME OVER - FINAL RESULT")
    print(f"  {p1_name}  : {p1_wins} wins")
    print(f"  {p2_name}  : {p2_wins} wins")
    print(f"  Ties    : {ties}")
    print("-" * 40)
    
    if p1_wins > p2_wins:
        print(f"   {p1_name} wins the game!")
    elif p2_wins > p1_wins:
        if p2_name == "PyBot":
            print("   PyBot wins! Better luck next time!")
        else:
            print(f"   {p2_name} wins the game!")
    else:
        print("   It's an overall tie! Great game!")

def play_pvp():
    """Handles the logic for Player vs Player game mode."""
    print("\n--- Player vs Player Mode ---")
    p1_name = get_player_name("Enter Player 1 name: ")
    p2_name = get_player_name("Enter Player 2 name: ")
    rounds = get_valid_rounds()
    
    p1_wins = 0
    p2_wins = 0
    ties = 0
    
    for current_round in range(1, rounds + 1):
        input(f"\n{p1_name}, press Enter to roll...")
        p1_roll = random.randint(1, 6)
        print(f"{p1_name} rolled : {p1_roll}")
        
        input(f"\n{p2_name}, press Enter to roll...")
        p2_roll = random.randint(1, 6)
        print(f"{p2_name} rolled : {p2_roll}")
        
        print()
        result = show_round_result(p1_name, p1_roll, p2_name, p2_roll, current_round)
        if result == 1:
            p1_wins += 1
        elif result == 2:
            p2_wins += 1
        else:
            ties += 1
            
    show_final_result(p1_name, p1_wins, p2_name, p2_wins, ties)

def play_pvc():
    """Handles the logic for Player vs Computer game mode."""
    print("\n--- Player vs Computer Mode ---")
    p1_name = get_player_name("Enter Player name: ")
    p2_name = "PyBot"
    rounds = get_valid_rounds()
    
    p1_wins = 0
    p2_wins = 0
    ties = 0
    
    for current_round in range(1, rounds + 1):
        input(f"\n{p1_name}, press Enter to roll...")
        p1_roll = random.randint(1, 6)
        print(f"{p1_name} rolled : {p1_roll}")
        
        print(f"\n{p2_name}'s turn...")
        p2_roll = random.randint(1, 6)
        print(f"{p2_name} rolled : {p2_roll}")
        
        print()
        result = show_round_result(p1_name, p1_roll, p2_name, p2_roll, current_round)
        if result == 1:
            p1_wins += 1
        elif result == 2:
            p2_wins += 1
        else:
            ties += 1
            
    show_final_result(p1_name, p1_wins, p2_name, p2_wins, ties)
