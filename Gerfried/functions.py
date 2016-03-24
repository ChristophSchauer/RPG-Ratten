prompt = "What do you do?\n>>>"
correct_answers = "Please use the numbers given for the action you want to do."

l_door = {}
invent = {}

# locked door function...
def locked_door(special_key, c_l_door, c_invent):
	l_door.update(c_l_door)
	invent.update(c_invent)
	print "\nYou stand in front of the door."
	if not l_door[special_key]:
		print "It seems to be locked as you try the handle."
	else:
		print "Since you unlocked it previously you can walk right through."
	print "You can try to open it (1), walk through (2) or step back (3)."
# door action selection sequence ...
	while True:
		choice = raw_input(prompt).strip()
		if choice == "1" and invent[special_key] and not l_door[special_key]:
			print "You unlock the door."
			l_door[special_key] = True
		elif choice == "1" and not invent[special_key]:
			print "You don't have the right key."
		elif choice == "1" and l_door[special_key]:
			print "The door is already unlocked."
		elif choice == "2" and l_door[special_key]:
			print "You walk through the door.\n"
			return(1)
		elif choice == "2" and not l_door[special_key]:
			print "You need to unlock the door first."
		elif choice == "3":
			return(2)
		else:
			print correct_answers

# simple doors
def door():
	print "\nYou stand in front of the door. As you try the handle it springs open."
	print "You can walk through the door (1) or step back from it (2)."
	while True:
		choice = raw_input(prompt).strip()
		if choice == "1":
			print "You walk through the door.\n"
			return(1)
		elif choice == "2":
			print "You step back from the door.\n"
			return(2)
		else:
			print correct_answers

# function to print the cause of death and exit game.	
def dead(why):
	print "\n", why, "Good Job!\n"
	raw_input("\n\npress any key to exit")
	exit(0)