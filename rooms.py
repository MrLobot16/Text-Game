from roomStructure import Room, locations

def loadRooms():
#test room
	test = Room()
	test.room_objects = [['w', 'w', 'w', 'w', 'w'], ['w', ' ', 'p', ' ', 'w'], ['w', ' ', ' ', ' ', 'w'], ['w', 'w', 'w', 'w', 'w']]
	locations['[0 0 0]'] = test
loadRooms()