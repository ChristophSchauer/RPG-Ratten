"""
Header
History:
[2016.03.23, CS]: initial setup; copy the main code from:
                  http://usingpython.com/python-rpg-game/;
"""

def showInstructions():
    # print a main menu and the commands
    print("RPG Game")
    print("========")
    print("commands:")
    print("'go [direction]'")
    print("'get [item]'")
    
def showStatus():
    # print the player's current status
    print("---------------------------")
    print("you are in the " + rooms[currentRoom]["name"])
    # print the current inventory
    print("inventory: " + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print("you see a " + rooms[currentRoom]["item"])
    print("---------------------------")
    
# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other positions
rooms = {
            1:{ "name" : "hall",
                "east" : 2,
                "south": 3},
                
            2:{ "name" : "bedroom",
                "west" : 1,
                "south": 4,
                "item" : "sword"},
                
            3:{ "name" : "kitchen",
                "north" : 1},
                
            4:{ "name" : "bathroom",
                "north" : 2}
        }
        
# start the player in room 1
currentRoom = 1

showInstructions()

# loop infinitely
while True:
    
    showStatus()
    
    # get the player's next move
    # .split() breaks it up into a list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = input(">").lower().split()
    
    # if they type 'go' first
    if move[0] == "go":
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if there is no door/link to the new room
        else:
            print("you can't go that way!")
    
    # if they type 'get' first
    if move[0] == "get":
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            # add the item to the inventory
            inventory += [move[1]]
            # display a helpfull message
            print(move[1] + " got!")
            # delete the item from the room
            del rooms[currentRoom]["item"]
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print("can't get " + move[1] + "!")