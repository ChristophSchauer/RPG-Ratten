import functions

prompt = "What do you do?\n>>>"
correct_answers = "Please use the numbers given for the action you want to do."
# dicts initiate
char = {}
invent = {}
l_door = {}
chap1 = {}
chapter = {"Chapter": True, "Room": 1}

# chapter run function: dicts update and room-loop
def run(c_char, c_invent, c_l_door, c_chap1):
	char.update(c_char)
	invent.update(c_invent)
	l_door.update(c_l_door)
	chap1.update(c_chap1)
	print "." * 20
	print "This is my first Text-Adventure, thx for testing."
	print "." * 20
	print "Name your Hero please:"
	char["Name"] = raw_input(">>> ")
	print "You named your hero: %s" % char["Name"]
	print "." * 20
# could be solved better and shorter ... lets's see	
	while chapter["Chapter"] == True:
		if chapter["Room"] == 1:
			cell_room()
		elif chapter["Room"] == 2:
			corridor1()
		elif chapter["Room"] == 3:
			intersection1()
		elif chapter["Room"] == 4:
			store_room()
		elif chapter["Room"] == 5:
			corridor2()
		elif chapter["Room"] == 6:
			cellar_door()
		
	return(char, invent, l_door, chap1)

	
# Cell-Room function... where the fun begins (room 1)
def cell_room():
# check for re-entry of the room and print aproporiate lines
	if chap1["Cell_Room"] == 0:
		print "\nYou wake up in a dark room. The walls are made of thick, cold stone."
		print "You bear only some ragged clothes you don't recognise."
		print "Your head feels a little dizzy and there is barely enough light to see."
		print "The floor is covered with straw and you can make out a wooden door in one of the walls."
		chap1["Cell_Room"] += 1
	elif chap1["Cell_Room"] >= 1 and invent["Torch"] == 0:
		print "You return to the cell, nothing seems to have changed."
	else:
		print "You return to the cell once again."
		print "Something on the wall seems different than the first time."

# start choice selection for room actions:
	while True:
		print "You can go to the door (1), examine the room (2) or shout for help (3)."
		choice = raw_input(prompt).strip()
# action selection starts here with leaving the room via locked door	
		if choice == "1":
			r_val = functions.locked_door("Fork_Key", l_door, invent)
			if r_val == 1:
				chapter["Room"] = 2
				return
			else:
				print "You are back in the Cell."
# second choice to search the room				
		elif choice == "2" and not invent["Fork_Key"]:
			print "You get a grasp at the size of the room and in one corner you stumble upon a hand of a skeleton."
			print "Within the clenched fist u can see a fork shaped to the form of a key."
			print "You can take the key (1) or leave it be (2)."
			key_choice = raw_input(prompt).strip()
# take the key or not				
			if key_choice == "1":
				print "You wrench the key from the dead fingers and stand back up.\n"
				invent["Fork_Key"] = True
			elif key_choice == "2":
				print "You return to the room.\n"
			else:
				print correct_answers
# rest of the things to do		
		elif choice == "2" and invent["Fork_Key"] and invent["Torch"] == 0:
			print "There is nothing more to find in here.\n"
# easter-egg
		elif choice == "2" and invent["Fork_Key"] and invent["Torch"] >= 1:
			print "Upon examining the room under the flickering light of the torch you aproach the rear wall."
			print "Etched into the stone you can make out the words:"
			print "The Cake Is A Lie!\n"
# shout option
		elif choice == "3":
			print "There is no response whatsoever, just your voice echoing in your mind.\n"
		else:
			print correct_answers
	
# corridor1 (room 2)	
def corridor1():
# set previous door as unlocked
	l_door["Fork_Key"] = True
# check for re-entry of the room and print aproporiate lines
	if chap1["Corridor1"] == 0:
		print "You find yourself in a corridor with just one dim flickering torch on the wall."
		print "Do you take the torch (1) or do you stay in the dark (2)?"
# first action bound to first entry of the corridor	
		choice = raw_input(prompt).strip()
		if choice == "1":
			invent["Torch"] += 1
			chap1["Corridor1"] += 1
			print "You manage to cautiously take the torch from its mounting.\n"
		elif choice == "2":
			print "You stare a little into the light but decide not to take the torch.\n"
		else:
			print correct_answers
# end of first entry action
		print "You can head on (1) or return back into the cell (2)."
	elif chap1["Corridor1"] == 1:
		print "You stand in the corridor again."
		print "You can head on (1) or return back into the cell (2)."
	else:
		print "You stand in the corridor leading from the cell to the first intersection."
		print "You can go to the intersection (1), or into the cell (2)."
# action selection for the room starts here.
	while True:
		choice = raw_input(prompt).strip()
# choice to go on with torch in hand		
		if choice == "1" and invent["Torch"] >= 1:
			print "You easily find your way along the walls and avoid the open sewer hatch until you come to an intersection.\n"
			chap1["Corridor1"] += 1
			chapter["Room"] = 3
			return
# choice no torch in hand		
		elif choice == "1" and invent["Torch"] == 0:
			functions.dead("You stumble onwards and fall into an open sewer hatch.")
# return to locked door (key name, door-status, inventory)		
		elif choice == "2":
			r_val = functions.locked_door("Fork_Key", l_door, invent)
			if r_val == 1:
				chapter["Room"] = 1
				return
			else:
				print "You are back in the Corridor."
				return
		else:
			print correct_answers

# intersection 1 (room 3)
def intersection1():
	chap1["Intersection1"] += 1
	print "\nYou reach a dark corner at the end of the corridor."
	print "As you peek around the corner cautiously you can see another dark corridor."
	print "A small door in one of the walls jumps your eyes."
# start room loop	
	while True:
		print "You can go into the corridor leading away from the cell (1),"
		print "you can try the door (2) or go back towards the cell (3)."
		choice = raw_input(prompt).strip()
# choice to head onwards		
		if choice == "1":
			chapter["Room"] = 5
			return
# choice to go into room via normal door
		elif choice == "2":
			re_val = functions.door()
			if re_val == 1:
				chapter["Room"] = 4
				return
			else:
				print "You are back at the dark corner."
# chioce to go back		
		elif choice == "3":
			chapter["Room"] = 2
			return
		else:
			print correct_answers

# store room (room 4)		
def store_room():
	chap1["Store_Room"] += 1
	print "Upon stepping into the room you discover shelves on the walls under a thick layer of cobwebs and dirt."
	print "Open chests stand to one side of the room with broken locks."
# start room loop until u exit the room (choice 2 - return)	
	while True:
		print "You can search the room (1) or leave (2)."
		choice = raw_input(prompt).strip()
# first choice if u have not taken anything yet		
		if choice == "1" and char["Clothing"] != "Merchant":
			print "You discover a Tuniq in a dark green color and a pair of black trousers."
			print "The clothes are not yours but still better than the rags you are wearing."
			print "As you step closer a big rat jumps from one of the upper shelves as to defend her possessions."
			print "The rat stares at you with fiercely glowing eyes."
			print "Do you dare take the clothes (1), take a swing for the rat (2),"
			print "wave your torch at the rat (3) or leave it be (4)?"
# the rat problem with 4 choices and 7 possibilities			
			clothes_rat = False
			rat = True
			while clothes_rat == False:
				choice = raw_input(prompt).strip()
				if choice == "1" and rat:
					print "The rat jumps at your outreaching hand, bites and leaves a bleeding wound."
					char["Wound"] += 1
					if char["Wound"] >= 5:
						functions.dead("Your wounds got too severe and you bled to death.")
				elif choice == "1" and not rat:
					print "You take the Clothes, put 'em on and return to the room."
					char["Clothing"] = "Merchant"
					clothes_rat = True
				elif choice == "2" and rat:
					print "You try to hit the rat, but it lashes out quicker and bites you leaving a bleeding wound."
					char["Wound"] += 1
					if char["Wound"] >= 5:
						functions.dead("Your wounds got too severe and you bled to death.")
				elif choice == "2" and not rat:
					print "There is no more rat here to hit."
				elif choice == "3" and rat:
					print "You singe some of its whiskers and it runs away through a hole in the wall."
					rat = False
				elif choice == "3" and not rat:
					print "There is no more rat to wave your torch at."
				elif choice == "4":
					print "You return to the room."
					clothes_rat = True
				else:
					print correct_answers
# first choice for room	when u have taken the clothes
		elif choice == "1" and char["Clothing"] == "Merchant":
			print "There is nothing more to find in this room."
# second choice to leave the room
		elif choice == "2":
			r_val = functions.door()
			if r_val == 1:
				chapter["Room"] = 3
				return
			else:
				print "You are back in the room."
		else:
			print correct_answers

# corridor 2 (room 5)			
def corridor2():
	chap1["Corridor2"] += 1
	print "\nThe walls of this corridor are lined with moss, fed by some small driplets of water from the ceiling."
	print "Taking cautious steps as you head on you stop at a small hole in the wall where some bricks have collapsed."
	while True:
# if you have not taken the knife yet:	
		if not invent["Knife"]:
			print "You see something reflecting the light of your torch inside the hole."
			print "You can take a closer look in the hole (1), walk back to the corner (2) or head to the end of the corridor (3)."
			choice = raw_input(prompt).strip()
			if choice == "1":
				print "As you take a closer look at the alluring reflection you see a small blade."
				print "Guarding the knife is a black snake that has already detected you."
# the knife and the snake:				
				snake = True
				knife = False
				while knife == False:
					print "Do you take the knife (1), scare away the snake with the torch (2), or leave it be (3)?"
					choice = raw_input(prompt).strip()
					if choice == "1" and snake:
						print "You try to take the dagger, you can grab it."
						print "But as you pull your hand back the snake shoots out and bites."
						functions.dead("The poison quickly shoots through your body, you feel dizzy and drop dead.")
					elif choice == "1" and not snake:
						print "You take the knife, put it in your waistband and step back.\n"
						knife = True
						invent["Knife"] = True
					elif choice == "2" and snake:
						print "The snake hisses but disappears in the dark."
						snake = False
					elif choice == "2" and not snake:
						print "The snake is already gone."
					elif choice == "3":
						print "You step back from the hole in the wall.\n"
						knife = True
					else:
						print correct_answers
# other choices but closer look
			elif choice == "2":
				chapter["Room"] = 3
				return
			elif choice == "3":
				chapter["Room"] = 6
				return
			else:
				print correct_answers
# if u have the knife there are just two options	
		elif invent["Knife"]:
			print "There is nothing more to discover in the hole in the wall."
			while True:
				print "You can go back to the corner (1) or head to the end of the corridor (2)."
				choice = raw_input(prompt).strip()
				if choice == "1":
					chapter["Room"] = 3
					return
				elif choice == "2":
					chapter["Room"] = 6
					return
				else:
					print correct_answers

#room 6 - cellar exit	
def cellar_door():
	chap1["Cellar_Door"] += 1
	print "\nYou stand at the first rundle of a wooden ladder."
	print "It leads to a hatch some feet above your head."
	print "Do you climb the ladder (1) or walk back (2)?"
	choice = raw_input(prompt).strip()
	if choice == "2":
		chapter["Room"] = 5
		return
	elif choice == "1":
		print "You try each rundle of the ladder carefully and reach the hatch."
	else:
		print correct_answers
	print "Upon reaching the last steps you try to push the hatch open. Seem you would have to work on that."
	
	door_hits = 0
	while door_hits < 5:
		print "You could try to break the center planks that look a little rotten (1), step back down (2) or call through the hatch (3)."
		choice = raw_input(prompt).strip()
		if choice == "1" and door_hits <= 1:
			door_hits += 1
			print "You hit the planks with you elbow. You can hear a little cracking.\n"
		elif choice == "1" and door_hits == 2:
			print "This time you can feel the plank almost giving in under the hit.\n"
			door_hits += 1
		elif choice == "1" and door_hits == 3:
			print "The plank breaks and you can reach through the hatch with your hand."
			print "You feel the bolt locking the hatch and pull it out of it's socket."
			print "Slowly opening the hatch you step out of the darkness and into a moonlit night."
			print "You sense the fresh air and inhale deeply to calm you down a little."
			print "Then you realize you are standing in a back-alley of a town, that does not seem familiar.\n\n"
			chapter["Chapter"] = False
			return
		elif choice == "2":
			print "You step back down from the ladder.\n"
			return
		elif choice == "3":
			print "With a deep breath taken you shout: \"Help me!\""
			print "And after what seemed only seconds to you, the hatch is being opened."
			print "A towering stone statue looks right into your eyes. 'THERE YOU ARE!'"
			functions.dead("Shocked with what you saw you loose grip of the ladder, drop to the ground head first and snap your neck.")
		else:
			print correct_answers