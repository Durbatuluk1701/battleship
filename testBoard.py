from Ship import Ship
from Board import Board
from Tile import Tile



board = Board() #initializes a empty board
fleet = [Ship("carrier", 5), Ship("battleship", 4), Ship("destroyer", 3), Ship("gunboat", 2), Ship("dinghy", 1)] #template fleet for testing a empty board

print(board.placeShip("right", fleet[0], 0, 1)) #how to place a ship on board 


#how to print a board 
for y in range(9): #iterates over rows 
    printRow = ""   
    for x in range(9): #iterates over tile in the row
        printRow += board.getTile(x, y).getTileItem()[0] + " " #constructs the row and displays the first letter of the item on the tile so w = water, b = battleship, etc. 
    print(printRow) #prints completed row
print("")

#how to print a board's attack status (works same way as printing, just T = True, F = false)
for y in range(9):
    printRow = ""
    for x in range(9):
        printRow += str(board.getTile(x, y).getTileAttacked())[0] + " "
    print(printRow)
print("")

#how to attack a tile on the board
x = 1   #x and y coordinate
y = 1
if(board.getTile(x, y).getTileItem() != "water"):   #If tile is not water
    for r in range(len(fleet)): #for loop to iterate through fleet
        if (fleet[r].getName() == board.getTile(x, y).getTileItem()):   #compares the current ship name to the tile name
            if (board.attackTile(x,y)): #Checks to see if the tile has already been attacked before
                fleet[r].damageShip()   #damages ship if it attacked  a place which hasn't already been attacked
else:
    board.attackTile(x,y) #if water just attacks the tile

#how to check ship healths
for boat in fleet:
    print(boat.getName() + " " + str(boat.getHealth()))