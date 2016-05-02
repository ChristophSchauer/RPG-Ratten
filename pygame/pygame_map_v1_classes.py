# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 19:17:26 2016

@author: Christoph
"""

'''
usingpython: PYgame Tilemaps
following are the different levels and the colors
'''
import pygame, sys
from pygame.locals import *
 

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
           
# a dictionary linking resources to textures
textures = {}
            
# game dimensions
TILESIZE = 50 # bigger than the mouse
MAPWIDTH = 9
MAPHEIGHT= 9
DX = 500
DY = 100

# player position [x,y]
playerPos = playerpos[currentRoom]


while True:    
        # if a key is pressed
        elif event.type == KEYDOWN:
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
            
    
    
class Main:
    '''
    handles the game initialization and the creation of the map
    '''
    def __init__(self, TILESIZE, MAPWIDTH, MAPHEIGHT, DX, DY):
        # initialize        
        pygame.init()
        self.tilesize = TILESIZE
        self.mapwidth = MAPWIDTH
        self.mapheight = MAPHEIGHT
        self.dx = DX
        self.dy = DY
        # set up the display
        self.DISPLAYSURF = pygame.display.set_mode((self.mapheight*self.tilesize+self.dx,self.mapheight*self.tilesize+self.dy))
        
        self.parameters()
        
        self.floors()
        
    def mainloop(self):
        # load the sprites
        self.loadSprites()
        
        # infinite loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.player.move(event.key,self.rooms)#
            # loop through each row
            for row in range(self.mapheight):
                # loop through each column
                for column in range(self.mapwidth):
                    if self.currentRoom < 15:
                        pygame.draw.rect(DISPLAYSURF, colours[tilemap_1_2[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                    elif currentRoom < 25:
                        pygame.draw.rect(DISPLAYSURF, colours[tilemap_1_2[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                    else:
                        pygame.draw.rect(DISPLAYSURF, colours[tilemap_3[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                        
                
            # display the player at the correct position
            DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
            
            if 'person' in rooms[currentRoom]:
                if rooms[currentRoom]['person'][1] == 0:
                    personPos = [playerpos[currentRoom][0]+1,playerpos[currentRoom][1]+1]
                    DISPLAYSURF.blit(PRINCESS,(personPos[0]*TILESIZE,personPos[1]*TILESIZE))
                if rooms[currentRoom]['person'][1] == 1:
                    personPos = [playerpos[currentRoom][0]-1,playerpos[currentRoom][1]-1]
                    DISPLAYSURF.blit(BAT,(personPos[0]*TILESIZE,personPos[1]*TILESIZE))
            
            # update the display
            pygame.display.update()
                
    def loadSprites(self):
        # the player image
        self.PLAYER = pygame.image.load('player.png')
        self.BAT = pygame.image.load('bat.png')
        self.PRINCESS = pygame.image.load('princess.png')
        
    def parameters(self):
        # color of the tiles
        self.BLACK = (0,  0,  0  )
        self.WHITE = (255,255,255)
        self.BROWN = (153,76, 0  )
        self.GREEN = (0,  255,0  )
        self.RED   = (255,0,  0  )
        self.BLUE  = (0,  0,  255)
        # dictionary linking resources to colours
        self.colours = {1:BLACK,
                        0:BROWN}  
        # sorted to be used for the ring
        self.directions = ['north','east','up','south','west','down']
                        
    def floors(self):
        # tile maps for the different levels
        self.tilemap_1_2 = [[1,1,1,1,1,1,1,1,1],
                            [1,0,0,0,1,0,0,0,1],           
                            [1,0,0,0,0,0,0,0,1],
                            [1,0,0,0,1,0,0,0,1],           
                            [1,1,0,1,1,1,0,1,1],           
                            [1,0,0,0,1,0,0,0,1],           
                            [1,0,0,0,1,0,0,0,1],           
                            [1,0,0,0,1,0,0,0,1],           
                            [1,1,1,1,1,1,1,1,1]]
                       
        self.tilemap_3 = [[0,0,0,0,1,1,1,1,1],
                          [0,0,0,0,1,0,0,0,1],
                          [0,0,0,0,1,0,0,0,1],
                          [0,0,0,0,1,0,0,0,1],
                          [0,0,0,0,1,1,1,1,1],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0]] 
        
        # a dictionary linking a room to other positions
        self.rooms = {
            00:{ "mission_eng" : "find the princess",
                 "mission_ger" : "finde die Prinzessin"},
        
            11:{ "name" : "hall",
                 "east" : [12,'opened'],
                 "south": [13,'opened'],
                 "up"   : [21,'opened'],
                 "item" : ["torch"]},
                
            12:{ "name" : "bedroom",
                 "west" : [11,'opened'],
                 "south": [14,'opened'],},
                
            13:{ "name" : "kitchen",
                 "north": [11,'opened'],
                 "item" : ["sword"],
                 "trigger": ["dark"]},
                
            14:{ "name" : "bathroom",
                 "detail":"You see traces of a fight, the sink is broken.",
                 "north": [12,'opened'],
                 "item" : ["soap"]},
                
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

class player():
    def __init__(self):
        # playerposition depending on room
        self.playerpos = {11:[2,2],
                          12:[6,2],
                          13:[2,6],
                          14:[6,6],
                          21:[2,2],
                          22:[6,2],
                          23:[2,6],
                          24:[6,6],
                          32:[6,2]} 
        # currentRoom
        self.currentRoom = 11
    def move(self,key,rooms):
        # get all the user events
        if (key == K_d):
                parameter = 'east'
                # check if the player can go into this direction
                if parameter in rooms[currentRoom].keys():
                    currentRoom = rooms[currentRoom][parameter][0]
                    # change the player's x position
                    playerPos = playerpos[currentRoom]
        
        