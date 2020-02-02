# Project 1: Tick tack toe

In this lesson we will create the fun and iconic game of tick tack toe.

## Pre-requisites
Before being able to complete this lesson you will need to know how to do the following:
1. Create and run a script
2. Print to the terminal
3. Create and execute functions
4. Create a while loop
5. Return a variable in a function

## Set up & project rules
For this project, we are going to create a game of tick tack toe. Using the agile methodologies, there will be multiple iterations for this project, as can be seen in the project iteration section.

## Project iterations
Below is a list with the various iterations of the project. 
These version are intended to break the project down into accomplishable steps, where at the end of every version you will have new functionality implemented. 

### Version 0.0.1
Create a function that will print the "board" for the game. The printed board does not have to be beautiful, but you should be able to see the board clearly. This board function should take in an array of 9 positions, and print each of those positions inside grid. Later we will be putting the moves of each player in this array.

The "board" for tick tack toe is a 3 x 3 grid. The board printed should look something like this:
```
   |   |
---+---+---
   |   |   
---+---+---
   |   |
```

This iteration will need one function:
`pint_board(moves)`

**This function should:**
* Take in a list with 8 positions in it
* Print each position in the list inside the grid

**When the script is run:**
* [ ] A function is run that:
    * [ ] Taken in a list (0 - 8)
    * [ ] Prints the board with the character in the list

**Hint:** Remember when using a list that the first position is 0 and not 1.

### Version 0.0.2
This version is going to get user input and then place it on the board. Please not that this is a simple solution, and the code solution is simple. This project will be refactored in a later iteration for a more elegant solution. 

Player 1 (the first player to move) is always `0`. The second player is `X`. Players take turns placing a `0` or `X` on the board. The players have the option of 9 spaces. 
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6  
---+---+---
 7 | 8 | 9
```

This iteration will need one new functions:
`player_one()`

**This function should:**
* Update the list where the user wishes to go with player ones symbol: `0`.

**When the script is run:**
* [ ] The board is printed
* [ ] Player 1 is asked where they would like to go (enters a number between 1 - 9)
* [ ] Player 1's move is displayed when the "board" is reprinted
* [ ] The program stops

**Hint:** The users input (1 - 9) will need to have 1 subtracted in order to correspond with the correct place on our board. 

### Version 0.0.3
In this iteration we are going to make the program get player 2's move. Remember that player 2's symbol is "X".

This iteration will need one new function:
`player_two()`

**This function should:**
* Update the list where the user wishes to go with player twos symbol: `X`.

**When the script is run:**
* [ ] The board is printed
* [ ] Player 1 is asked to enter their move (1 - 9), & the board is updated with their move
* [ ] Player 2 is asked to enter their move (1 - 9), & the board is updated with their move
* [ ] The program stops

### Version 0.0.4
In this iteration, we are going to make the game loop, so that after both players have entered their move the game does not end.

In this iteration we will need one new function:
`play_game()`

**This function should:**
* Print the board
* Call `player_one()`
* Call `player_two()`
* Loop these calls until 9 moves have been made

**When the script is run:**
* [ ] `play_game()` is run
    * [ ] The board is printed
    * [ ] Player 1 is asked to make a move
    * [ ] Player 2 is asked to make a move
    * [ ] Each player is asked to make a move until a total of 9 moves has happened
    * [ ] The program stops

### Version 0.0.5
Now we need to add a function that will validate each players move, as in the current version a player can write over the other players move, which they should not be able to. 

In this iteration we will need one new function:
`validate_move(move)`

**This function should:**
* Check that the input move is a number
* Check that the move number is between 1 - 9
* Verify that the position the move is being made to is empty
* Returns `True` if the move is valid
* Returns `False` if the move is not valid

**When the script is run:**
* [ ] `play_game()` is run
    * [ ] The board is printed
    * [ ] Player 1 is asked to make a move

### Version 1.0.0
This is the final step we need in order to have a functioning game of tick tack toe. We need to make a function that checks if a user has won the game.

A player wins when their symbol (`0`/`X`) is 3 in a row. 
```
0 wins when:
 0 | 0 | 0   |   0 |   |     |   0 |   |    
---+---+---  |  ---+---+---  |  ---+---+--- 
   |   |     |   0 |   |     |     | 0 |    
---+---+---  |  ---+---+---  |  ---+---+--- 
   |   |     |   0 |   |     |     |   | 0  
```

In this iteration we will need one new function:
`check_for_win()`

**This function should:**
* [ ] Checks if anyone has won the game (any winning combination)
* [ ] Returns 0 if no one has won
* [ ] Returns 1 if Player one won
* [ ] Returns 2 if Player two won

**When the script is run:**
* [ ] `play_game()` is run
    * [ ] The board is printed
    * [ ] Player 1 & 2 are asked to make a move
    * [ ] After every move, `check_for_win()` is run, and if anyone wins the loop ends and the winner is printed