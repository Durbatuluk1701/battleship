                Welcome to Team 3's Battleship project!

In this file we will be explaining how our battleship game was created and how it works.
As a team we decided to use python as our coding language to implement this battleship game.
Our teams Battleship game used pygame as a library to produce a display of our game.
Now lets look at how this game was emplemented:

    1. Display Class
        -
    
    2. GameFlow Class

        - Overview: the gameflow class is used to run the game and do any interaction with the player. This class imports the display, computer, board, ship and tile calsses.

        - placeShips(): Uses nested for loops to make sure that when the user is placing ships he isnt placing them out of bounds or on top of another ship.
                        It also allows the user to pick which direction they want the ship to face before placing it down.

        - run(): runs the function that allows users to place ships and uses a while loop to continue the game util one side has all its ships destroyed.
    
    3. Board Class
        - Overview: This class creates a board using an array to act as the game grid and imports tile and ship classes.

        - setTile(xCoord, yCoord, value): This function sets a valid tile to what ever is passed through value.

        - placeShip(direction, ship, xCoord, yCoord): Places a ship where the user wants it placed as long as it is valid and then sets the tile s acoording to where the ship is using the ships name to keep track of of it.

        - isValid(xCoord, yCoord): returns true if a tile at the given x and y coordinate hasn't been attacked.

        - attackTile(xCoord, yCoord): makes sure it is a valid tile to attack and rreturns true if it attacked and false if it was a invalid tile to attack.

        -getTile(xCoord, yCoord): takes in an x,y coordinate and returns the value inside of the tile.
    
    4. Tile Class
        - Overview: the tile class holds all the information we need to know about a square on the grid.
                    A tile either holds water, a ship or if it has been attacked or not.

        - getTileItem(): returns what type of tile is in a given coordinate.

        - getTileAttacked(): returns true if tile has been attacked before and false if not.

        - setTileAttacked(): sets the bool for the tile to true that it has been attacked.

        - setTileItem(tileItem): sets what is in the tile through the parameters.
    
    5. Ship Class
        - Overview: Holds information on wht kind of ship, its health, how long it is, and where they are on the board.

        - getName(): returns name of ship.

        - damageShip(): decreases a given ship's health by one.

        - isDead(): Checks if the health of the ship is zero and if it is returns true otherwise false.
    
    6. Computer Class

        - Overview: The computer class is used to control all things AI related. This class imports the random library, board, ship and tile classees.
          In this class it has a private computer board for the AI and two funcitions to randomly select ship placement and how it guesses where to aim on the players board.
        
        - shipPlacement(): randomly selects an x,y coordinate and places a ship there.
          It checks in a up, down, left, right pattern taking in account the ship to see if it can place the ship and places it if it can.

        - shipGuess(userBoard): randomly selects an x,y coordinate on the board and checks if it has already tried to shoot there and if it has it gets new coordinates and if not the it fires there. 

