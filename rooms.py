from roomStructure import Room, locations

roomDat = []

#test room

test = Room('test')
locations['[0 0 0]'] = test

def newGameRooms():
	test.room_objects = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['w', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', 'w'], ['w', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', ' ', ' ', ' ', 'w', 'w'], ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', 'w'], ['w', ' ', ' ', ' ', 'e', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w', 'w'], ['w', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', ' ', ' ', 'w'], ['w', 'w', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']]
def saveRooms():
    roomDat.append(test.room_objects)
    return roomDat

def loadRooms(data):
    test.room_objects = data[0]