from select import select
import time
import getch
import sys
import contextlib
import termios
import sys
from Board import Board
from Bomber import Bomber
from Enemy import Enemy
import os
from select import select
import time
import math
import random

matrix=[]
board=Board(68, 34, matrix)
bmbman=Bomber(2, 4, board, 0)
enemies=Enemy(10, 10, board, bmbman)

# enemies=[]
# for i in range(1, 6):
# 	newX=math.floor(random.random()*15)*4
# 	newY=math.floor(random.random()*15)*2
# 	if (newX>=4 and newX<=64) and (newY>=4 and newY<=32): 
# 		enemies.append(Enemy(newX, newY, board, bmbman))

keypressed=0
board.makeWall()
print(board.getBoard())

@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)

def isKeyPressed():
	i, o, e=select([sys.stdin], [], [], 0)
	return i!=[]

while True:
	time.sleep(0.1)
	os.system("clear")
	enemies.move()
	board.edit(enemies.posx, enemies.posy, enemies)

	# for i in range(1, 6):
	# 	enemies[i].move()
	# 	board.edit(enemies[i].posx, enemies[i].posy, enemies[i])
	bmbman.bomb_update()
	with raw_mode(sys.stdin):
		try:
			if isKeyPressed():
				ch = sys.stdin.read(1)
				keypressed=ch
				bmbman.move(keypressed)
		except (KeyboardInterrupt):
			pass
	termios.tcflush(sys.stdin, termios.TCIOFLUSH)
	print(board.getBoard())
	print("Score: "+str(bmbman.score))