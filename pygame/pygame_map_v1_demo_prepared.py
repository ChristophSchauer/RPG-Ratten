# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:17:26 2016

@author: Christoph
"""

'''
usingpython: PYgame Tilemaps
following are the different levels and the colors

with key input change the position of the mouse

01052016
insert stairs in whitewa
setting the area as 'background' (blit once)
and only update the current room and the last room
'''
import pygame, sys
from pygame.locals import *
 
# currentRoom
currentRoom = 11

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# color of the tiles
BLACK  = (0,  0,  0  )
WHITE  = (255,255,255)
BROWN  = (153,76, 0  )
GREEN  = (0,  255,0  )
RED    = (255,0,  0  )
BLUE   = (0,  0,  255) 
GREY   = (128,128,128)
YELLOW = (255,255,0  )
MAGENTA= (255,0  ,255)
CYAN   = (0,  255,255)


# dictionary linking resources to colours
colours = {0 : GREY,
           1 : BLACK,
           2 : BROWN,
           3 : WHITE}
           
# a dictionary linking resources to textures
textures = {}

# tile maps for the different levels
tilemap_1_2 = [[1,1,1,1,1,1,1,1,1],
               [1,0,0,3,1,0,0,0,1],           
               [1,0,0,0,0,0,0,0,1],
               [1,0,0,0,1,0,0,0,1],           
               [1,1,0,1,1,1,0,1,1],           
               [1,0,0,0,1,0,0,0,1],           
               [1,0,0,0,1,0,0,0,1],           
               [1,0,0,0,1,0,0,0,1],           
               [1,1,1,1,1,1,1,1,1]]
               
tilemap_3 = [[0,0,0,0,1,1,1,1,1],
             [0,0,0,0,1,0,0,3,1],
             [0,0,0,0,1,0,0,0,1],
             [0,0,0,0,1,0,0,0,1],
             [0,0,0,0,1,1,1,1,1],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]  
             
# game dimensions
TILESIZE = 50 # bigger than the mouse
MAPWIDTH = 9
MAPHEIGHT= 9

# the player image
PLAYER = pygame.image.load('player.png')
BAT = pygame.image.load('bat.png')
PRINCESS = pygame.image.load('princess.png')

# playerposition depending on room
playerpos = {11:[2,2],
             12:[6,2],
             13:[2,6],
             14:[6,6],
             21:[2,2],
             22:[6,2],
             23:[2,6],
             24:[6,6],
             32:[6,2]}
             
# a dictionary linking a room to other positions
rooms = {
    00:{ "mission_eng" : "find the princess",
         "mission_ger" : "finde die Prinzessin"},

    11:{ "name" : "hall",
         "east" : [12,'opened'],
         "south": [13,'opened'],
         "up"   : [21,'opened'],
         "item" : ["torch"],
         "room" : [1,1]},
        
    12:{ "name" : "bedroom",
         "west" : [11,'opened'],
         "south": [14,'opened'],
         "room" : [1,5]},
        
    13:{ "name" : "kitchen",
         "north": [11,'opened'],
         "item" : ["sword"],
         "trigger": ["dark"],
         "room" : [5,1]},
        
    14:{ "name" : "bathroom",
         "detail":"You see traces of a fight, the sink is broken.",
         "north": [12,'opened'],
         "item" : ["soap"],
         "room" : [5,5]},
        
    21:{ "name" : "staircase",
         "detail":"You see a dusty old bookshelf.", 
         "east" : [22,'opened'],
         "south": [23,'opened','hidden','book'],
         "down" : [11,'opened'],
         "item" : ["torch"]},
        
    22:{ "name" : "corridor",
         "west" : [21,'opened'],
         "south": [24,'opened'],
         "up"   : [32,'locked'],
         "item" : ["torch"],
         "person": ["bat",1]},
        
    23:{ "name" : "terrace",
         "north": [21,'opened'],
         "trigger": ["dark"],
         "person": ["bat",1],
         "item" : ["key"]},
        
    24:{ "name" : "study",
         "north": [22,'opened'],
         "item" : ["book"]},
    
    32:{ "name" : "towerroom",
         "down" : [22,'locked'],
         "person" : ["princess",0]}
        }
    
# sorted to be used for the ring
directions = ['north','east','up','south','west','down']

# player position [x,y]
playerPos = playerpos[currentRoom]
personPos = [playerpos[11][0]-1,playerpos[11][1]-1]

# set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE+500,MAPHEIGHT*TILESIZE+100)) 

# loop through each row
for row in range(MAPHEIGHT):
    # loop through each column
    for column in range(MAPWIDTH):
        if currentRoom < 15:
            pygame.draw.rect(DISPLAYSURF, colours[tilemap_1_2[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
        elif currentRoom < 25:
            pygame.draw.rect(DISPLAYSURF, colours[tilemap_1_2[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
        else:
            pygame.draw.rect(DISPLAYSURF, colours[tilemap_3[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))  

while True:
    # predefine parameter    
    parameter = []
       
    # get all the user events
    for event in pygame.event.get():
        # if the user wants to quit
        if event.type == QUIT:
            # end the game and close the window
            pygame.quit()
            sys.exit()
        
        # if a key is pressed
        elif event.type == KEYDOWN:
            # change layout in current room
            # find start point
            x_start = rooms[currentRoom]['room'][0]
            y_start = rooms[currentRoom]['room'][1]
            for row in range(3):
                # loop through each column
                for column in range(3):
                    pygame.draw.rect(DISPLAYSURF, colours[0],((x_start + column)*TILESIZE,(y_start+row*TILESIZE),TILESIZE,TILESIZE))
                        
            
            # if the right arrow is pressed
            if (event.key == K_d):
                parameter = 'east'
                # check if the player can go into this direction
                if parameter in rooms[currentRoom].keys():
                    currentRoom = rooms[currentRoom][parameter][0]
                    # change the player's x position
                    playerPos = playerpos[currentRoom]
                            
            # if the left arrow is pressed
            if (event.key == K_a):
                parameter = 'west'
                # check if the player can go into this direction
                if parameter in rooms[currentRoom].keys():
                    currentRoom = rooms[currentRoom][parameter][0]
                    # change the player's x position
                    playerPos = playerpos[currentRoom]

            # if the up arrow is pressed
            if (event.key == K_w):
                parameter = 'north'
                # check if the player can go into this direction
                if parameter in rooms[currentRoom].keys():
                    currentRoom = rooms[currentRoom][parameter][0]
                    # change the player's x position
                    playerPos = playerpos[currentRoom]

            # if the down arrow is pressed
            if (event.key == K_s):
                parameter = 'south'
                # check if the player can go into this direction
                if parameter in rooms[currentRoom].keys():
                    currentRoom = rooms[currentRoom][parameter][0]
                    # change the player's x position
                    playerPos = playerpos[currentRoom]

            # if the plus is pressed
            if (event.key == K_UP):
                parameter = 'up'
                # check if the player can go into this direction
                if parameter in rooms[currentRoom].keys():
                    currentRoom = rooms[currentRoom][parameter][0]
                    # change the player's x position
                    playerPos = playerpos[currentRoom]

            # if the minus is pressed
            if (event.key == K_DOWN):
                parameter = 'down'
                # check if the player can go into this direction
                if parameter in rooms[currentRoom].keys():
                    currentRoom = rooms[currentRoom][parameter][0]
                    # change the player's x position
                    playerPos = playerpos[currentRoom]
            
            # if the q is pressed
            if (event.key == K_q):
                # end the game and close the window
                pygame.quit()
                sys.exit()                    
            
        if parameter == 'up' or parameter == 'down':
            # loop through each row
            for row in range(MAPHEIGHT):
                # loop through each column
                for column in range(MAPWIDTH):
                    if currentRoom < 15:
                        pygame.draw.rect(DISPLAYSURF, colours[tilemap_1_2[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                    elif currentRoom < 25:
                        pygame.draw.rect(DISPLAYSURF, colours[tilemap_1_2[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                    else:
                        pygame.draw.rect(DISPLAYSURF, colours[tilemap_3[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
        # change layout in current room
        # find start point
        x_start = rooms[currentRoom]['room'][0]
        y_start = rooms[currentRoom]['room'][1]
        for row in range(3):
            # loop through each column
            for column in range(3):
                pygame.draw.rect(DISPLAYSURF, colours[2],((x_start + column)*TILESIZE,(y_start+row*TILESIZE),TILESIZE,TILESIZE))
                        
                
    # display the player at the correct position
    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
    
    # display an enemy  if available
    if 'person' in rooms[currentRoom]:
        if rooms[currentRoom]['person'][1] == 0:
            personPos = [playerpos[currentRoom][0]+1,playerpos[currentRoom][1]+1]
            DISPLAYSURF.blit(PRINCESS,(personPos[0]*TILESIZE,personPos[1]*TILESIZE))
        if rooms[currentRoom]['person'][1] == 1:
            personPos = [playerpos[currentRoom][0]-1,playerpos[currentRoom][1]-1]
            DISPLAYSURF.blit(BAT,(personPos[0]*TILESIZE,personPos[1]*TILESIZE))
    
    # update the display
    pygame.display.update()
