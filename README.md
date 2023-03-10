# Battleships

A version of the classic battleship game built by use of python.

The purpose of this application is to provide the user with a playable battleship game built with specifically python.

The application gives the user a compitition against a generated oponent. The landing page will great the user with the question of if they are intrested in playing a game of battleship, and if so to enter their name. If the user chooses to enter their name, they will be welcomed to the game, the users playing board will be generated as will a guessing board. The user will be asked to input coordinates as guesses and the oponent has their guess randomly generated. When one of the two have sunken all of the others ships, the user is informed of the winner and asked if they wnat to restart the game. If yes, the playing boards are cleared and ships generated again. If not, the game loop is exited and the user recives a message to indicate that they have left the game.

[LIVE SITE HERE](https://battleships-python-game.herokuapp.com/)

## Features

### Landing page

The landing page introduces the user with what it is, through a question of if the user wants to play a game of battleship. It also asks for the users name to initite the game.  

<img src="readme-images/landing-page.png" alt="Image showing landing page">

<br>

### Game start

After providing their name, the user is introduced to how the game works. They are shown their own board and a guessing board, hiding the oponents board, and asked to make a guess of on which cordinates hides the oponents ships.

<img src="readme-images/game-start-1.png" alt="Image showing page as game starts">
<img src="readme-images/game-start-2.png" alt="Image showing page as game starts">

<br>

### Coordinates entered

As the coordinates have been entered, the user is informed of the round results. In the case bellow, the computer found one of the users ships and the user missed. The results will also be shown on the users board and guess board. This is done to show a visual representation of where both the computer and user have guessed, as well as how many ships have been hit. 

As neither the user or the computer has found all of the oponents ships, the user is urged to take another guess, and the game continues in the same fashion.

<img src="readme-images/coordinates-entered-1.png" alt="Image showing page as game starts">
<img src="readme-images/coordinates-entered-2.png" alt="Image showing page as game starts">

<br>

### Winner is anounced

When either the computer or the user has sunken all of the oponents ships, the game ends and the winner is anounced. In the case bellow, the game ended with the user winning. But the game can also end with the computer winning or as a draw. In those cases the message displayed will reflect that reult.

As the game has ended, the user is faced with the question of if they want to restart the game.

<img src="readme-images/winner.png" alt="Image showing game winner and questioning if the user wants to continue playing">

<br>

### Continue playing

The user can now choose to either restart the game or end the game. If they choose to restart the game, all boards will reset, the ship placement will be rerandomized and a message will indicate that the game is restarted. 

Each game is it's own and the program will not keep count of how many games each party has won. 

<img src="readme-images/restart-y.png" alt="Image showing game restarting">

<br>

If the user chooses to end the game, they will exit the game and a message will indicate that they have left.

<img src="readme-images/restart-n.png" alt="Image showing user exiting game">

<br>

## Future implementations

A future vertion of the app will feature a function to keep count of computer and user wins between different games. So the games played between computer and user will be connected instead of being completely seperate games.

