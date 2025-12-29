def display_character_full(character):
    # View/Debug entire character sheet
    for key, value in character.items():
        print()
        print(f"==={key}===")
        print()
        if isinstance(value, list):
            for item in value:
                print(f"- {item}")
        else:
            print(value)

