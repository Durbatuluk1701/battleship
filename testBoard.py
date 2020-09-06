from Ship import Ship
from Board import Board
from Tile import Tile



board = Board()
fleet = [Ship("carrier", 5), Ship("battleship", 4), Ship("destroyer", 3), Ship("gunboat", 2), Ship("dinghy", 1)]

placement = True
print(board.placeShip("right", fleet[2], 0, 1))

for y in range(9):
    printRow = ""
    for x in range(9):
        printRow += board.getTile(x, y).getTileItem()[0] + " "
    print(printRow)
print("")

for y in range(9):
    printRow = ""
    for x in range(9):
        printRow += str(board.getTile(x, y).getTileAttacked())[0] + " "
    print(printRow)
print("")

x = 2
y = 3
if(board.getTile(x, y).getTileItem() != "water"):
    for r in range(len(fleet)):
        if (fleet[r].getName() == board.getTile(x, y).getTileItem()):
            if (board.attackTile(x,y)):
                fleet[r].damageShip()
else:
    board.attackTile(x,y)


for y in range(9):
    printRow = ""
    for x in range(9):
        printRow += str(board.getTile(x, y).getTileAttacked())[0] + " "
    print(printRow)

for boat in fleet:
    print(boat.getName() + " " + str(boat.getHealth()))