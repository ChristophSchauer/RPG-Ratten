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
 
# currentRoom
currentRoom = 11

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

# color of the tiles
BLACK = (0,  0,  0  )
WHITE = (255,255,255)
BROWN = (153,76, 0  )
GREEN = (0,  255,0  )
RED   = (255,0,  0  )
BLUE  = (0,  0,  255) 

# dictionary linking resources to colours
colours = {4:BLUE,
           3:GREEN,
           2:WHITE,
           1:BLACK,
           0:BROWN}
           
# a dictionary linking resources to textures
textures = {}

# tile maps for the different levels
'''
# old
tilemap_1 = [[1,1,1,1,1,1,1,1,1],
             [1,0,0,2,1,0,0,0,1],           
             [1,0,0,0,0,0,0,0,1],
             [1,0,0,0,1,0,0,0,1],           
             [1,1,0,1,1,1,0,1,1],           
             [1,0,0,0,1,0,0,0,1],           
             [1,0,0,0,1,0,0,0,1],           
             [1,0,0,0,1,0,0,0,1],           
             [1,1,1,1,1,1,1,1,1]]
               
tilemap_2 = [[1,1,1,1,1,1,1,1,1],
             [1,0,0,0,1,0,0,2,1],           
             [1,0,0,0,0,0,0,0,1],
             [1,0,0,0,1,0,0,0,1],           
             [1,1,0,1,1,1,0,1,1],           
             [1,0,0,0,1,0,0,0,1],           
             [1,0,0,0,1,0,0,0,1],           
             [1,0,0,0,1,0,0,0,1],           
             [1,1,1,1,1,1,1,1,1]]
               
tilemap_3 = [[0,0,0,0,1,1,1,1,1],
             [0,0,0,0,1,0,0,0,1],
             [0,0,0,0,1,0,0,0,1],
             [0,0,0,0,1,0,0,0,1],
             [0,0,0,0,1,1,1,1,1],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]
'''             
tielmap_level_1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#1
                   [1,0,0,3,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,3,1],
                   [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],#3
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1],#5
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1],#7
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],#9
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1],#11
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],#13
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1],#15
                   [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
                   [1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1],#17
                   [1,0,0,0,1,0,1,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,1,0,1,0,0,0,1],
                   [1,0,4,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],#19
                   [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
                   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]#21 
             
tilemap_level_2 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#1
                   [1,0,0,3,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,3,1],
                   [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],#3
                   [1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
                   [1,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1],#5
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],#7
                   [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],#9
                   [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
                   [1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1],#11
                   [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],#13
                   [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
                   [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],#15
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1],#17
                   [1,0,0,0,1,0,1,0,0,2,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,2,1,0,1,0,0,0,1],
                   [1,0,4,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1],#19
                   [1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
                   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]#21
                                      
tielmap_level_3 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#1
                   [1,0,0,3,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,3,1],
                   [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],#3
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1],#5
                   [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                   [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],#7
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],#9
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1],#11
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,2,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1],#13
                   [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
                   [1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1],#15
                   [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
                   [1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1],#17
                   [1,0,0,0,1,0,1,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,1,0,1,0,0,0,1],
                   [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],#19
                   [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
                   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]#21                   
                   
# game dimensions
'''
# old            
TILESIZE = 50 # bigger than the mouse
MAPWIDTH = 9
MAPHEIGHT= 9
DX = 500
DY = 100
'''

TILEHEIGHT = 11
TILEWIDTH = 12
MAPWIDTH = 33*TILEWIDTH     # 396px
MAPHEIGHT = 21*TILEHEIGHT   # 231px

# the player image
'''
# old
PLAYER = pygame.image.load('player.png')
BAT = pygame.image.load('bat.png')
PRINCESS = pygame.image.load('princess.png')
'''
PLAYER = pygame.image.load('player_new.png')
BAT = pygame.image.load('bat_new.png')
PRINCESS = pygame.image.load('princess_new.png')

# playerposition depending on room
'''
# old
playerpos = {11:[2,2],
             12:[6,2],
             13:[2,6],
             14:[6,6],
             21:[2,2],
             22:[6,2],
             23:[2,6],
             24:[6,6],
             32:[6,2]}
'''
             
# a dictionary linking a room to other positions
'''
# old
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
'''

        
rooms = {# level 2
         211:{"name" : "stairs",
              "detail":"",
              "east" : [212,'opened'],
              #"up"   : [311,'opened'],
              #"down" : [111,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         212:{"name" : "corridor",
              "detail":"",
              "south" : [222,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         213:{"name" : "office",
              "detail":"",
              "south": [223,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         214:{"name" : "office",
              "detail":"",
              "south": [224,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         215:{"name" : "office",
              "detail":"",
              "south": [225,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         216:{"name" : "office",
              "detail":"",
              "south": [226,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         217:{"name" : "office",
              "detail":"",
              "south": [227,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         218:{"name" : "corridor",
              "detail":"",
              "south": [228,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         219:{"name" : "stairs",
              "detail":"",
              "west" : [218,'opened'],
              #"up"   : [319,'opened'],
              #"down" : [119,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
                         
         221:{"name" : "corridor",
              "detail":"",
              "east" : [222,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         222:{"name" : "corridor",
              "detail":"",
              "north": [212,'opened'],
              "east" : [223,'opened'],
              "south": [232,'opened'],
              "west" : [221,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         223:{"name" : "corridor",
              "detail":"",
              "north": [213,'opened'],
              "east" : [224,'opened'],
              "west" : [222,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         224:{"name" : "corridor",
              "detail":"",
              "north": [214,'opened'],
              "east" : [225,'opened'],
              "west" : [223,'opened'],
              "south": [234,'opened'], #to foodstuff
              "item" : [],
              "person" : [],
              "trigger": []},
         225:{"name" : "corridor",
              "detail":"",
              "north": [215,'opened'],
              "east" : [226,'opened'],
              "west" : [224,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         226:{"name" : "corridor",
              "detail":"",
              "north": [216,'opened'],
              "east" : [227,'opened'],
              "west" : [225,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         227:{"name" : "corridor",
              "detail":"",
              "north": [217,'opened'],
              "east" : [228,'opened'],
              "west" : [226,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         228:{"name" : "corridor",
              "detail":"",
              "north": [218,'opened'],
              "east" : [229,'opened'],
              "south": [238,'opened'],
              "west" : [227,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         229:{"name" : "corridor",
              "detail":"",
              "west" : [228,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},

         231:{"name" : "office",
              "detail":"",
              "east": [232,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         232:{"name" : "corridor",
              "detail":"",
              "north": [222,'opened'],
              "east" : [233,'opened'],
              "south": [242,'opened'],
              "west" : [231,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         233:{"name" : "office",
              "detail":"",
              "west": [232,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         234:{"name" : "foodstuff",
              "detail":"",
              "north": [224,'opened'],
              "east" : [235,'opened'],
              "south": [244,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         235:{"name" : "foodstuff",
              "detail":"",
              "east" : [236,'opened'],
              "south": [245,'opened'],
              "west" : [234,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         236:{"name" : "foodstuff",
              "detail":"",
              "south": [246,'opened'],
              "west" : [235,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         237:{"name" : "office",
              "detail":"",
              "east": [238,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         238:{"name" : "corridor",
              "detail":"",
              "north": [228,'opened'],
              "east" : [239,'opened'],
              "south": [248,'opened'],
              "west" : [237,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         239:{"name" : "office",
              "detail":"",
              "west": [238,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},

         241:{"name" : "office",
              "detail":"",
              "east": [242,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         242:{"name" : "corridor",
              "detail":"",
              "north": [232,'opened'],
              "east" : [243,'opened'],
              "south": [252,'opened'],
              "west" : [241,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         243:{"name" : "office",
              "detail":"",
              "west": [242,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         244:{"name" : "foodstuff",
              "detail":"",
              "north": [234,'opened'],
              "east" : [245,'opened'],
              "south": [254,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         245:{"name" : "foodstuff",
              "detail":"",
              "north": [235,'opened'],
              "east" : [246,'opened'],
              "west" : [244,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         246:{"name" : "foodstuff",
              "detail":"",
              "north": [236,'opened'],
              "west" : [245,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         247:{"name" : "office",
              "detail":"",
              "east": [248,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         248:{"name" : "corridor",
              "detail":"",
              "north": [238,'opened'],
              "east" : [249,'opened'],
              "south": [258,'opened'],
              "west" : [247,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         249:{"name" : "office",
              "detail":"",
              "west": [248,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},

         251:{"name" : "corridor",
              "detail":"",
              "east" : [252,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         252:{"name" : "corridor",
              "detail":"",
              "north": [242,'opened'],
              "east" : [253,'opened'],
              "south": [262,'opened'],
              "west" : [251,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         253:{"name" : "corridor",
              "detail":"",
              "east" : [254,'opened'],
              "south": [263,'opened'],
              "west" : [252,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         254:{"name" : "corridor",
              "detail":"",
              "north": [244,'opened'], #to foodstuff
              "east" : [255,'opened'],
              "south": [264,'opened'],
              "west" : [253,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         255:{"name" : "corridor",
              "detail":"",
              "east" : [256,'opened'],
              "south": [265,'opened'],
              "west" : [254,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         256:{"name" : "corridor",
              "detail":"",
              "east" : [257,'opened'],
              "south": [266,'opened'],
              "west" : [255,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         257:{"name" : "corridor",
              "detail":"",
              "east" : [258,'opened'],
              "south": [267,'opened'],
              "west" : [256,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         258:{"name" : "corridor",
              "detail":"",
              "north": [248,'opened'],
              "east" : [259,'opened'],
              "south": [268,'opened'],
              "west" : [257,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         259:{"name" : "corridor",
              "detail":"",
              "west" : [258,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},

         261:{"name" : "office",
              "detail":"",
              "east": [262,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         262:{"name" : "corridor",
              "detail":"",
              "north": [252,'opened'],
              "west" : [261,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         263:{"name" : "elevator",
              "detail":"",
              "north": [253,'opened'],
              #"up"   : [363,'opened'],
              #"down" : [163,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         264:{"name" : "office",
              "detail":"",
              "north": [254,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         265:{"name" : "office",
              "detail":"",
              "north": [255,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         266:{"name" : "office",
              "detail":"",
              "north": [256,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         267:{"name" : "elevator",
              "detail":"",
              "north": [257,'opened'],
              #"up"   : [367,'opened'],
              #down" : [167,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         268:{"name" : "corridor",
              "detail":"",
              "north": [258,'opened'],
              "east" : [269,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []},
         269:{"name" : "office",
              "detail":"",
              "west": [268,'opened'],
              "item" : [],
              "person" : [],
              "trigger": []}}
    
# sorted to be used for the ring
directions = ['north','east','up','south','west','down']

# player position [x,y]
playerPos = playerpos[currentRoom]
personPos = [playerpos[11][0]-1,playerpos[11][1]-1]

# initialize        
pygame.init()
# set up the display
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE+DX,MAPHEIGHT*TILESIZE+DY))   

while True:   
       
    # get all the user events
    for event in pygame.event.get():
        # if the user wants to quit
        if event.type == QUIT:
            # end the game and close the window
            pygame.quit()
            sys.exit()
        
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
            
    # loop through each row
    for row in range(MAPHEIGHT):
        # loop through each column
        for column in range(MAPWIDTH):
            if currentRoom < 15:
                pygame.draw.rect(DISPLAYSURF, colours[tilemap_1[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
            elif currentRoom < 25:
                pygame.draw.rect(DISPLAYSURF, colours[tilemap_2[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
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
