#changes a room from text to a list

'''
key:
w = wall
space = floor
d = door
x = door w/ exit location
s = stairs
i[id] = item with id
p = player pos
e = enemy

'''


room = '''
wwwwwwwwwwwwww
w p         ww
w      e    ww
w           ww
w   e       ww
ww       e   w
ww           w
wwwwwwwwwwwwww'''

roomLines = room.split('\n')
print (roomLines)

roomList = []
for line in roomLines:
	row = []
	if line != '':
		for letter in line:
			row.append(letter)
		roomList.append(row)

print (f'Room Dat:\n{roomList}')