import random

def roll_die(sides):
    return random.randint(1, sides)

    
def roll_and_display(sides, mode="normal"):
    print()

    if mode == "normal":
        roll = roll_die(sides)
        print("You rolled normally.")
        print(f"Result: {roll}")

    else:
        roll_one = roll_die(sides)
        roll_two = roll_die(sides)

        print(f"You rolled with {mode.upper()}!")
        print(f"Rolls: {roll_one} and {roll_two}")

        if mode == "advantage":
            chosen = max(roll_one, roll_two)
        elif mode == "disadvantage":
            chosen = min(roll_one, roll_two)
        else:
            print("Unknown roll mode.")
            return

        print(f"Result used: {chosen}")

    print()
    input("Press Enter to return to menu...")


while True:

    dice_map = {
        "1": 4,
        "2": 6,
        "3": 8,
        "4": 10,
        "5": 12,
        "6": 20,
        "7": 100
    }
    print("Roll mode:")
    print("1. Normal")
    print("2. Advantage")
    print("3. Disadvantage")

    mode_choice = input("Select roll mode: ")

    if mode_choice == "1":
        mode = "normal"
    elif mode_choice == "2":
        mode = "advantage"
    elif mode_choice == "3":
        mode = "disadvantage"
    else:
        print("Invalid mode.")
        continue
    print()
    print("Select die:")
    print("1. D4")
    print("2. D6")
    print("3. D8")
    print("4. D10")
    print("5. D12")
    print("6. D20")
    print("7. D100")
    print("8. Exit")

    die_choice = input("Select a die: ")

    if die_choice == "8":
        break

    if die_choice not in dice_map:
        print("Invalid die selection.")
        continue

    sides = dice_map[die_choice]
    roll_and_display(sides, mode)

