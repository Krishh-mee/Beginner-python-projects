import random

# this is list of dice faces in ASCII art 
DICE_ART= {
    1:(
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2:(
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),
    3:(
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4:(
         "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    5:(
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    6:(
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘",
    ),
}
def roll_dice(num_dice: int):
# this rolls the dice and return the list of results
    return[random.randint(1,6) for _ in range(num_dice) ]

def display_dice(dice_values):
    """Displays multiple dices side by side"""
    dice_faces = [DICE_ART[values] for values in dice_values]
    for line in zip(*dice_faces):
        print(" ".join(line))

def main():
    print("Welcome to the Dice roller")

    while True:
        try:
            num_dice= int(input("\nHow many dice you want to roll? :"))
            if not (1<= num_dice <=6):
                print("Please enter a number between 1 and 6")
                continue
        except ValueError:
            print("Enter a valid number")
            continue

        results= roll_dice(num_dice)
        print("\nYou rolled:")
        display_dice(results)
        print("Results:", results)

        roll_again = input("\nRoll again? (y/n): ").strip().lower()
        if roll_again!= "y":
            print("\nThanks for playing. Bye bye")
            break

if __name__== "__main__":
    main()