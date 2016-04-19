# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:48:25 2016

@author: Christoph

Hist:
[2016.04.19, CS]:   implement the first version of the GUI;
"""

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()