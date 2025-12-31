# Display Simple Character Data
def display_character_simple(character):
   
    print()
    print("=== Character Overview ===")
    print()
    
    print(f"Name: {character.get('Name', ['Unknown'])[0]}")     
    print(f"Race: {character.get('Race', ['Unknown'])[0]}")
    print(f"Ray: {character.get('Ray', ['Unknown'])[0]}")
    print(f"Power: {character.get('Power', ['Unknown'])[0]}")
    print(f"Job: {character.get('Job', ['Unknown'])[0]}")
    stats_display(character)
   
   
   
   
   
# Build attributes display
def stats_display(character):
    attributes_list = ["Health", "Mana", "Stamina", "Initiative", "Range", "Power Str.", "Strength", "Intelligence", "Endurance", "Wisdom", "Will", "Dexterity", "Agility", "Speed", "Durability", "Luck"]
    attributes_combat = ["Defense", "Melee Attack", "Range Attack", "Magic Attack", "Power Attack", "Protection"]
    print()
    print("=== Attributes ===")
    print()
    for attribute in attributes_list:
        value = character.get(attribute, [])
        if not value:
            print(f"{attribute}: —")
        else:
            print(f"{attribute}: {value[0]}")

    print()
    print("=== Combat Attributes ===")
    print()
    for attribute in attributes_combat:
        value = character.get(attribute, [])
        if not value:
            print(f"{attribute}: —")
        else:
            print(f"{attribute}: {value[0]}")


