# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version:            1.0

Programmed with:    WinPython 3.4.4.1
Changed to:         WinPython 2.7.10.3

History:
[2016.03.23, CS]:   initial setup; copy the main code from: 
                    http://usingpython.com/python-rpg-game/; insert a second 
                    and a third floor above the hall; insert items in the 
                    rooms; insert enemy; insert princess;
[2016.03.24, CS]:   insert game logic (need a key for the towerroom door) and 
                    the use of the key; insert the exit function; put every 
                    command in an own function; save playerstatus; load rooms 
                    from an external file or use the dummy file; 
[2016.03.29, CS]:   ERROR5: using a command like 'fight' or 'go' without a 
                    specific target -> crash;
                    ERROR5: solved: the commands with two parameters are
                    checked for length (if len(move) == 2);
                    ERROR6: using a command like 'fight' with a false target 
                    -> crash;
                    ERROR6: solved: look, if the person the player wants to
                    fight is in the room;
[2016.04.11, CS]:   ISSUE#16: changed all the naming of the interaction in
                    english;
[2016.04.14, CS]:   insert Version of the program: consists of game version, 
                    date, hour and initials (eg V0_2016.04.14_15_CS);
[2016.04.15, CS]:   ISSUE#21: insert the save command;
[2016.04.16, CS]:   ISSUE#21: implement the autosave;
[2016.04.16, MG]:   ISSUE#19: "use" function called
[2016.04.16, CS]:   ISSUE#22: shift the load game to the main function;
[2016.04.18, CS]:   ISSUE#26: add a history of the player's commands to the 
                    game, implemented it also in all the subfunctions with 
                    input in them;
[2016.04.18, CS]:   ISSUE#29: add the help function to the main loop;  
[2016.04.19, CS]:   change the credits; change to version 1.0;   
[2016.04.20, CS]:   ISSUE#35: make the code python 2-3 compatible;
                    ISSUE#32: implemented a behavoir of the game when the soap
                    is used;
[2016.04.25, CS]:   load game and load character implemented; currentRoom, 
                    inventory, torch and turn changed to be within fct_main;
"""
# python 2-3 compatible code
import future
from builtins import input
import past
import six

# import the functions
import functions_RPG
from parameter_RPG import directions

import time

# version number
version = 'V1_2016.04.21_16_CS'

def credits_game():
    functions_RPG.print_lines("development and programming","Christoph","Hias","")
    functions_RPG.print_lines("testing","Flo","Alex","Steffi","Patrick","Ben","")
    functions_RPG.print_lines("support","missing","")
    functions_RPG.print_lines("special thanks","Kopfkino")

def fct_main():
    # start the player in room 1
    currentRoom = 11
    # an inventory, which is initially empty
    inventory = []
    #torch burn duration
    torch = 0
    # initialize the turns
    turn = 1
    
    # time window until the game makes an autosave
    time_window = 0
    
    # generate the save_time stamp for the history
    # get the localtime variables
    localtime = time.localtime(time.time())
    # make the save time stamp (year_month_day_hour_min_sec)
    save_time = str(localtime.tm_year) +'_'+ str(localtime.tm_mon) +'_'+ str(localtime.tm_mday) +'_'+ str(localtime.tm_hour) +'_'+ str(localtime.tm_min) +'_'+ str(localtime.tm_sec)
    # generate file name
    history = 'history_'+save_time+'.txt'
    
    
    # ask the player, if he wants to load a game
    functions_RPG.print_lines("want to load a save point (Y/N)?",
                              "if N, a new game is started.")
    decision = input('>').lower() 
    decision = decision.lower() 
    # write the command to the history
    functions_RPG.write_history(history, decision)
    
    if decision == 'y' or decision == 'yes' or decision == 'z':
        # load the data of the save game
        playerstatus, rooms, currentRoom, inventory, turn = functions_RPG.fct_load_game()
    else:
        # ask the player if eh wants to load a character?
        print('want to load a character? (Y/N)')
        decision = input('>').lower() 
        decision = decision.lower() 
        # write the command to the history
        functions_RPG.write_history(history, decision)
        if decision == 'y' or decision == 'yes' or decision == 'z':
            # load the data of the save game
            playerstatus, rooms_dummy, currentRoom_dummy, inventory, turn_dummy = functions_RPG.fct_load_game()
            # delete the not used parameters
            del rooms_dummy
            del currentRoom_dummy
            del turn_dummy
            
        else:
            # generate the character
            playerstatus = functions_RPG.generate_char(history)
            # generate rooms
            rooms = functions_RPG.fct_rooms()
       
    functions_RPG.showInstructions()
        
    # loop infinitely
    while True:
        # first time stamp
        first_time_stamp = time.time()
        
        functions_RPG.showStatus(currentRoom, rooms, turn, inventory, torch, history, playerstatus)
        
        # get the player's next move
        # .split() breaks it up into a list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = input(">")
        move = move.lower().split()  
        # write the command to the history
        functions_RPG.write_history(history, move)      
        
        # check if there is any input
        if len(move) != 0:
            # if they type 'go' first
            if move[0] == "go":
                if len(move) == 2:
                    if directions.count(move[1]) == 1:
                        currentRoom = functions_RPG.fct_move(move[1], currentRoom, rooms, inventory, history)
                        turn += 1
                        if torch != 0:
                            torch -= 1
                    else:
                        print("burn the heretic, this is no legal direction!")
                else: 
                    print("false input")
                
            # if they type 'get' first
            elif move[0] == "get":
                if len(move) == 2:
                    inventory = functions_RPG.fct_get(move[1], currentRoom, rooms, inventory, torch)
                else: 
                    print("false input")
                    
            # if they type 'fight' first
            elif move[0] == "fight":
                if len(move) == 2:               
                    functions_RPG.fct_fight(move[1], currentRoom, rooms, inventory, turn, torch)
                    #functions_RPG.fct_fight_rat(playerstatus, parameter_enemies_RPG.enemystatus, move[1], currentRoom, rooms, history)
                else: 
                    print("false input")
                        
            # if the player wants to drop something
            elif move[0] == "drop":
                if len(move) == 2:
                    inventory = functions_RPG.fct_drop(move[1], currentRoom, rooms, inventory)
                else: 
                    print("false input")
            
            #if the player wants to use something
            elif move[0] == "use":
                if len(move) == 2:
                    invNtor = functions_RPG.fct_use(move[1], currentRoom, rooms, inventory, torch)
                    inventory = invNtor[0]
                    torch = invNtor[1]
                    #inventory = functions_RPG.fct_use(move[1], currentRoom, rooms, inventory, torch)
                else: 
                    print("false input")

            #if the player wants to know his status
            elif move[0] == "status":
                print(playerstatus)
                
            # if the player wants to end the game        
            elif move[0] == "exit":
                functions_RPG.fct_exit(turn, playerstatus, history)
                
            # if the player wants to end the game        
            elif move[0] == "mission":
                print(rooms[00]["mission_eng"])  
                
            elif move[0] == "credits":
                credits_game()   
                
            # if the player wants to save his status
            elif move[0] == "save":
                functions_RPG.fct_save_game(0, playerstatus, rooms, currentRoom, inventory, turn)
                
            # if the player wants to see the commands
            elif move[0] == "help":
                functions_RPG.showInstructions()
                
            # if there is a false input from the player
            else: 
                print("false input")
        else:
            print("should I try something? no, this is your adventure")
        
        # second time stamp
        second_time_stamp = time.time()
        # add up the time stamps
        time_window += second_time_stamp-first_time_stamp
        # 5 min = 5*60 = 300
        if time_window >= 300:    
            time_window = 0
            print('game since 5 minutes not stored')
            functions_RPG.fct_save_game(1, playerstatus, rooms, currentRoom, inventory, turn)
           
# main function
if __name__=='__main__':
    # version number
    global version
    print('Version: %s' % version)

    # start the game
    fct_main()
