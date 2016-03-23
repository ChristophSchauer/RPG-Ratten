"""
Header
History:
[2016.03.23, CS]: initial setup; copy the main code from: 
                  http://usingpython.com/python-rpg-game/; insert a second and 
                  a third floor above the hall; insert items in the rooms;
                  insert enemy; insert princess;
"""
import random

def showInstructions():
    # print a main menu and the commands
    print("RPG Game")
    print("========")
    print("commands:")
    print("'go [direction]'")
    print("'get [item]'")
    print("'fight [person]'")
    print("'drop [item]'")
    
def showStatus():
    # print the player's current status
    print("---------------------------")
    print("you are in the " + rooms[currentRoom]["name"])
    # print the current inventory
    print("inventory: " + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print("you see a " + rooms[currentRoom]["item"])
    # print POI if there is one
    if "person" in rooms[currentRoom]:
        print("you see " + rooms[currentRoom]["person"])
        if rooms[currentRoom]["person"] == "princess":
            print("you won the game!")
    print("---------------------------")
    
# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other positions
rooms = {
            11:{ "name" : "hall",
                 "east" : 12,
                 "south": 13,
                 "up"   : 21,
                 "item" : "torch"},
                
            12:{ "name" : "bedroom",
                 "west" : 11,
                 "south": 14},
                
            13:{ "name" : "kitchen",
                 "north": 11,
                 "item" : "sword"},
                
            14:{ "name" : "bathroom",
                 "north": 12,
                 "item" : "soap"},
                
            21:{ "name" : "stair",
                 "east" : 22,
                 "south": 23,
                 "down" : 11,
                 "item" : "torch"},
                
            22:{ "name" : "corridor",
                 "west" : 21,
                 "south": 24,
                 "up"   : 32,
                 "item" : "torch",
                 "person": "gretchin"},
                
            23:{ "name" : "terrace",
                 "north": 21},
                
            24:{ "name" : "study",
                 "north": 22,
                 "item" : "book"},
            
            32:{ "name" : "towerroom",
                 "down" : 22,
                 "person" : "princess"}
        }
        
# start the player in room 1
currentRoom = 11

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
            
    # if they type 'fight' first
    if move[0] == "fight":
        # if the player has a sword he is better at fighting
        if "sword" in inventory:
            if(random.randint(1,6+1)>2):
                print("enemy died")
                # if the enemy died delete it from the room
                del rooms[currentRoom]["person"]
            else:
                print("you died")
        else:
            if(random.randint(1,6+1)>4):
                print("enemy died")
                # if the enemy died delete it from the room
                del rooms[currentRoom]["person"]
            else:
                print("you died")
                
    # if the player wants to drop something
    if move[0] == "drop":
        # look if the player has something to drop
        if inventory == []:
            print("you can't drop anything")
        else:
            rooms[currentRoom]["item"] = move[1]
            del inventory[inventory.index(move[1])]
            print("you dropped " + move[1] + "!")
            