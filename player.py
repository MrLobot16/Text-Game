from roomStructure import Room, locations

OPTIONS = ["q", "quit", "h", "help", "?"]

def quit():
		save = input("Would you like to save? y/n\n").lower()
		if save in ["y", "yes"]:
			print("Saving comming soon")
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

def menu():
	choice = ''
	while choice not in OPTIONS:
		choice = input("What would you like to do?\n").lower()
		if choice not in OPTIONS:
			print("\nInvalid command, please try again.\n? or help for list of commands\n")
	
	#quit game
	if choice in OPTIONS[0:2]:
		choice = quit()



