#changes a room from text to a list

'''
key:
w = wall
space = floor
d = door
x = door w/ exit location
s = stairs
i = item
p = player pos

'''


room = '''
wwwww
w   w
w   w
wwwww'''

roomLines = room.split('\n')
print (roomLines)

roomList = []
for line in roomLines:
	row = []
	if line != '':
		for letter in line:
			row.append(letter)
		roomList.append(row)

print (roomList)