import random as rand

cities = ["Abreah", "Aerok", "Avhilanch City", "Britig", "Cregor", "Dragonspawnia", "Dungar", "Elysmira", "Faindor", "Fungalthorn", "Glas Suile", "Kalhoon", "Lyman", "Nikat", "Palmor Port", "Rivertin", "Rock Nation", "Shadow Deep", "Stallion", "Tanor"]
places = ["Forest", "River", "Ocean", "Port", "Mountains", "Cave", "Field", "Road"]
people = ["Archer", "Assassin", "Monk", "Ranger", "Warlock", "Farmer"]
npc_desc = ["creepy", "spooky", "haunting", "unearthly", "odd", "weird", "curious", "bizarre", "erratic", "strange", "unusual", "friendly", "chummy", "familiar", "good-natured"]
races = ["Alpi", "Angelic", "Dragonspawn", "Dwarf", "Elf", "Erutan", "Gnome", "Goblin", "Halfling", "Human", "Imp", "Ork", "Reefer", "Seinz", "Terrian", "Urk Hai", "Vennra"]
npc_type = ["man", "woman", "child"]
actions_neutral = [
    "searching the area carefully",
    "resting near the road",
    "arguing quietly amongst themselves",
    "examining strange markings nearby",
    "looking for treasure",
    "scouting the surroundings",
    "attempting to hide something",
    "watching from a distance",
    "moving cautiously through the area"
]
actions_positive = [
    "attempting to trade with you",
    "waving enthusiastically",
    "asking for directions",
    "offering assistance",
    "trying to get your attention",
    "warning you of nearby danger",
    "requesting help with a task",
    "sharing local rumors"
]
actions_hostile = [
    "about to attack",
    "preparing an ambush",
    "drawing their weapons",
    "closing in aggressively",
    "issuing threats",
    "attempting to intimidate"
]

def npc_action():
    action_categories = {
        "neutral": actions_neutral,
        "positive": actions_positive,
        "negative": actions_hostile
    }

    category = rand.choice(list(action_categories.keys()))
    action = rand.choice(action_categories[category])

    if category == "negative" and "attack" in action:
        target = rand.choice(npc_type)
        return f"about to attack a {target}"


    return action



def npc_count():
    rand_people = rand.choice(people)
    rand_npc_desc = rand.choice(npc_desc)
    num = rand.randint(1,6)
    if num == 1:
        return f'you encountered a {rand_npc_desc} {rand_people}'
    else:
        return f'you encountered {num} {rand_npc_desc} {rand_people}s'


def event_gen():
    rand_cities = rand.choice(cities)
    rand_cities_two = rand.choice(cities)
    rand_places = rand.choice(places)
    npc_gen = npc_count()
    npc_act = npc_action()

    print()
    print("===Generated Event===")
    print()
    print(f"While walking near the {rand_places} by {rand_cities}, {npc_gen} from {rand_cities_two} {npc_act}")
    print()
while True:
    print()
    print("===World Event Generator===")
    print()
    print("1. Generate Event")
    print("2. Exit")
    menu_select = int(input("Select: "))

    match menu_select:
        case 1:
            event_gen()
            input("Press Enter to return to menu...")

        case 2: 
            break
        case _:
            print("Input unknown. Please try again.")
            input("Press Enter to return to menu...")

