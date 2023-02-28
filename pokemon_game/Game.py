def select_pokemon(player):
    print(f"{player.name}, select your Pokémon:")
    for i, p in enumerate(player.pokemon):
        print(f"{i+1}. {p['name']} ({p['type']})")
    choice = input("Enter the number of your choice: ")
    return player.pokemon[int(choice)-1]


def attack(attacker, defender):
    damage = 10  # Change this later to make it more realistic
    print(
        f"{attacker['name']} attacks {defender['name']} for {damage} damage!")
    defender['hp'] -= damage


def heal(pokemon):
    hp = 20  # Change this later to make it more realistic
    print(f"{pokemon['name']} has been healed for {hp} health points.")
    pokemon['hp'] += hp
