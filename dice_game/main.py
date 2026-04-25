
from display import show_banner, show_menu, show_how_to_play
from game import play_pvp, play_pvc

def main():
    show_banner()
    
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            play_pvp()
        elif choice == '2':
            play_pvc()
        elif choice == '3':
            show_how_to_play()
        elif choice == '4':
            print("Thanks for playing PyDice!")
            print("   See you next time! ")
            break
        else:
            print("Invalid choice! Enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
