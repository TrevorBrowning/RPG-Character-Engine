# Display Simple Character Data
def display_character_simple(character):
   
    print()
    print("=== Character Overview ===")
    print()
    print(f"Name: {character['Name'][0]}")
    print(f"Race: {character['Race'][0]}")
    print(f"Ray: {character['Ray'][0]}")
    print(f"Power: {character['Power'][0]}")
    print(f"Job: {character['Job'][0]}")
    stats_display(character)
   
   
   
   
   
# Build attributes display
def stats_display(character):
    attributes_list = ["Health", "Mana", "Stamina", "Initiative", "Range", "Power Str.", "Strength", "Intelligence", "Endurance", "Wisdom", "Will", "Dexterity", "Agility", "Speed", "Durability", "Luck"]
    attributes_combat = ["Defense", "Melee Attack", "Range Attack", "Magic Attack", "Power Attack", "Protection"]
    print()
    print("=== Attributes ===")
    print()
    for attribute in attributes_list:
        print(f"{attribute}: {character[attribute][0]}")
    print()
    print("=== Combat Attributes ===")
    print()
    for attribute in attributes_combat:
        print(f"{attribute}: {character[attribute][0]}")

