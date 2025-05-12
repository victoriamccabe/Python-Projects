# ReadMe for "Nice or Mean" Game

## Overview:

This is a text-based Python game where the player interacts with strangers and chooses whether to be "nice" or "mean." Their decisions influence the outcome, and the game has multiple endings based on their actions.

## Features:

* **User Interaction**: The player inputs their name (if new) and chooses to be "nice" or "mean."
* **Multiple Endings**: Winning or losing depends on the player's accumulated "nice" or "mean" actions.
* **Replay Option**: After the game ends, the player can choose to play again.
* **Visual Feedback**: Displays images ("Nice.png" or "Mean.png") depending on the outcome.

## Functions:

* **start()**: Initializes the game, either welcoming the player or thanking them for returning.
* **describe\_game()**: Asks for the player’s name if new or thanks them if returning.
* **nice\_mean()**: Prompts the player to choose between being nice or mean, and updates their score.
* **show\_score()**: Displays the current score.
* **score()**: Checks if the game is over based on scores, and calls `win()`, `lose()`, or continues.
* **win()**: Displays a winning message and image.
* **lose()**: Displays a losing message and image.
* **again()**: Asks if the player wants to play again.
* **reset()**: Resets the scores and restarts the game.

## Usage:

1. Run the script.
2. Enter your name (if new).
3. Choose "Nice" (N) or "Mean" (M).
4. Decide if you want to play again after the game ends.

## Prerequisites:

* Python 3.x
* `Pillow` library (for images): `pip install Pillow`

## Files:

* `Nice.png` – Image shown when the player wins.
* `Mean.png` – Image shown when the player loses.
