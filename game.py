from rooms import loadRooms
from player import main
import shelve
import os
import string


#List of valid file name characters
valid_chars = "-_.()%s%s" % (string.ascii_letters, string.digits)

def newGame():
	valid = False
	while valid == False:
		name = input("Name File:\n")
		valid = True
		for letter in name:
			if letter not in valid_chars:
				valid = False
		if valid:
			main(name)
			with open("saves.txt", "a") as file:
				file.write(f"{name}\n")
		else:
			print(f"\"{name}\" is not a valid file name.")
	currentFile = name

def loadGame():
	pass

def deleteSave():
	with open("saves.txt", "r") as file:
		print("Current saves:\n")
		saves = []
		for line in file:
			print(line)
			saves.append(line)
		print(saves)
	delete = input("\nChoose file to delete\n")
	if delete+'\n' in saves:
		confirm = input(f"Are you sure you want to delete \"{delete}\"?\n")
		if confirm in ('y', 'yes'):
			os.remove(delete + ".dat")
			saves.remove(delete+'\n')
			with open("saves.txt", "w") as file:
				file.writelines(saves)
			print("File removed")
			input()
		else:
			print("Invalid File")





title = ('''
 ▄▄▄      ▓█████▄  ██▒   █▓▓█████  ███▄    █ ▄▄▄█████▓ █    ██  ██▀███   ▄▄▄      
▒████▄    ▒██▀ ██▌▓██░   █▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▒████▄    
▒██  ▀█▄  ░██   █▌ ▓██  █▒░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒██  ▀█▄  
░██▄▄▄▄██ ░▓█▄   ▌  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ░██▄▄▄▄██ 
 ▓█   ▓██▒░▒████▓    ▒▀█░  ░▒████▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒ ▓█   ▓██▒
 ▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
  ▒   ▒▒ ░ ░ ▒  ▒    ░ ░░   ░ ░  ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░   ░▒ ░ ▒░  ▒   ▒▒ ░
  ░   ▒    ░ ░  ░      ░░     ░      ░   ░ ░   ░       ░░░ ░ ░   ░░   ░   ░   ▒   
      ░  ░   ░          ░     ░  ░         ░             ░        ░           ░  ░
''')
choices = '''
				1 - New Game
				2 - Load Game
				3 - Delete save
				4 - Credits
				5 - Quit\n
'''

choice = '0'
while choice != '5':
	print(title)
	choice = input(choices)
	if choice == '1':
		newGame()
	elif choice == '2':
		loadGame()
	elif choice == '3':
		deleteSave()
	elif choice == '4':
		print("Game Made by Logan Haroldsen\nRoom code by Mr. Simonsen")
		input()
	elif choice == '5':
		print("Goodbye")
	else:
		print("Invalid Choice")


