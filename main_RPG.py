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
            if parameter_enemies_RPG.directions.count(move[1]) == 1:
                currentRoom = functions_RPG.fct_move(move[1], currentRoom, rooms, inventory)
                turn += 1
            else:
                print("burn the heretic, this is no legal direction!")
            
        # if they type 'get' first
        elif move[0] == "get":
            inventory = functions_RPG.fct_get(move[1], currentRoom, rooms, inventory)
                
        # if they type 'fight' first
        elif move[0] == "fight":
            #functions_RPG.fct_fight(move[1], currentRoom, rooms, inventory, turn)
            functions_RPG.fct_fight_rat(playerstatus, parameter_enemies_RPG.enemystatus, move[1], currentRoom, rooms)
                    
        # if the player wants to drop something
        elif move[0] == "drop":
            inventory = functions_RPG.fct_drop(move[1], currentRoom, rooms, inventory)
        
        #if the player wants to know his status
        elif move[0] == "status":
            print(playerstatus)
            
        # if the player wants to end the game        
        elif move[0] == "exit":
            functions_RPG.fct_exit(turn, playerstatus)
            
        # if the player wants to end the game        
        elif move[0] == "mission":
            print(rooms[00]["mission"])   
            
        # if there is a false input from the player
        else: 
            print("falsche Eingabe")
           
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