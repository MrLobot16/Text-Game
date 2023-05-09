from numpy import array
#numpy.array() makes a matrix so I can do matrix math
MOVEMENT = {"north":array([1,0,0]),
			"south":array([-1,0,0]),
			"east":array([0,1,0]),
			"west":array([0,-1,0]),
			"up":array([0,0,1]),
			"down":array([0,0,-1])}
locations = {}
class obj():
	def __init__(self, type):
		self.type = type
		self.sprite = ''
		self.dammage = 0
		self.blockade = False
		self.moveText = ''
	def runInto(self, newPos, ):
		from player import playerDat
		playerDat.health -= self.dammage
		if self.blockade == False:
			locations[str(playerDat.mapPos)].room_objects[newPos[1]][newPos[0]] = 'p'
			locations[str(playerDat.mapPos)].room_objects[playerDat.roomPos[1]][playerDat.roomPos[0]] = ' '
			playerDat.roomPos = newPos
		if self.moveText != '':
			input(self.moveText)

wall = obj('w')
wall.sprite = '▓'
wall.blockade = True
wall.moveText = 'You scratch your head after running into the wall.'

empty = obj(' ')
empty.sprite = '·'

player = obj('p')
player.sprite = '^'
player.blockade = True

enemy = obj('e')
enemy.sprite = 'M'
enemy.blockade = True
enemy.dammage = 5
enemy.moveText = "Ouch! this creature bit you!"

#Dictionary of objects and their counterpart
objId = {"w": wall,
" ": empty,
"p": player,
"e": enemy
}

class Room():
	'''Room Object'''
	def __init__(self, name):
		self.room_structure = []#room object locations
		self.name = name#room name
