"""
Header

@author: Christoph
Version: 0.1

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
[2016.04.14, CS]:   insert Version of the program: consists of game version, date, hour 
                    and initials (eg V0_2016.04.14_15_CS);
[2016.04.15, CS]:   ISSUE#21: insert the save command;
[2016.04.16, CS]:   ISSUE#21: implement the autosave;
"""
# import the functions
import functions_RPG
from parameter_RPG import directions

import time

# version number
version = 'V0_2016.04.15_16_CS'

def credits_game():
    functions_RPG.print_lines("development and programming","Christoph","Hias","")
    functions_RPG.print_lines("testing","Flo","Gerfried","Alex","")
    functions_RPG.print_lines("support","missing","")
    functions_RPG.print_lines("special thanks","Kopfkino")
            
def fct_main(currentRoom, inventory , turn, rooms):
    time_window = 0
    
    playerstatus = functions_RPG.generate_char()
       
    functions_RPG.showInstructions()
    
    # loop infinitely
    while True:
        # first time stamp
        first_time_stamp = time.time()
        
        functions_RPG.showStatus(currentRoom, rooms, turn, inventory)
        
        # get the player's next move
        # .split() breaks it up into a list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = input(">").lower().split()
        
        # check if there is any input
        if len(move) != 0:
            # if they type 'go' first
            if move[0] == "go":
                if len(move) == 2:
                    if directions.count(move[1]) == 1:
                        currentRoom = functions_RPG.fct_move(move[1], currentRoom, rooms, inventory)
                        turn += 1
                    else:
                        print("burn the heretic, this is no legal direction!")
                else: 
                    print("false input")
                
            # if they type 'get' first
            elif move[0] == "get":
                if len(move) == 2:
                    inventory = functions_RPG.fct_get(move[1], currentRoom, rooms, inventory)
                else: 
                    print("false input")
                    
            # if they type 'fight' first
            elif move[0] == "fight":
                if len(move) == 2:               
                    functions_RPG.fct_fight(move[1], currentRoom, rooms, inventory, turn)
                    #functions_RPG.fct_fight_rat(playerstatus, parameter_enemies_RPG.enemystatus, move[1], currentRoom, rooms)
                else: 
                    print("false input")
                        
            # if the player wants to drop something
            elif move[0] == "drop":
                if len(move) == 2:
                    inventory = functions_RPG.fct_drop(move[1], currentRoom, rooms, inventory)
                else: 
                    print("false input")
            
            #if the player wants to know his status
            elif move[0] == "status":
                print(playerstatus)
                
            # if the player wants to end the game        
            elif move[0] == "exit":
                functions_RPG.fct_exit(turn, playerstatus)
                
            # if the player wants to end the game        
            elif move[0] == "mission":
                print(rooms[00]["mission_eng"])  
                
            elif move[0] == "credits":
                credits_game()   
                
            # if the player wants to save his status
            elif move[0] == "save":
                functions_RPG.fct_save_game(0, playerstatus, rooms, currentRoom, inventory, turn)
                
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
    # start the player in room 1
    currentRoom = 11
    # an inventory, which is initially empty
    inventory = []
    # initialize the turns
    turn = 1
    # version number
    global version
    print('Version: %s' % version)
    # generate rooms
    rooms = functions_RPG.fct_rooms()
    # start the game
    fct_main(currentRoom, inventory, turn, rooms)