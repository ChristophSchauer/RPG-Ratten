"""
Header

@author: Christoph
Version: 0.1

History:
[2016.03.23, CS]:   initial setup; copy the main code from: 
                    http://usingpython.com/python-rpg-game/; insert a second and 
                    a third floor above the hall; insert items in the rooms;
                    insert enemy; insert princess;
[2016.03.24, CS]:   insert game logic (need a key for the towerroom door) and 
                    the use of the key; insert the exit function; put every 
                    command in an own function; save playerstatus; load rooms 
                    from an external file or use the dummy file;
                    ERROR1: say the user the right counter of turns he used;
                    start with the function for the char generation;
                    generate a functions file;
                    insert the asking of the user to save his char;
                    ERROR2: thLib has an error, maybe reinstallation of python;
"""
# for random numbers
import random
import sys
# for saving and loading dictionarys
import json
import os

import functions_RPG

path_at_work = r'C:\Users\Schauer\Documents\Privat\RPG-Ratten.git\trunk'

def fct_move(parameter, currentRoom, rooms):
    # check that they are allowed wherever they want to go
    if parameter in rooms[currentRoom]:
        newRoom = rooms[currentRoom][parameter]
        # check if the door to the new room is locked
        if "property" in rooms[newRoom] and rooms[newRoom]["property"] == "locked":
            print("door locked")
            if "key" in inventory:
               print("want to use the key? [Y/N]")
               answer = input(">")
               if answer == "Y" or answer == "y":
                   print("opens the door with the key")
                   # set the current room to the new room
                   currentRoom = rooms[currentRoom][parameter]
        else:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][parameter]
    # if there is no door/link to the new room
    else:               
        print("you can't go that way!")
    return(currentRoom)
        
def fct_get(parameter, currentRoom, rooms, inventory):
    # if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and parameter in rooms[currentRoom]["item"]:
        # add the item to the inventory
        inventory += [parameter]
        # display a helpfull message
        print(parameter + " got!")
        # delete the item from the room
        del rooms[currentRoom]["item"][rooms[currentRoom]["item"].index(parameter)]
    # otherwise, if the item isn't there to get
    else:
        # tell them they can't get it
        print("can't get " + parameter + "!")
    return(inventory)
        
def fct_fight(parameter, currentRoom, rooms, inventory, turn):
    # if the player has a sword he is better at fighting
    if "sword" in inventory:
        if(random.randint(1,6+1)>2):
            print("enemy died")
            # if the enemy died delete it from the room
            del rooms[currentRoom]["person"]
        else:
            print("you died")
            print("you played " + str(turn) + " turn(s)")
            sys.exit()
    else:
        if(random.randint(1,6+1)>4):
            print("enemy died")
            # if the enemy died delete it from the room
            del rooms[currentRoom]["person"]
        else:
            print("you died")
            print("you played " + str(turn) + " turn(s)")
            sys.exit()
            
def fct_drop(parameter, currentRoom, rooms, inventory):
    # look if the player has something to drop
    if inventory == [] or inventory[inventory.index(parameter)] != parameter:
        print("you can't drop anything")
    else:
        rooms[currentRoom]["item"] += [parameter]
        del inventory[inventory.index(parameter)]
        print("you dropped " + parameter + "!")
    return(inventory)
               
def random_dice(numberdices):
    values = []
    [values.append(random.randint(1,7)) for i in range(numberdices)]
    
    return(values)

def fct_rooms():
    if os.path.exists(path_at_work + '\rooms.json'):
        with open(path_at_work + '\rooms.json') as f:
            rooms = json.load(f)
    # a dictionary linking a room to other positions
    else:
        rooms = {
                    11:{ "name" : "hall",
                         "east" : 12,
                         "south": 13,
                         "up"   : 21,
                         "item" : ["torch"]},
                        
                    12:{ "name" : "bedroom",
                         "west" : 11,
                         "south": 14,
                         "item" : ["key"]},
                        
                    13:{ "name" : "kitchen",
                         "north": 11,
                         "item" : ["sword"]},
                        
                    14:{ "name" : "bathroom",
                         "north": 12,
                         "item" : ["soap"]},
                        
                    21:{ "name" : "stair",
                         "east" : 22,
                         "south": 23,
                         "down" : 11,
                         "item" : ["torch"]},
                        
                    22:{ "name" : "corridor",
                         "west" : 21,
                         "south": 24,
                         "up"   : 32,
                         "item" : ["torch"],
                         "person": "gretchin"},
                        
                    23:{ "name" : "terrace",
                         "north": 21},
                        
                    24:{ "name" : "study",
                         "north": 22,
                         "item" : ["book"]},
                    
                    32:{ "name" : "towerroom",
                         "down" : 22,
                         "person" : "princess",
                         "property" : "locked"}
                }
    return(rooms)
               
def fct_main(currentRoom, inventory , turn, rooms):
    
    playerstatus = functions_RPG.generate_char()
    
    functions_RPG.showInstructions()
    
    # loop infinitely
    while True:
        
        functions_RPG.showStatus(currentRoom, rooms, turn, inventory)
        
        # get the player's next move
        # .split() breaks it up into a list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = input(">").lower().split()
        
        # if they type 'go' first
        if move[0] == "go":
            currentRoom = fct_move(move[1], currentRoom, rooms)
        
        # if they type 'get' first
        if move[0] == "get":
            inventory = fct_get(move[1], currentRoom, rooms, inventory)
                
        # if they type 'fight' first
        if move[0] == "fight":
            fct_fight(move[1], currentRoom, rooms, inventory, turn)
                    
        # if the player wants to drop something
        if move[0] == "drop":
            inventory = fct_drop(move[1], currentRoom, rooms, inventory)
              
        if move[0] == "status":
            print(playerstatus)
                
        if move[0] == "exit":
            print("thank you for playing")
            print("you played " + str(turn) + " turn(s)")
            print("want to save your char (y/n)?")
            decision = input(">")
            if decision == 'y' or decision == 'Y':
                print("where do you want to save your char?")
                #path = th.ui.getfile(FilterSpec='.json', DialogTitle='Select File:')
                #myfile = os.path.join(path[1],path[0])
                with open(myfile, 'w') as f:
                    json.dump(playerstatus, f)
                    print("stats saved under: " + path_at_work)      
            sys.exit()
            
        turn += 1
        
# main function
if __name__=='__main__':
    # start the player in room 1
    currentRoom = 11
    # an inventory, which is initially empty
    inventory = []
    # initialize the turns
    turn = 1
    # generate rooms
    rooms = fct_rooms()
    
    fct_main(currentRoom, inventory, turn, rooms)