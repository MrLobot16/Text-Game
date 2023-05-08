from roomStructure import Room, locations

roomDat = []

#test room

test = Room('test')
test.room_objects = [['w', 'w', 'w', 'w', 'w'], ['w', ' ', 'p', ' ', 'w'], ['w', ' ', ' ', ' ', 'w'], ['w', 'w', 'w', 'w', 'w']]
locations['[0 0 0]'] = test

def saveRooms():
    roomDat.append(test.room_objects)
    print(roomDat)
    return roomDat

def loadRooms(data):
    print(data)
    test.room_objects = data[0]