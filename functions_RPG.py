# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version : 0.1

History:
[2016.03.24, CS]:   initial setup; put in all the functions of the main_RPG;
                    ERROR1: say the user the right counter of turns he used;
                    start with the function for the char generation;
                    generate a functions file;
                    insert the asking of the user to save his char;
                    ERROR2: thLib has an error, maybe reinstallation of python;
[2016.03.25, CS]:   insert the rest of the functions; insert the random_dice 
                    function;
                    start with the rat fighting system function;
                    ERROR2 solved: put the needed functions into the 
                    functions_RPG.py;
                    ERROR1: solved: the turn counter has to inerate with 1 and 
                    not with itself;
                    implement random_dice function with any number of dices, 
                    output and an exclusion criteria;
                    ERROR3: starting a fight the following message appears:
                    'numpy.float64' object cannot be interpreted as an integer;
                    ERROR3: solved: change the type of the fight_array from
                    float64 to int32;
                    ERROR4: problem with the enemy's turn in fct_fight_rat;                    
[2016.03.29, CS]:   change the char generation; check, that the player has not
                    more than 3 points on each attribute;
                    ERROR4: solved: checked the if clauses for the fights;
                    changed the damage_calculation: the attack values of player
                    and enemy are passed;
[2016.03.30, CS]:   ERROR7: change random_dice: add the checking for zero 
                    dices, the function random_dice function has to check for 
                    the number of dices which are thrown and adjust the output 
                    accordingly;
                    ERROR7: solved;
                    exit() changed to raise SystemExit;
                    changed the rooms-dictionary: all the persons must be 
                    defined with 0 or 1, if the player can fight against them 
                    or not;
                    changed the move-funtion and the rooms-dictionary: now all
                    doors must be defined with 'locked' or 'opened';
[2016.03.31, CS]:   changed the imported libraries to save memory;
[2016.04.06, CS]:   ERROR#14: when the map should be loaded, there is a problem 
                    with y/j, maybe english and german layout of Keyboard;
                    ERROR#14: solved: also answer for the z from english
                    keyboards;
[2016.04.11, MG]:   ISSUE#13: Adjacent rooms are now shown, TODO: Hidden room 
                    option;
[2016.04.11, CS]:   ISSUE#16: changed all the naming of the interaction in
                    english;
                    ISSUE#18: changed the call of tkinter;
"""
import parameter_RPG

from random import randint
from os import path
import json

import sys

if sys.version_info.major == 3:
    # Python 3.x
    import tkinter as tk
    import tkinter.filedialog as tkf
else:
    # Python 2.x
    import Tkinter as tk
    import tkFileDialog as tkf

from numpy import ones

from time import sleep

def getfile(FilterSpec='*', DialogTitle='Select File: ', DefaultName=''):
    '''
    taken from Thomas Haslwanter
    Selecting an existing file.
    
    Parameters
    ----------
    FilterSpec : query-string
        File filters
    DialogTitle : string
        Window title
    DefaultName : string
        Can be a directory AND filename
    
    Returns
    -------
    filename :  string
        selected existing file, or empty string if nothing is selected
    pathname:   string
        selected path, or empty string if nothing is selected
    
    Examples
    --------
    >>> (myFile, myPath) = thLib.ui.getfile('*.py', 'Testing file-selection', 'c:\\temp\\test.py')
    
    '''
    
    root = tk.Tk()
    root.withdraw()
    fullInFile = tkf.askopenfilename(initialfile=DefaultName,
            title=DialogTitle, filetypes=[('all files','*'), ('Select',
                FilterSpec)])
    
    # Close the Tk-window manager again
    root.destroy()
    
    if not path.exists(fullInFile):
        return (0, 0)
    else:
        print('Selection: ' + fullInFile)
        dirName = path.dirname(fullInFile)
        fileName = path.basename(fullInFile)
        return (fileName, dirName)
        
def savefile(FilterSpec='*',DialogTitle='Save File: ', DefaultName=''):
    '''
    taken from Thomas Haslwanter
    Selecting an existing or new file:
    
    Parameters
    ----------
    FilterSpec : string
        File filters.
    DialogTitle : string
        Window title.
    DefaultName : string
        Can be a directory AND filename.
    

    Returns
    -------
    filename : string
        Selected file.
    pathname : string
        Selecte path.
    

    Examples
    --------
    >>> (myFile, myPath) = thLib.ui.savefile('*.py', 'Testing file-selection', 'c:\\temp\\test.py')

    '''
    
    root = tk.Tk()
    root.withdraw()
    outFile = tkf.asksaveasfile(mode='w', title=DialogTitle, initialfile=DefaultName, filetypes=[('Save as', FilterSpec)])
    
    # Close the Tk-window manager again
    root.destroy()
    
    if outFile == None:
        (fileName, dirName) = ('','')
    else:
        fullOutFile = outFile.name
        print('Selection: ' + fullOutFile)
        dirName = path.dirname(fullOutFile)
        fileName = path.basename(fullOutFile)
        
    return (fileName, dirName)
    
def print_lines(*lines):
    """
    A helpful function for printing many
    separate strings on separate lines.
    """
    print("\n".join([line for line in lines]))

def showInstructions():
    """
    show the user his interface and the possible commands
    
    input:
        none        
    output:
        show the pssoble commands and parameters to the user
    """
    # print a main menu and the commands
    print_lines("RPG Game", 
                "========", 
                "commands:", 
                "'exit'", 
                "'status'",
                "'mission'", 
                "'go [north, east, south, west, up, down]'", 
                "'get [item]'", 
                "'fight [person]'", 
                "'drop [item]'",
                "'credits'")
    
def showStatus(currentRoom, rooms, turn, inventory):
    """
    the user can see in which room he is standing
    also his inventory is shown to him   
    the persons in the room
    the last point are the possible directions where he can go
    
    input:
        none
    output:
        three lines:
            place
            inventory
            persons
            possible directions
    """
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
        print("you see: " + rooms[currentRoom]["person"][0])
        if rooms[currentRoom]["person"][0] == "princess":
            print_lines("you won the game!", 
                        "you played " + str(turn) + " turn(s)")
    # print other accessible rooms
    CurRoom = set(rooms[currentRoom]).intersection(parameter_RPG.directions)
    
    if len(CurRoom) == 1:
    	print("There's a door leading: " + str(CurRoom))
    elif len(CurRoom) == 0:
    	print("There are no doors you can see!")
    elif len(CurRoom) > 1:
    	print("There are doors leading: " + str(CurRoom))
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
        "pros"      : [],
        "cons"      : []
                         }    
    
    print("name your hero please:")
    playerstatus_dummy["name"] = input(">")

    value = 0
    while (value != 8):
        value = 0
        print_lines("you can distribute 8 points onto the following 4 attributes:\n", 
                    "clever, social, strong, fast", 
                    "seperate them by comma (eg:2,2,3,1)",
                    "no atttribute should have more than 3 points")
        """
        # if german
        print_lines("du kannst 8 Punkte auf die folgenden 4 Attribute verteilen:\n",
                    "clever, sozial, stark, schnell",
                    "trenne sie mit Komma (z.B.: 2,2,3,1)",
                    "keiner der Attribute dar mehr als 3 PUnkte haben")
        """
        data = input(">").split(sep= ",")
        for index in range(4):
            # check if the values from the user are between 0 and 3
            if int(data[index]) <= 3 and int(data[index]) >= 0:
                 value = value + int(data[index])
        if value != 8:
            print("you distributed the values false")
        else:
            playerstatus_dummy["clever"] = int(data[0])
            playerstatus_dummy["social"] = int(data[1])
            playerstatus_dummy["strong"] = int(data[2])
            playerstatus_dummy["fast"] = int(data[3])
            playerstatus_dummy["life"] = int(data[2])*3
    print("your char was created, now the game can begin")
    return(playerstatus_dummy)

def fct_rooms():
    print("want to load a room layout (Y/N)?",
          "if N, the default training area is loaded.")
    decision = input(">").lower()
    if decision == 'y' or decision == 'yes':
        path = getfile(FilterSpec='.json', DialogTitle='Select file:')
        myfile = path.join(path[1],path[0])
        with open(myfile) as f:
            rooms = json.load(f)
    else:
        print("using default")

    # a dictionary linking a room to other positions
        rooms = {
            00:{ "mission_eng" : "find the princess",
                 "mission_ger" : "finde die Prinzessin"},
        
            11:{ "name" : "hall",
                 "east" : [12,'opened'],
                 "south": [13,'opened'],
                 "up"   : [21,'opened'],
                 "item" : ["torch"]},
                
            12:{ "name" : "bedroom",
                 "west" : [11,'opened'],
                 "south": [14,'opened'],
                 "item" : ["key"]},
                
            13:{ "name" : "kitchen",
                 "north": [11,'opened'],
                 "item" : ["sword"]},
                
            14:{ "name" : "bathroom",
                 "north": [12,'opened'],
                 "item" : ["soap"]},
                
            21:{ "name" : "stair",
                 "east" : [22,'opened'],
                 "south": [23,'opened'],
                 "down" : [11,'opened'],
                 "item" : ["torch"]},
                
            22:{ "name" : "corridor",
                 "west" : [21,'opened'],
                 "south": [24,'opened'],
                 "up"   : [32,'locked'],
                 "item" : ["torch"],
                 "person": ["bat",1]},
                
            23:{ "name" : "terrace",
                 "north": [21,'opened']},
                
            24:{ "name" : "study",
                 "north": [22,'opened'],
                 "item" : ["book"]},
            
            32:{ "name" : "towerroom",
                 "down" : [22,'locked'],
                 "person" : ["princess",0]}
                }
    return(rooms)
    
def fct_move(parameter, currentRoom, rooms, inventory):
    # check that they are allowed wherever they want to go
    if parameter in rooms[currentRoom]:
        # check if the door to the new room is locked
        if "locked" in rooms[currentRoom][parameter]:
            print("door locked")
            if "key" in inventory:
               print("want to use the key? [Y/N]")
               answer = input(">").lower()
               if answer == "y" or answer == "yes" or answer == "z":
                   print("opens the door with the key")
                   # change the door property
                   rooms[currentRoom][parameter][rooms[currentRoom][parameter].index("locked")] = 'opened'
                   # set the current room to the new room
                   currentRoom = rooms[currentRoom][parameter][0]
                   # change the lock of the old room from the new room
                   other = parameter_RPG.directions[(parameter_RPG.directions.index(parameter)+3)%6]
                   rooms[currentRoom][other][rooms[currentRoom][other].index("locked")] = 'opened'                  
        else:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][parameter][0]
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
    # check if someone is in the room
    # check that they are allowed whoever they want to fight
    if "person" in rooms[currentRoom] and parameter in rooms[currentRoom]["person"]:
        # if the player has a sword he is better at fighting
        if rooms[currentRoom]['person'][1] == 1:
            if "sword" in inventory:
                if(randint(1,6+1)>2):
                    print("enemy died")
                    # if the enemy died delete it from the room
                    del rooms[currentRoom]["person"]
                else:
                    print("you died")
                    print("you played " + str(turn) + " turn(s)")
                    # waits for 10 seconds to close the game
                    print("the game closes in 10 seconds")
                    sleep(10)
                    raise SystemExit
            else:
                if(randint(1,6+1)>4):
                    print("enemy died")
                    # if the enemy died delete it from the room
                    del rooms[currentRoom]["person"]
                else:
                    print("you died")
                    print("you played " + str(turn) + " turn(s)")
                    # waits for 10 seconds to close the game
                    print("the game closes in 10 seconds")
                    sleep(10)
                    raise SystemExit
        else:
            print("this person can't be attacked")
    else:
        print("you are fighting against your own shadow")
            
def fct_drop(parameter, currentRoom, rooms, inventory):
    # look if the player has something to drop
    if inventory == [] or inventory[inventory.index(parameter)] != parameter:
        print("you can't drop anything")
    else:
        rooms[currentRoom]["item"] += [parameter]
        del inventory[inventory.index(parameter)]
        print("you dropped " + parameter + "!")
    return(inventory)
    
def fct_exit(turn, playerstatus):
    print_lines("thank you for playing", 
               "you played " + str(turn) + " turn(s)", 
              "want to save your char (y/n)?")
    answer = input(">").lower()
    if answer == 'y' or answer == 'yes' or answer == "z":
        print("where do you want to save your char?")
        path = savefile(FilterSpec='.json', DialogTitle='Select File:')
        myfile = path.join(path[1],path[0])
        with open(myfile, 'w') as f:
            json.dump(playerstatus, f)
            print("stats saved under: " + myfile)      
    raise SystemExit
    
def random_dice(numberdices=6, numberoutput=2, exclusion = ' '):
    # if more than 0 dices are used
    if numberdices > 0:
        # if the output would be larger than the input
        # limit the number of dices to the output number
        if numberoutput > numberdices:
            numberoutput = numberdices

        values = []
        for i in range(numberdices):
            values.append(randint(1,6))
        values.sort(reverse=True)
        output = []
        if numberdices == 1:
            return(int(sum(values)))
        else:
            if exclusion != ' ':
                for index in range(numberdices):
                    if len(output) < numberoutput:
                        if values[index] != exclusion:
                            output += [values[index]]
            else:
                for index in range(numberoutput):
                    output += [values[index]]
        return(int(sum(output)))
    # if 0 or less dices are used
    else:
        return(0)
    
def fct_fight_rat(playerstatus, enemystatus, enemy, currentRoom, rooms):
    # look for any exclusion criteria
    if playerstatus["pack"] == 'collector':
        player_exclusion_init = 6
    else:
        player_exclusion_init = ' '
        
    # dice out the initiative of the player and the enemy
    init_player = random_dice(numberdices=playerstatus["fast"], numberoutput=playerstatus["fast"], exclusion=player_exclusion_init)
    init_enemy = random_dice(numberdices=enemystatus[enemy]["fast"], numberoutput=enemystatus[enemy]["fast"], exclusion=' ')
    
    # falls sie den gleichen Wert haben
    if init_player == init_enemy:
        while init_player == init_enemy:    
            init_player = random_dice(1,1,' ')
            init_enemy = random_dice(1,1,' ')
            
    if init_player > init_enemy:
        player_turn = True
        enemy_turn = False
    else:
        player_turn = False
        enemy_turn = True
    
    # values needed: strong, fast, clever, life
    fight_array = ones((2,8))
    fight_array[0,0] = playerstatus['strong']
    fight_array[0,1] = playerstatus['fast']
    fight_array[0,2] = playerstatus['clever']
    fight_array[0,3] = playerstatus['life'] # gesamte Lebenspunkte
    fight_array[0,4] = playerstatus['life'] # aktuelle Lebenspunkte
    fight_array[0,5] = 1 # Status Bewusstsein
    fight_array[0,6] = 0 # Status festbeißen
    fight_array[0,7] = 0 # Status überwältigen
    
    fight_array[1,0] = enemystatus[enemy]['strong']
    fight_array[1,1] = enemystatus[enemy]['fast']
    fight_array[1,2] = enemystatus[enemy]['clever']
    fight_array[1,3] = enemystatus[enemy]['life'] # gesamte Lebenspunkte
    fight_array[1,4] = enemystatus[enemy]['life'] # aktuelle Lebenspunkte
    fight_array[1,5] = 1 # Status Bewusstsein
    fight_array[1,6] = 0 # Status festbeißen
    fight_array[1,7] = 0 # Status überwältigen
    
    fight_array = fight_array.astype(int)
    
    while fight_array[0,4] != 0 or fight_array[1,4] != 0:
        # calculate the malus for the dice results
        player_malus = int((fight_array[0,3]-fight_array[0,4])//2)
        enemy_malus = int((fight_array[1,3]-fight_array[1,4])//2)

        # falls der Spieler am Zug ist oder der Gegner bewusstlos ist:
        if player_turn or fight_array[1,5] == 0:
            decision = 0 
            # falls der Spieler sich schon festgebissen hat
            if fight_array[0,6] == 1:
                # attack values of the enemy and the player not necessary, 
                # because the damage is dealt automatically:
                # player = 1
                # enemy = 0
                fight_array = damage_calculation(currentRoom, rooms, fight_array, player=1, enemy=0)               
            # falls der Spieler sich noch nicht festgebissen hat
            else: 
                while decision == 0:
                    print_lines("what do you want to do?", 
                    "(1) attack", # strong/fast
                    "(2) bite tight", # strong/fast; dann strong/fast vs. strong/fast
                    "(3) overwhelm") # strong/fast, strong/clever vs. strong/clever
                    if fight_array[1,6] == 1:
                        print("(4) shake of the bite")
                        if fight_array[1,7] == 1:
                            print("(5) shake of overwhelming")
                    else:
                        if fight_array[1,7] == 1:
                            print("(4) shake of overwhelming")
                    decision = int(input(">"))
                    # Wert Spieler und Gegner bestimmen
                    player = random_dice(numberdices=fight_array[0,0]+fight_array[0,1], numberoutput=2, exclusion=' ') - int(player_malus)
                    # falls der Gegner nicht bewusstlos ist
                    if fight_array[1,5] != 0:
                        # Wahrscheinlichkeit: 2/3 ausweichen, 1/3 blocken
                        # falls kleiner, dann ausweichen: clever/fast
                        if randint(1,6) < 4:
                            enemy = random_dice(numberdices=fight_array[1,2]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                        # sonst blocken: strong/fast
                        else:
                            enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                    # ansonsten hat er einen Kampf mit dem Ergebnis 0 gemacht
                    else:
                        enemy = 0
                    
                    if player > enemy:
                        # falls es keine Überwältigung und kein durch den Gegner gab
                        if fight_array[1,7] == 1 and fight_array[1,6] == 1:
                            if decision < 1 or decision > 5:
                                print("false input")
                                decision = 0
                        # falls es keine festbeißen durch den Gegner gab
                        elif fight_array[1,6] == 1:
                            if decision < 1 or decision > 4:
                                print("false input")
                                decision = 0
                        # falls es keine Behinderung durch den Gegner gab
                        else:
                            if decision < 1 or decision > 3:
                                print("false input")
                                decision = 0
                        # wenn der Spieler angreift
                        if decision == 1:
                            fight_array = damage_calculation(currentRoom, rooms, fight_array, player, enemy)
                                    
                        # wenn der Spieler sich festbeißen will               
                        if decision == 2:
                            # Angriff erfolgreich, Schaden verrechnen
                            fight_array = damage_calculation(currentRoom, rooms, fight_array, player, enemy)
                                
                            # muss sich noch festbeißen
                            player = random_dice(numberdices=fight_array[0,0]+fight_array[0,1], numberoutput=2, exclusion=' ') - int(player_malus)
                            enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                            # falls größer, hast sich der Spieler festgebissen
                            if player > enemy:
                                fight_array[0,6] = 1
                                print("you were able to bite tight")
                            else:
                                print("you weren't able to bite tight")
                               
                        # falls der Spieler den Gegner überwältigen will
                        if decision == 3:
                            # kein Schaden verrechnet
                            # muss den Gegner noch überwältigen
                            player = random_dice(numberdices=fight_array[0,0]+fight_array[0,2], numberoutput=2, exclusion=' ') - int(player_malus)
                            enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,2], numberoutput=2, exclusion=' ') - int(enemy_malus)
                            # falls größer, wurde der Gegner überwältigt
                            if player > enemy:
                                fight_array[0,7] = 1
                                print("you have overpowered the enemy")
                            else:
                                print("you couldn't overpower the enemy")  
                        if decision == 4:
                            print("you could loose the bite")
                        if decision == 5:
                            print("you could loose the overpowering")
                    else:
                        print("the enemy has tricked you")
                        
        else: # enemy turn
            # hat nur eine Attacke pro Runde
            attack_used = False
            
            # if the enemy lost consciosness he has no turn
            if fight_array[1,5] == 0:
                attack_used = True
                
            # falls der Gegner überwätligt wurde, befreit er sich
            if fight_array[0,7] == 1 and attack_used == False:
                enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,2], numberoutput=2, exclusion=' ') - int(fight_array[0,0]) - int(enemy_malus)
                player = random_dice(numberdices=fight_array[0,0]+fight_array[0,2], numberoutput=2, exclusion=' ') - int(player_malus)
                if enemy>player:
                    print("the enemy has freed himself")
                    fight_array[0,7] = 0
                else:
                    print("the enemy wasn't able to free himself")
                attack_used = True
            # festbeißen lösen , selber festbeißen, selber angreifen oder überwältigen
            # falls Spieler sich nicht festgebissen hat
            if fight_array[0,6] == 0:
                # gibt es nur 3 Möglichkeiten (angreifen, selber festbeißen, überwältigen)
                decision = randint(1,3)
            # falls Spieler sich festgebissen hat
            else:
                # gibt es 4 Möglichkeiten (angreifen, selber festbeißen, überwältigen, festbeißen lösen)
                decision = randint(1,4)
            
            # Werte für Angriff vorberechnen
            enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,2], numberoutput=2, exclusion=' ') - int(enemy_malus)
            player = random_dice(numberdices=fight_array[0,0]+fight_array[0,2], numberoutput=2, exclusion=' ') - int(player_malus)
            
            # falls 1, dann angreifen
            if decision == 1 and attack_used == False:
                if enemy > player:
                    fight_array = damage_calculation(currentRoom, rooms, fight_array, player, enemy)
                    print("the enemy has attacked and damaged you")
                else:
                    print("the enemy attacked you but wasn't able to damage you")
                attack_used = True
                    
            # falls 2, dann selber festbeißen
            elif decision == 2 and attack_used == False:
                # angreifen
                if enemy > player:
                    fight_array = damage_calculation(currentRoom, rooms, fight_array, player, enemy)
                    print("the enemy attacked you and tries to bite tight")
                    # festbeißen
                    enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                    player = random_dice(numberdices=fight_array[0,0]+fight_array[0,1], numberoutput=2, exclusion=' ') - int(player_malus)
                    if enemy > player:
                        fight_array[1,6] = 1
                        print("the enemy was able to bite tight")
                    else:
                        print("the enemy wasn't able to bite tight")
                else:
                    print("the enemy attacked you but wasn't able to damage you")
                attack_used = True
                        
            # falls 3, dann Spieler überwältigen
            elif decision == 3 and attack_used == False:
                if enemy > player:
                    print("the enemy attacked you and tries to overpower you")
                    enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,2], numberoutput=2, exclusion=' ') - int(enemy_malus)
                    player = random_dice(numberdices=fight_array[0,0]+fight_array[0,2], numberoutput=2, exclusion=' ') - int(player_malus)
                    # falls größer, wurde der Gegner überwältigt
                    if enemy > player:
                        fight_array[1,7] = 1
                        print("you were overpowered")
                    else:
                        print("you weren't overpowered")
                else:
                    print("the enemy attacked you but wasn't able to damage you")
                attack_used = True
                     
            # falls 4, dann festbeißen lösen
            elif decision == 4 and attack_used == False:
                enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                player = random_dice(numberdices=fight_array[0,0]+fight_array[0,1], numberoutput=2, exclusion=' ') - int(player_malus)
                if enemy > player:
                    print("the enemy could free himself from your bite")
                else:
                    print("the enemy couldn't free himself from your bite")
                attack_used = True
            
            else:
                print("you have tricked the enemy")
            
        # switch turns
        player_turn = not player_turn
        enemy_turn = not enemy_turn
        
    if fight_array[1,4] == 0:
        print("the enemy is dead")
    else:
        print("you died after XXX turns")
        
def damage_calculation(currentRoom, rooms, fight_array, player, enemy):
    if player > enemy:
        # Abzug der Lebenspunkte
        fight_array[1,4] = fight_array[1,4] - fight_array[0,0]
        print("you have bitten the enemy")
        # falls die LP des Gegners <1 sind, dann passiert etwas
        if fight_array[1,4] < 1:
            # Gegner ist bewusstlos
            fight_array[1,5] = 0
            print("enemy is unconscios")                            
            #falls seine Lebenspunkte = -Stärke, dann stirbt er
            if fight_array[1,4] <= -fight_array[1,0]:
                print("enemy is dead")
                del rooms[currentRoom]["person"]
    else:
        # Abzug der Lebenspunkte
        fight_array[0,4] = fight_array[0,4] - fight_array[1,0]
        print("the enemy has bitten you")
        # falls die LP des Spielers <1 sind, dann passiert etwas
        if fight_array[0,4] < 1:
            # Spieler ist bewusstlos
            fight_array[0,5] = 0
            print("you are unconsios")                            
            #falls seine Lebenspunkte = -Stärke, dann stirbt er
            if fight_array[0,4] <= -fight_array[0,0]:
                print("you are dead")  
    return(fight_array)
                        
