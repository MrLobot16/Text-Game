from roomStructure import Room, locations

def loadRooms():
#starting room
	start = Room()
	start.room_items.append('key')
	start.usable_items['stick'] = "You use the stick to move the mound of dirt."
	start.allowed_movements.append('east')
	start.descriptions[(('key',),("stick",))] = "Entry: There's a mound of dirt."
	start.descriptions[(('key',),())] = "Entry: An uncovered key with scattered dirt around it and a used stick."
	start.descriptions[((),())] = "Entry: Scattered dirt and a used stick."
	locations[(0,0,0)]=start