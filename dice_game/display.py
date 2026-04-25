"""
Display functions for the PyDice game.
Handles printing banners, menus, results, and dice faces.
"""

import datetime
from utils import typing_effect

def print_box(message):
    """Prints a message enclosed in a clean border."""
    print(f"  {message}")

def show_banner():
    """Shows the startup banner with a typing effect."""
    typing_effect("L o a d i n g   P y D i c e   G a m e . . .")
    print("       PyDice - The Dice Game  ")
    print("     Roll the Dice. Claim the Glory!")

def show_menu():
    """Displays the main menu with current date and time."""
    now = datetime.datetime.now()
    date_time_str = now.strftime("%d-%m-%Y  %I:%M %p")
    
    print(f" Date & Time : {date_time_str}")
    print("         PyDice - MENU")
    print("  1. Player vs Player")
    print("  2. Player vs Computer")
    print("  3. How to Play")
    print("  4. Exit")

def show_how_to_play():
    """Displays instructions on how to play the game."""
    print("            HOW TO PLAY")
    print("   Each player rolls one dice per round")
    print("   Dice values range from 1 to 6")
    print("   Higher number wins the round")
    print("   Same number = Tie round")
    print("   Player with most round wins = Winner")
    print("    Press Enter when it's your turn to roll")
