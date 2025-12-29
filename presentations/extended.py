# Display Extended Character Data
def display_character_extended(character):
   
    print()
    print("*=== Character Overview ===*")
    print()
    print(f"Name: {character['Name'][0]}")
    print(f"Race: {character['Race'][0]}")
    print(f"Ray: {character['Ray'][0]}")
    print(f"Power: {character['Power'][0]}")
    print(f"Job: {character['Job'][0]}")
    print(f"Personality: {character['Personality'][0]}")
    print(f"Type: {character['Type'][0]}")
    print(f"Special Moves: {character['Special Moves'][0]}")
    print(f"Honor: {character['Honor'][0]}")
    print(f"Prestige: {character['Prestige'][0]}")
    print(f"Level: {character['Level'][0]}")
    background_display(character)
    assets_display(character)
    skills_display(character)
    stats_display(character)
   
   
   
   
# Build attributes display
def stats_display(character):
    attributes_list = ["Health", "Mana", "Stamina", "Initiative", "Range", "Power Str.", "Strength", "Intelligence", "Endurance", "Wisdom", "Will", "Dexterity", "Agility", "Speed", "Durability", "Luck"]
    attributes_combat = ["Defense", "Melee Attack", "Range Attack", "Magic Attack", "Power Attack", "Protection"]
    print()
    print("*=== Stats ===*")
    print()
    print("== Attributes ==")
    print()
    for attribute in attributes_list:
        print(f"{attribute}: {character[attribute][0]}")
    print()
    print("== Combat Attributes ==")
    print()
    for attribute in attributes_combat:
        print(f"{attribute}: {character[attribute][0]}")

# Build skills display
def skills_display(character):
    print("*=== Skills ===*")
    print()
    for skill in character["Skills"]:
        print(skill)

# Build assets display
def assets_display(character):
    print()
    print("*=== Assets ===*")
    print()
    print(f"Money: {character['Money'][0]}")
    print(f"Bank: {character['Bank'][0]}")
    print()
    print("== Shops ==")
    print()
    for store in character["Stores"]:
        print(store)
    print()
    print("== Vehicles ==")
    print()
    for vehicle in character["Vehicles"]:
        print(vehicle)
    print()
    

# Build background display
def background_display(character):
    print()
    print("*=== Background ===*")
    print()
    print("== Family ==")
    print()
    for family in character["Family"]:
        print(family)
    print()
    print("== Known Languages ==")
    for language in character["Known Languages"]:
        print(language)
    print()
    print("== Notable Offenses ==")
    print()
    for offense in character["Notable Offenses"]:
        print(offense)
    print()


