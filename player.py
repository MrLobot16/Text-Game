from roomStructure import Room, locations
import shelve
from items import itemlist
import render

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
def save():
	pass


def quit():
		save = input("Would you like to save? y/n\n").lower()
		if save in ["y", "yes"]:
			print("Saving comming soon")
			return 'exit'
		elif save in ["n", "no"]:
			confirm = input("Are you sure you want to quit without saving?\n")
			if confirm in ["y", "yes"]:
				print("Goodbye")
				return 'exit'
			else:
				print("Game not Quit")
				return ''
		else:
			print("Invalid command\nGame not Quit\n")
			return ''



def move(dir):
	pass

class player:
    def __init__(self):
        self.slot = 2
        self.health = 100
        self.maxHealth = 100
        self.inventory = [itemlist[1], itemlist[2], itemlist[0], itemlist[0], itemlist[0]]
playerDat = player()

def menu():
	choice = ''
	while choice not in OPTIONS[0:1]:
		while choice not in OPTIONS:
			choice = input("What would you like to do?\n").lower()
			if choice not in OPTIONS:
				print("\nInvalid command, please try again.\n? or help for list of commands\n")
	
		#Gameplay loop
		
		if choice in OPTIONS[1:4]:
			print(GAMEHELP)
			input()
		elif choice in OPTIONS[4:8]:
			move(choice)
		elif choice in OPTIONS[11:16]:
			playerDat.slot = int(choice)
			render.render()
		if choice == 'exit':
			choice = quit()
		else:
			choice = ''

menu()