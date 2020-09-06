from Ship import Ship
from Board import Board
from Tile import Tile



board = Board()
fleet = [Ship("carrier", 5), Ship("battleship", 4), Ship("destroyer", 3), Ship("gunboat", 2), Ship("dinghy", 1)]


try:
    board.placeShip("up", fleet[1], -1, 0)
    print("Exception X < 0 Test: Failed")
except:
    print("Exception X < 0 Test: Passed")

try:
    board.placeShip("up", fleet[1], 9, 0)
    print("Exception X > 8 Test: Failed")
except:
    print("Exception X > 8 Test: Passed")


try:
    board.placeShip("up", fleet[1], 0, -1)
    print("Exception Y < 0 Test: Failed")
except:
    print("Exception Y < 0 Test: Passed")

try:
    board.placeShip("up", fleet[1], 0, 9)
    print("Exception Y > 8 Test: Failed")
except:
    print("Exception Y > 8 Test: Passed")

if not (board.placeShip("up", fleet[1], 1, 1)):
    print("Invalid Placement up: Passed")
else:
    print("Invalid Placement up: Failed")

if not (board.placeShip("left", fleet[1], 1, 1)):
    print("Invalid Placement left: Passed")
else:
    print("Invalid Placement left: Failed")

if not (board.placeShip("down", fleet[1], 7, 7)):
    print("Invalid Placement down: Passed")
else:
    print("Invalid Placement down: Failed")

if not (board.placeShip("right", fleet[1], 7, 7)):
    print("Invalid Placement right: Passed")
else:
    print("Invalid Placement right: Failed")




placement = True
if (board.placeShip("right", fleet[1], 2, 3)):
    for y in range(fleet[1].getHealth()):
        if (board.getTile(1, 1 + y).getTileItem() != fleet[1].getName()):
            placement = False
else:
    placement = False
if placement:
    print("Placement Test Down: Passed")
else:
    print("Placement Test Down: Failed")

print(board.getTile(1,4).getTileItem())




if not (board.placeShip("up", fleet[2], 3, 4)):
    print("Placement Test Collision: Passed")
else:
    print("Placement Test Collision: Failed")




for y in range(9):
    printCheck = ""
    for x in range(9):
        printCheck += board.getTile(x, y).getTileItem()[0] + " "
    print(printCheck)
print("")

for y in range(9):
    printCheck = ""
    for x in range(9):
        printCheck += str(board.getTile(x, y).getTileAttacked())[0] + " "
    print(printCheck)
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
    printCheck = ""
    for x in range(9):
        printCheck += str(board.getTile(x, y).getTileAttacked())[0] + " "
    print(printCheck)

for boat in fleet:
    print(boat.getName() + " " + str(boat.getHealth()))