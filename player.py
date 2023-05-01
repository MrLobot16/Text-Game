from roomStructure import Room, locations
import shelve

OPTIONS = ["exit", "h", "help", "?", "w", "a", "s", "d", " ", "q", "e", str(range(1,6))]
GAMEHELP = '''
"exit" ------------------ Exit game
"h"/"help"/"?" ---------- Open help menu
"w", "a", "s", "d" ------ Move/Turn direction
"Space" ----------------- Attack/Use Item
"e" --------------------- Interact
"q" --------------------- Drop Item
"1-5" ------------------- Select Inventory
'''

def quit(file):
		save = input("Would you like to save? y/n\n").lower()
		if save in ["y", "yes"]:
			save(file)
			return 'q'
		elif save in ["n", "no"]:
			confirm = input("Are you sure you want to quit without saving?\n")
			if confirm in ["y", "yes"]:
				print("Goodbye")
				return 'q'
			else:
				return ''
		else:
			print("Invalid command")
			return ''

def save(file):
	print(f"Saving comming soon for \"{file}\"")

def move(dir):
	pass

def menu():
	choice = ''
	while choice not in OPTIONS:
		choice = input("What would you like to do?\n").lower()
		if choice not in OPTIONS:
			print("\nInvalid command, please try again.\n? or help for list of commands\n")
	
	#quit game
	if choice in OPTIONS[0:1]:
		choice = quit()
	elif choice in OPTIONS[1:4]:
		print(GAMEHELP)
	elif choice in OPTIONS[4:8]:
		move(choice)

