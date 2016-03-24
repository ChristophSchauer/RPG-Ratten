from sys import exit

# defining speech outputs
prompt = "What do you do?\n>>>"
correct_answers = "Please use the numbers given for the action you want to do."

# dictionaries for character, inventory, chapters
char = {"Name": "Hero", "Clothing": "Rags", "Wound": 0}
invent = {"Fork_Key": False, "Torch": 0, "Knife": False}
l_door = {"Fork_Key": False}
chap1 = {"Cell_Room": 0, "Corridor1": 0, "Intersection1": 0, "Store_Room": 0, "Corridor2": 0, "Cellar_Door": 0}


import chapter1


(char, invent, l_door, chap1) = chapter1.run(char, invent, l_door, chap1)
print "This is the end of the first chapter. It will be continued soon.\n"

print "Debug Status:"
print "Char-stats", char
print "Inventory", invent
print "Chapter1-stats", chap1
print "Locked-door-stats", l_door

raw_input("\n\npress any key to exit")
exit()