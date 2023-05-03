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
		self.type = 'type'
		self.sprite = ''

wall = obj('w')
wall.sprite = '▓'

empty = obj(' ')
empty.sprite = '·'

player = obj('p')
player.sprite = '^'

obj = {"w": wall,
" ": empty,
"p": player
}

class Room():
	'''Room Object'''
	def __init__(self, name):
		self.room_structure = []#room object locations
		self.name = name#room name
