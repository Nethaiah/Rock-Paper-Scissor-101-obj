# Rock-Paper-Scissors Game
==========================

## Introduction
This is a Rock-Paper-Scissors game implemented in Python. The game fetches the list of available objects from an API, allows the player to choose an object, and then randomly selects an object for the computer. The game then determines the winner based on the game's rules.

## Requirements
* Python 3.x
* `requests` library for making API requests
* `random` library for generating random numbers
* `json` library for parsing JSON responses

## How to Play
1. Run the game by executing the `main.py` file.
2. The game will fetch the list of available objects from the API and display them.
3. Enter the object you want to choose.
4. The computer will randomly select an object.
5. The game will determine the winner based on the game's rules.

## Functions
### `fetch_rps_objects()`
Fetches the list of available objects from the API.

### `choose_object_p1(objects)`
Allows the player to choose an object from the list of available objects.

### `choose_object_computer(objects)`
Randomly selects an object for the computer.

### `fetch_match_result(p1, computer)`
Determines the winner of the game based on the game's rules.

### `main()`
The main game loop that fetches the list of available objects, allows the player to choose an object, randomly selects an object for the computer, and determines the winner.

## API Endpoints
* `https://rps101.pythonanywhere.com/api/v1/objects/all`: Fetches the list of available objects.
* `https://rps101.pythonanywhere.com/api/v1/match?object_one={p1}&object_two={computer}`: Determines the winner of the game.

## License
This game is licensed under the MIT License.
