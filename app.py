from flask import Flask, request, jsonify
from pokemon_game import Pokemon, Trainer, Game

app = Flask(__name__)

game = Game()


@app.route('/start', methods=['POST'])
def start():
    # Get the player name from the request
    data = request.json
    player_name = data['player_name']

    # Start the game with the player name
    game.start(player_name)

    # Return the player's name and the available Pokémon as a response
    response = {
        'player_name': game.player.name,
        'available_pokemon': [p.to_dict() for p in game.player.pokemon],
    }
    return jsonify(response)


@app.route('/choose', methods=['POST'])
def choose():
    # Get the chosen Pokémon from the request
    data = request.json
    pokemon_name = data['pokemon_name']

    # Choose the player's Pokémon
    game.choose_pokemon(pokemon_name)

    # Return the chosen Pokémon as a response
    response = {
        'chosen_pokemon': game.player_pokemon.to_dict(),
    }
    return jsonify(response)


@app.route('/attack', methods=['POST'])
def attack():
    # Attack the enemy's Pokémon
    game.attack()

    # Return the updated game state as a response
    response = {
        'player_pokemon': game.player_pokemon.to_dict(),
        'enemy_pokemon': game.enemy_pokemon.to_dict(),
        'game_over': game.game_over,
    }
    return jsonify(response)


@app.route('/heal', methods=['POST'])
def heal():
    # Heal the player's Pokémon
    game.heal()

    # Return the updated game state as a response
    response = {
        'player_pokemon': game.player_pokemon.to_dict(),
        'enemy_pokemon': game.enemy_pokemon.to_dict(),
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
