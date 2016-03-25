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
[2016.03.25, CS]:   ERROR2 solved: put the needed functions into the 
                    functions_RPG.py;
                    ERROR1: solved: the turn counter has to inerate with 1 and 
                    not with itself;
                    implement random_dice function with any number of dices, 
                    output and an exclusion criteria;
                    ERROR3: starting a fight the following message appears:
                    'numpy.float64' object cannot be interpreted as an integer;
                    ERROR3: solved: change the type of the fight_array from
                    float64 to int32;
                    ERROR4: problem with the enemy's turn;
"""
# import the functions
import functions_RPG
import parameter_enemies_RPG

path_at_work = r'C:\Users\Schauer\Documents\Privat\RPG-Ratten.git\trunk'
            
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
            currentRoom = functions_RPG.fct_move(move[1], currentRoom, rooms, inventory)
        
        # if they type 'get' first
        if move[0] == "get":
            inventory = functions_RPG.fct_get(move[1], currentRoom, rooms, inventory)
                
        # if they type 'fight' first
        if move[0] == "fight":
            #functions_RPG.fct_fight(move[1], currentRoom, rooms, inventory, turn)
            functions_RPG.fct_fight_rat(playerstatus, parameter_enemies_RPG.enemystatus, move[1], currentRoom, rooms)
                    
        # if the player wants to drop something
        if move[0] == "drop":
            inventory = functions_RPG.fct_drop(move[1], currentRoom, rooms, inventory)
              
        if move[0] == "status":
            print(playerstatus)
                
        if move[0] == "exit":
            functions_RPG.fct_exit(turn, playerstatus)
           
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
    rooms = functions_RPG.fct_rooms(path_at_work)
    # start the game
    fct_main(currentRoom, inventory, turn, rooms)