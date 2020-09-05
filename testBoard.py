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
if (board.placeShip("Down", fleet[1], 1, 1)):
    for x in range(fleet[1].getHealth):
        if not (board.getTile(1, 1 + x).getName() == fleet[1].getName()):
            placement = False
else:
    placement = False
if placement:
    print("Placement Test Down: Passed")
else:
    print("Placement Test Down: Failed")

if not (board.placeShip("right", fleet[2], 0, 2)):
    print("Placement Test Collision: Passed")
else:
    print("Placement Test Collision: Failed")

for x in range(9):
    printCheck = ""
    for y in range(9):
        printCheck += board.getTile(x, y).getItem()[0] + " "
    print(printCheck)

for x in range(9):
    printCheck = ""
    for y in range(9):
        printCheck += board.getTile(x, y).getAttacked() + " "
    print(printCheck)

x = 1
y = 1
for r in range(len(fleet)):
    if (fleet[r].getName() == board.getTile(x, y).getItem()):
        if (board.attackTile(x,y)):
            fleet[r].damageShip()
    board.attackTile(1,1)

for x in range(9):
    printCheck = ""
    for y in range(9):
        printCheck += board.getTile(x, y).getAttacked() + " "
    print(printCheck)

for boat in fleet:
    print(boat.getName() + " " + boat.getHealth())