from presentations.simple import display_character_simple
from presentations.extended import display_character_extended             
from presentations.full import display_character_full
def read_file():
    with open("character.csv") as file_data:
        char_data = file_data.read()
    return char_data

file_data = read_file()

def load_character(file_data):
    split_file = file_data.split("\n")
    csv_data = []
    for data in split_file:
        line = data.split(",")
        csv_data.append(line)

    header_data = csv_data[0]
    row_data= csv_data[1:]


    character = {}
    for header in header_data:
        character[header] = []


    for row in row_data:
        for header_name, cell_value in zip(header_data, row):
            if cell_value != "":
                character[header_name].append(cell_value)

    return character

def main():
    character = load_character(file_data)


    while True:
        print("RPG Character Engine")
        print()
        print("1. Show Simple Character Sheet")
        print("2. Show Extended Character Sheet")
        print("3. Show All/Debug Character Sheet")
        print("4. Exit")
        print()
        menu_choice = input("Enter your choice: ")
        
        if menu_choice == "1":
            display_character_simple(character)
            print()
            input("Press Enter to return to menu...")

        elif menu_choice == "2":
            display_character_extended(character)
            print()
            input("Press Enter to return to menu...")

        elif menu_choice == "3":
            display_character_full(character)
            print()
            input("Press Enter to return to menu...")

        elif menu_choice == "4":
             break
        
        else:
            print()
            print("Unknown command. Please try again.")
            print()


if __name__ == "__main__":
    main()