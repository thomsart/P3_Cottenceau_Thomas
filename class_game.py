#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import random

import pygame
from pygame.locals import *


""" This file contains all classes and methodes' objets of the game. For more clarity we decide to separate 
the logique (class_game.py) from the executable (game.py) """

pygame.init()  # initialisation of all modules in pygame

window = pygame.display.set_mode((600, 600)) # creation of the MacGyver game's window

class Items(pygame.sprite.Sprite): # we create a class for the items to catch

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)          
        self.image = pygame.image.load("ressource/needle.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)


def put_items(): # and then we create a methode to put items randomly in the maze

    positions_items = [(60,460),(140,340),(340,540),(540,380),(540,60),(460,180),
    (300,60),(180,220),(300,140)] # we choose the places

    needle = Items()
    needle.image = pygame.image.load("ressource/needle.png").convert()
    random_position = random.choice(positions_items)
    needle.rect.center = random_position  # we attribute randomly the place from position_items
    positions_items.remove(random_position) # to avoid that two items get the same place

    tube = Items()
    tube.image = pygame.image.load("ressource/tube.png").convert()
    random_position = random.choice(positions_items)
    tube.rect.center = random_position
    positions_items.remove(random_position)
    
    ether = Items()
    ether.image = pygame.image.load("ressource/ether.png").convert()
    random_position = random.choice(positions_items)
    ether.rect.center = random_position

    group_items = pygame.sprite.Group()
    group_items.add(needle) # we put all items in the group made for, and update it to draw
    group_items.add(tube)
    group_items.add(ether)
    group_items.update() 
    group_items.draw(window)
            
    return group_items


class Gard(pygame.sprite.Sprite): # we create a class only fo the gard

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ressource/gard.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (580, 300)


class MacGyver(pygame.sprite.Sprite): # finally we create the player MacGyver in the same way.

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ressource/macgyver.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (20, 300)

    def up(self): # the moves of MacGver are mades by four methodes from his class.
        self.rect.y -= 40

    def right(self):
        self.rect.x += 40

    def down(self):
        self.rect.y += 40

    def left(self):
        self.rect.x -= 40