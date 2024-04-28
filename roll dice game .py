import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Roll the Dice game!")
    while True:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print("You rolled:", dice_roll)
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
