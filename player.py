from roomStructure import Room, locations, objId
import shelve
from items import itemlist, weapon, empty
import render
from numpy import array
from rooms import roomDat
import rooms

OPTIONS = ["exit", "h", "help", "?", "w", "a", "s", "d", " ", "q", "e", "1", "2", "3", "4", "5"]
GAMEHELP = '''
"exit" ------------------ Exit game
"h"/"help"/"?" ---------- Open help menu
"w", "a", "s", "d" ------ Move/Turn direction
"Space" ----------------- Attack/Use Item
"e" --------------------- Interact
"q" --------------------- Drop Item
"1-5" ------------------- Select Inventory
'''
directions = {'w':'^', '^':array([0, -1]),
'a':'<', '<':array([-1, 0]),
's':'v', 'v':array([0, 1]),
'd':'>', '>':array([1, 0]),}

class player:
	def __init__(self):
		self.reset()
	
	def reset(self):
		self.slot = 0
		self.heal = 1
		self.health = 100
		self.maxHealth = 100
		self.mapPos = array([0, 0, 0])
		self.roomPos = array([2, 1])
		self.dir = '^'
		self.save = ''
		self.play = True
		self.facing = ' '
		self.inventory = [itemlist[1], itemlist[2], itemlist[0], itemlist[0], itemlist[0]]
		self.score = 0

	def getFacing(self):
		roomDat = locations[str(playerDat.mapPos)].room_objects
		newPos = self.roomPos + directions[self.dir]
		print(roomDat[newPos[1]][newPos[0]])
		self.facing = roomDat[newPos[1]][newPos[0]]

playerDat = player()


def saveGame():
	with open("saves.txt", "r") as file:
		saves = []
		for line in file:
			print(line)
			saves.append(line)
		print(saves)
	with open("saves.txt", "a") as file:
		if playerDat.save+'\n' not in saves:
			file.write(f"{playerDat.save}\n")
	s = shelve.open(f'{playerDat.save}.dat')
	s['playerDat'] = [playerDat.slot, playerDat.health, playerDat.maxHealth, playerDat.mapPos, playerDat.roomPos, playerDat.dir, playerDat.save, playerDat.inventory, playerDat.score, None]
	s['roomDat'] = rooms.saveRooms()
	s.sync()
	s.close()

def move(dir):
	newPos = playerDat.roomPos + directions[directions[dir]]
	if playerDat.dir == directions[dir]:
		objId[playerDat.facing].runInto(newPos)
		newPos = playerDat.roomPos + directions[directions[dir]]
		gameStep()
		render.render()
	else:
		playerDat.dir = directions[dir]
		playerDat.getFacing()
		render.render()

def attack():
	if playerDat.inventory[playerDat.slot].type == 'weapon':
		input(playerDat.inventory[playerDat.slot].hitText[playerDat.facing])
		if playerDat.facing == 'e':
			attackPos = playerDat.roomPos + directions[playerDat.dir]
			locations[str(playerDat.mapPos)].room_objects[attackPos[1]][attackPos[0]] = ' '
			playerDat.score += 1
			
	else:
		input(input(empty.hitText[playerDat.facing]))
	render.render()
	gameStep()

def quit():
	save = input("Would you like to save? y/n\n").lower()
	if save in ["y", "yes"]:
		saveGame()
		playerDat.play = False
	elif save in ["n", "no"]:
		confirm = input("Are you sure you want to quit without saving?\n")
		if confirm in ["y", "yes"]:
			print("Goodbye")
			playerDat.play = False
		else:
			print("Game not Quit")
	else:
		print("Invalid command\nGame not Quit\n")

def gameStep():
	from enemy import getMonsters, spawnMonster
	playerDat.health += playerDat.heal
	if playerDat.health > playerDat.maxHealth:
		playerDat.health = playerDat.maxHealth
	monsters = getMonsters()
	for monster in monsters:
		monster.enemyMove()
	spawnMonster()
	playerDat.getFacing()



def main(name):
	playerDat.save = name
	choice = ''
	render.render()
	playerDat.play = True
	while playerDat.play:
		while choice not in OPTIONS:
			choice = input("What would you like to do?\n").lower()
			if choice not in OPTIONS:
				print("\nInvalid command, please try again.\n? or help for list of commands\n")
	
		#Gameplay loop
		if choice in OPTIONS[1:4]: #Help
			print(GAMEHELP)
			input()
		elif choice in OPTIONS[4:8]: #Move
			move(choice)
		elif choice in OPTIONS[8:9]: #attack
			attack()
		elif choice in OPTIONS[11:16]: #Inventory
			playerDat.slot = int(choice)-1
			render.render()
		if choice == 'exit': #exit Game
			quit()
		else:
			choice = ''
		if playerDat.health <= 0:
			input("Game over!")
			playerDat.play = False
