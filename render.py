
def render():
	from player import playerDat
	from roomStructure import locations, obj
	#Displays inventory
	screen = '║'
	for x in range(1,6):
		if playerDat.slot == x:
			screen += ' -───────- ║'
		else:
			screen += '           ║'
	#Splits Sprites up into lines
	itemSprite = []
	for item in playerDat.inventory:
		itemSprite.append(item.sprite.split("\n"))

	#put split sprites in order
	itemLine = '\n'
	for x in range(3):
		itemLine += '║'
		for y in range(5):
			if playerDat.slot-1 == y:
				itemLine += ' |'
			else:
				itemLine += '  '
			itemLine += itemSprite[y][x]
			if playerDat.slot-1 == y:
				itemLine += '| ║'
			else:
				itemLine += '  ║'
		itemLine += '\n'
	screen += itemLine + "║"
	for x in range(1,6):
		if playerDat.slot == x:
			screen += ' -───────- ║'
		else:
			screen += '           ║'
	screen += '\n'
	room = ''
	roomObj = locations[str(playerDat.mapPos)].room_objects
	for line in roomObj:
		for letter in line:
			if obj[letter].sprite != '^':
				room += obj[letter].sprite
			else:
				room += playerDat.dir
		room += '\n'
	screen += room



	print(screen)

if __name__ == "__render__":
	render()