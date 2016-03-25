# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version : 0.1

History:
[2016.03.24, CS]:   initial setup; put in all the functions of the main_RPG;
[2016.03.25, CS]:   insert the rest of the functions; insert the random_dice 
                    function;
                    start with the rat fighting system function;
"""
import random
import os.path as pfad
import json
import tkinter as tk
import tkinter.filedialog as tkf

import numpy as np

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
    
    if not pfad.exists(fullInFile):
        return (0, 0)
    else:
        print('Selection: ' + fullInFile)
        dirName = pfad.dirname(fullInFile)
        fileName = pfad.basename(fullInFile)
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
        dirName = pfad.dirname(fullOutFile)
        fileName = pfad.basename(fullOutFile)
        
    return (fileName, dirName)
    
def print_lines(*lines):
    """
    A helpful function for printing many
    separate strings on separate lines.
    """
    print("\n".join([line for line in lines]))

def showInstructions():
    # print a main menu and the commands
    print_lines("RPG Game", 
                "========", 
                "commands:", 
                "'exit'", 
                "'status'", 
                "'go [direction]'", 
                "'get [item]'", 
                "'fight [person]'", 
                "'drop [item]'")
    
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
            print_lines("you won the game!", 
                        "you played " + str(turn) + " turn(s)")
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
    
    print("Name your Hero please:")
    playerstatus_dummy["name"] = input(">")

    value = 0
    while (value != 8):
        value = 0
        print_lines("you can distribute 8 points onto the following 4 attributes:\n", 
                    "clever, social, strong, fast", 
                    "seperate them by comma (eg:2,2,3,1)")
        data = input(">").split(sep= ",")
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

def fct_rooms(path_at_work):
    print("want to load a room layout or use the default (Y/N)?")
    decision = input(">").lower()
    if decision == 'y' or decision == 'yes':
        path = getfile(FilterSpec='.json', DialogTitle='Select file:')
        myfile = pfad.join(path[1],path[0])
        with open(myfile) as f:
            rooms = json.load(f)
    else:
        print("using default")
        if pfad.exists(path_at_work + '\rooms.json'):
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
                     "person": "fledermaus"},
                    
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
    
def fct_move(parameter, currentRoom, rooms, inventory):
    # check that they are allowed wherever they want to go
    if parameter in rooms[currentRoom]:
        newRoom = rooms[currentRoom][parameter]
        # check if the door to the new room is locked
        if "property" in rooms[newRoom] and rooms[newRoom]["property"] == "locked":
            print("door locked")
            if "key" in inventory:
               print("want to use the key? [Y/N]")
               answer = input(">").lower()
               if answer == "y" or answer == "yes":
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
            exit()
    else:
        if(random.randint(1,6+1)>4):
            print("enemy died")
            # if the enemy died delete it from the room
            del rooms[currentRoom]["person"]
        else:
            print("you died")
            print("you played " + str(turn) + " turn(s)")
            exit()
            
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
    decision = input(">").lower()
    if decision == 'y' or decision == 'yes':
        print("where do you want to save your char?")
        path = savefile(FilterSpec='.json', DialogTitle='Select File:')
        myfile = pfad.join(path[1],path[0])
        with open(myfile, 'w') as f:
            json.dump(playerstatus, f)
            print("stats saved under: " + myfile)      
    exit()
    
def random_dice(numberdices=6, numberoutput=2, exclusion = ' '):
    if numberoutput > numberdices:
        return('ERROR')
    else:
        values = []
        for i in range(numberdices):
            values.append(random.randint(1,6))
        values.sort(reverse=True)
        output = []
        if numberdices == 1:
            return(values)
        else:
            if exclusion != ' ':
                for index in range(numberdices):
                    if len(output) < numberoutput:
                        if values[index] != exclusion:
                            output += [values[index]]
            else:
                for index in range(numberoutput):
                    output += [values[index]]
        return(int(np.sum(output)))
    
def fct_fight_rat(playerstatus, enemystatus, enemy, currentRoom, rooms):
    # look for any exclusion criteria
    if playerstatus["pack"] == 'Sammler':
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
    fight_array = np.ones((2,8))
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
        print_lines("what do you want to do?", 
                    "(1) angreifen", # strong/fast
                    "(2) festbeißen", # strong/fast; dann strong/fast vs. strong/fast
                    "(3) überwältigen") # strong/fast, strong/clever vs. strong/clever
        if fight_array[1,7] == 1:
            print("(4) Überwältigung lösen")
        decision = input(">")
        
        if player_turn or fight_array[1,5] == 0:
            # falls der Spieler sich schon festgebissen hat
            if fight_array[0,6] == 1:
                fight_array = damage_calculation(currentRoom, rooms, fight_array, player_turn)

            # falls der Spieler sich noch nicht festgebissen hat           
            else: 
                # Wert Spieler und Gegner bestimmen
                player = random_dice(numberdices=fight_array[0,0]+fight_array[0,1], numberoutput=2, exclusion=' ') - int(player_malus)
                # falls der Gegner nicht bewusstlos ist
                if fight_array[1,5] != 0:
                    # falls kleiner, dann ausweichen: clever/fast
                    if random_dice(1,1)[0] < 4:
                        enemy = random_dice(numberdices=fight_array[1,2]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                    # sonst blocken: strong/fast
                    else:
                        enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                # ansonsten hat er einen Kampf mit dem Ergebnis 0 gemacht
                else:
                    enemy = 0
                
                if player > enemy:
                    # wenn der Spieler angreift
                    if decision == 1:
                        fight_array = damage_calculation(currentRoom, rooms, fight_array, player_turn)
                                
                    # wenn der Spieler sich festbeißen will               
                    if decision == 2:
                        # Angriff erfolgreich, Schaden verrechnen
                        fight_array = damage_calculation(currentRoom, rooms, fight_array, player_turn)
                            
                        # muss sich noch festbeißen
                        player = random_dice(numberdices=fight_array[0,0]+fight_array[0,1], numberoutput=2, exclusion=' ') - int(player_malus)
                        enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                        # falls größer, hast sich der Spieler festgebissen
                        if player > enemy:
                            fight_array[0,6] = 1
                            print("du konntest dich festbeißen")
                        else:
                            print("du konntest dich nicht festbeißen")
                           
                    # falls der Spieler den Gegner überwältigen will
                    if decision == 3:
                        # kein Schaden verrechnet
                        # muss den Gegner noch überwältigen
                        player = random_dice(numberdices=fight_array[0,0]+fight_array[0,2], numberoutput=2, exclusion=' ') - int(player_malus)
                        enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,2], numberoutput=2, exclusion=' ') - int(enemy_malus)
                        # falls größer, wurde der Gegner überwältigt
                        if player > enemy:
                            fight_array[0,7] = 1
                            print("du hast den Gegner überwältigt")
                        else:
                            print("du konntest den Gegner nicht überwältigen")
                else:
                    print("der Gegner hat dich ausgetrickst")
        else: # enemy turn
            # hat nur eine Attacke pro Runde
            attack_used = False
            # falls der Gegner überwätligt wurde, befreit er sich
            if fight_array[0,6] == 1 and attack_used == False:
                enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,2], numberoutput=2, exclusion=' ') - int(fight_array[0,0]) - int(enemy_malus)
                player = random_dice(numberdices=fight_array[0,0]+fight_array[0,2], numberoutput=2, exclusion=' ') - int(player_malus)
                if enemy>player:
                    print("der Gegner hat sich befreit")
                    fight_array[0,6] = 0
                else:
                    print("der Gegner konnte sich nicht befreien")
                attack_used = True
            # festbeißen lösen , selber festbeißen, selber angreifen oder überwältigen
            decision = random.randint(1,4)
            
            # Werte für Angriff vorberechnen
            enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,2], numberoutput=2, exclusion=' ') - int(enemy_malus)
            player = random_dice(numberdices=fight_array[0,0]+fight_array[0,2], numberoutput=2, exclusion=' ') - int(player_malus)
            
            # falls 1, dann angreifen
            if decision == 1 and attack_used == False:
                if enemy > player:
                    fight_array = damage_calculation(currentRoom, rooms, fight_array, player_turn)
                    
            # falls 2, dann festbeißen lösen
            elif decision == 2 and attack_used == False:
                enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                player = random_dice(numberdices=fight_array[0,0]+fight_array[0,1], numberoutput=2, exclusion=' ') - int(player_malus)
                if enemy > player:
                    print("der Gegner konnte sich aus deinem Biss lösen")
                else:
                    print("der Gegner konnte sich aus deinem Biss nicht lösen")
                    
            # falls 3, dann selber festbeißen
            elif decision == 3 and attack_used == False:
                # angreifen
                if enemy > player:
                    fight_array = damage_calculation(currentRoom, rooms, fight_array, player_turn)
                    # festbeißen
                    enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,1], numberoutput=2, exclusion=' ') - int(enemy_malus)
                    player = random_dice(numberdices=fight_array[0,0]+fight_array[0,1], numberoutput=2, exclusion=' ') - int(player_malus)
                    if enemy > player:
                        fight_array[1,6] = 1
                        print("der Gegner konnte sich festbeißen")
                    else:
                        print("der Gegner konnte sich nicht festbeißen")
                        
            # falls 4. dann Spieler überwältigen
            else:
             if enemy > player:
                 enemy = random_dice(numberdices=fight_array[1,0]+fight_array[1,2], numberoutput=2, exclusion=' ') - int(enemy_malus)
                 player = random_dice(numberdices=fight_array[0,0]+fight_array[0,2], numberoutput=2, exclusion=' ') - int(player_malus)
                 # falls größer, wurde der Gegner überwältigt
                 if enemy > player:
                     fight_array[1,7] = 1
                     print("du wurdest überwältigt")
                 else:
                     print("du konntest vom Gegner nicht überwältigen werden") 
            attack_used = True
            
        # switch turns
        player_turn = not player_turn
        enemy_turn = not enemy_turn
        
        
                    
def damage_calculation(currentRoom, rooms, fight_array, player_turn):
    if player_turn    :
        # Abzug der Lebenspunkte
        fight_array[1,4] = fight_array[1,4] - fight_array[0,0]
        print("du hast den Gegner gebissen")
        # falls die LP des Gegners <1 sind, dann passiert etwas
        if fight_array[1,4] < 1:
            # Gegner ist bewusstlos
            fight_array[1,5] = 0
            print("Gegner ist bewusstlos")                            
            #falls seine Lebenspunkte = -Stärke, dann stirbt er
            if fight_array[1,4] <= -fight_array[1,0]:
                print("Gegner ist tot")
                del rooms[currentRoom]["person"]
    else:
        # Abzug der Lebenspunkte
        fight_array[0,4] = fight_array[0,4] - fight_array[1,0]
        print("der Gegner hat dich gebissen")
        # falls die LP des Spielers <1 sind, dann passiert etwas
        if fight_array[0,4] < 1:
            # Spieler ist bewusstlos
            fight_array[0,5] = 0
            print("du bist bewusstlos")                            
            #falls seine Lebenspunkte = -Stärke, dann stirbt er
            if fight_array[0,4] <= -fight_array[0,0]:
                print("du bist tot")  
    return(fight_array)
                        