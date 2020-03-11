#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pygame
from pygame.locals import *



""" This file contains the structure of the maze. The idea is to create-
the class Brick in order to build the maze with brick's sprites. """

pygame.init()  # initialisation of all modules in pygame

window = pygame.display.set_mode((600, 600)) # creation of the MacGyver game's window

class Brick(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("ressource/brick.png").convert()
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0
        
def build_maze():

    group_brick = pygame.sprite.Group()
    points_x = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560,]

    # creation of the line 1 until 15

    for elm in points_x: # the first line
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 0
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)
        
    for elm in points_x: # and the last line
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 560
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)
        
    line02 = [0, 200, 320, 480, 560]
    for elm in line02:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 40
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line03 = [0, 80, 120, 200, 280, 320, 400, 560]
    for elm in line03:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 80
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line04 = [0, 80, 120, 200, 320, 400, 440, 480, 560]
    for elm in line04:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 120
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line05 = [0, 120, 200, 280, 320, 400, 480, 560]
    for elm in line05:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 160
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line06 = [0, 40, 120, 200, 320, 400, 480, 560]
    for elm in line06:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 200
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line07 = [0, 120, 160, 200, 240, 400, 480, 560]
    for elm in line07:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 240
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line08 = [80, 320, 400, 480]
    for elm in line08:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 280
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line09 = [0, 80, 160, 200, 240, 280, 320, 400, 480, 520, 560]
    for elm in line09:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 320
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line10 = [0, 120, 320, 400, 480, 560]
    for elm in line10:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 360
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line11 = [0, 40, 200, 240, 320, 400, 480, 560]
    for elm in line11:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 400
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line12 = [0, 80, 120, 160, 200, 240, 400, 480, 560]
    for elm in line12:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 440
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line13 = [0, 120, 320, 400, 480, 560]
    for elm in line13:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 480
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    line14 = [0, 40, 200, 280, 560]
    for elm in line14:
        brick = Brick()
        brick.rect.x = elm
        brick.rect.y = 520
        group_brick.add(brick)
        group_brick.update()
        group_brick.draw(window)

    return group_brick



