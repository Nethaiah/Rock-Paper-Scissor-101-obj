Rock Paper Scissors 101 Game
This is a Python program that allows a player to play an advanced version of Rock Paper Scissors against a computer. The program interacts with an API to fetch available game objects and determine the outcome of the match.

Features
Fetches all the available game objects (like Rock, Paper, Scissors, etc.) from the RPS 101 API.
Allows the player to choose an object, while the computer randomly selects one.
Fetches and displays the result of the match (winner, loser, and outcome) from the RPS 101 API.
Prerequisites
Make sure you have the following installed:

Python 3.x
The requests library: You can install it using pip install requests
How to Run
Clone the repository or download the code.

Install dependencies using the following command:

bash
Copy code
pip install -r requirements.txt
Note: The only dependency required is the requests library.

Run the script using Python:

bash
Copy code
python rps_game.py
How it Works
The game fetches all available objects from the RPS 101 API.
The player selects an object, and the computer randomly selects one.
The game sends the selected objects to the API to fetch the result.
The result includes the winner, loser, and the outcome of the match, which is displayed to the player.
Code Structure
fetch_rps_objects(): Fetches the available game objects from the API.
choose_object_p1(objects): Allows the player to select an object from the list of objects.
choose_object_computer(objects): Randomly selects an object for the computer.
fetch_match_result(p1, computer): Fetches the result of the match between the player and the computer.
main(): Runs the game loop.
Example Output
bash
Copy code
Player 1 chooses: Rock
Computer chooses: Scissors

Winner: Player 1
Loser: Computer
Outcome: Rock crushes Scissors
Notes
The game will keep running in a loop until you terminate it (e.g., using Ctrl + C).
If you select an invalid object, you will be prompted to try again.
API Information
This game uses the RPS 101 API provided by rps101.pythonanywhere.com.

License
This project is licensed under the MIT License.
