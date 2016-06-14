#Rules for IF STATEMENTS:
# 1) every if must have an else
# 2) if else doesnt run, use 'die' funciton that prints errors
# 3) 1 deep if statement nest better than 2+ nested
# 4) if statement like paragraph : if-elif-else group = sentences
# 5) boolean tests simple; complex = calculation move to simple variables
#
#Rules for loops:
# 1) while-loop only for forever
# 2) for-loops if fixed or limited number of things to loops
#
# Debug tips:
# 1) print variables at points in program to see where things are going wrong
# 2) code a little, fix a little

from sys import exit

def front_door():
	print ""

def living_room():
	print "You enter an entry foryer."
	print "You see a black cat and a brown dog."
	print "What do you go up to first?"

	choice = raw_input("> ")

	if choice == "cat":
		cat()
	elif choice == "dog":
		dog()
	else:
		dead("You walk away quietly.")

def cat():
	print "You walk up to the cat."
	print "It glowers at you dubiously."
	print "What do you do?"

	choice = raw_input("> ")

	if "pet" in choice:
		dead("The cat did not approve of your pets. It scratches you and you die.")
	else:
		dead("The cat hisses and runs away.")

def dog():
	print "You walk up to the dog."
	print "It happily wags it's tail at you."
	print "What do you do?"

	choice = raw_input("> ")

	if "pet" in choice:
		friend("The dog licks your hand.")
	elif "treat" in choice:
		friend("The dog seems thankful.")
	else:
		dead("The dog seems bored by you.")

def start():
	print "You find yourself in front of a house."
	print "The front door is cracked. Do you enter (yes/no)?"

	choice = raw_input("> ")

	if choice == "yes":
		living_room()
	elif choice == "no":
		run_away()
	else:
		dead("You walk away quietly.")

def friend(why):
	print why, "How nice. You made a friend!"
	exit(0)

def dead(why):
	print why, "Good job!"
	exit(0)


start()
