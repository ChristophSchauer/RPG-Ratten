# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version : 0.1

History:
[2016.03.24, CS]: initial setup; put in all the functions of the main_RPG;
"""

def showInstructions():
    # print a main menu and the commands
    print("RPG Game")
    print("========")
    print("commands:")
    print("'exit'")
    print("'status'")
    print("'go [direction]'")
    print("'get [item]'")
    print("'fight [person]'")
    print("'drop [item]'")
    
def showStatus(currentRoom, rooms, turn, inventory):
    # print the player's current status
    print("---------------------------")
    print("you are in the " + rooms[currentRoom]["name"])
    # print the current inventory
    print("inventory: " + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print("you see: " + str(rooms[currentRoom]["item"]))
    # print POI if there is one
    if "person" in rooms[currentRoom]:
        print("you see: " + rooms[currentRoom]["person"])
        if rooms[currentRoom]["person"] == "princess":
            print("you won the game!")
            print("you played " + str(turn) + " turn(s)")
    print("---------------------------")
    

                    
def generate_char():
    playerstatus_dummy = {
                        "name"      : [],
                        "clever"    : [],
                        "social"    : [],
                        "strong"    : [],
                        "fast"      : [],
                        "life"      : [],
                        "tricks"    : [],
                        "talents"   : [],
                        "pack"      : [],
                        "proscons"  : []
                    }    
    
    print("Name your Hero please:")
    playerstatus_dummy["name"] = input(">")

    value = 0
    while (value != 8):
        value = 0
        print("you can distribute 8 points onto the following 4 attributes:\n")
        print("clever, social, strong, fast")
        print("seperate them by coma (eg:2,2,3,1)")
        data = input(">")
        data = data.split(sep= ",")
        for index in range(4):
            value = value + int(data[index])
        if value != 8:
            print("you distributed the values false")
        else:
            playerstatus_dummy["clever"] = int(data[0])
            playerstatus_dummy["social"] = int(data[1])
            playerstatus_dummy["strong"] = int(data[2])
            playerstatus_dummy["fast"] = int(data[3])
            playerstatus_dummy["life"] = int(data[2])*3
    return(playerstatus_dummy)

