from rooms import roomDat
from roomStructure import locations, objId
from player import playerDat
import random
from numpy import array

class monster():
	def __init__(self, pos, type):
		self.pos = pos
		self.type = type
		self.health = 10
		self.moveChance = 100
	def enemyMove(self):
		moved = random.randrange(1, 100)
		monstersHit = 0
		totalDammage = 0
		if moved <= self.moveChance:
			moveDir = random.randrange(1, 3) #horrizontal, virticle
			y, x = 0, 0
			if moveDir == 1:
				if playerDat.roomPos[1] - self.pos[1] < 0:
					#print('left')
					y = -1
				elif playerDat.roomPos[1] - self.pos[1] > 0:
					#print('right')
					y = 1
				else:
					y = 0
					if playerDat.roomPos[0] - self.pos[0] < 0:
						#print('up')
						x = -1
					elif playerDat.roomPos[0] - self.pos[0] > 0:
						#print('down')
						x = 1
			else:
				if playerDat.roomPos[0] - self.pos[0] < 0:
					#print('up')
					x = -1
				elif playerDat.roomPos[0] - self.pos[0] > 0:
					#print('down')
					x = 1
				else:
					x = 0
					if playerDat.roomPos[1] - self.pos[1] < 0:
						#print('left')
						y = -1
					elif playerDat.roomPos[1] - self.pos[1] > 0:
						#print('right')
						y = 1
			newPos = self.pos + [x, y]
			#print(f'a monster tried to move from {self.pos} to you: {playerDat.roomPos} using {newPos}')
			#stops monster from running into you
			if not objId[locations[str(playerDat.mapPos)].room_objects[newPos[1]][newPos[0]]].blockade:
				locations[str(playerDat.mapPos)].room_objects[self.pos[1]][self.pos[0]] = ' '
				locations[str(playerDat.mapPos)].room_objects[newPos[1]][newPos[0]] = 'e'
				self.pos = newPos
			elif locations[str(playerDat.mapPos)].room_objects[newPos[1]][newPos[0]] == 'p':
				playerDat.health -= self.type.dammage
				monstersHit += 1
				totalDammage += self.type.dammage
		if monstersHit > 1:
			input(f'{monstersHit} monster/s hit you for {totalDammage} Dammage')
		elif monstersHit == 1:
			input(f'A monster hit you for {totalDammage} Dammage')

def getMonsters():
	monsters = []
	roomObj = locations[str(playerDat.mapPos)].room_objects
	for row in range(len(roomObj)):
		for letter in range(len(roomObj[row])):
			if roomObj[row][letter] == 'e':
				pos = array([letter, row])
				type = objId[roomObj[row][letter]]
				newMonster = monster(pos, type)
				monsters.append(newMonster)
	return monsters
