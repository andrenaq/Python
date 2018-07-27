# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 10:32:54 2017

@author: andre
"""
from numpy import random as rd
def checkCollision(x,y,treasureX,treasureY):
    global screen, textWin
    collisionState = False
    if y>=treasureY and y<=treasureY + h:
        if x >= treasureX and x<= treasureX+h:
            collisionState = True
        elif x +30 >= treasureX and x +30 <= treasureX+h:
            collisionState = True
    elif y+30>=treasureY and y+30<=treasureY + h:
        if x >= treasureX and x<= treasureX+h:
            collisionState = True
        elif x+30 >= treasureX and x+30<= treasureX+h:
            collisionState = True
    return collisionState
import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
finished = False
x=20#-30/2
y=20
h=30
contador = True
x1,x2,x3,x4,x5,x6 = 60,120,240,340,360,440
y1,y2,y3,y4,y5,y6 = 40,320,100,200,300,400
treasureX = 320 - 30/2
treasureY = 240 - 30/2
color =(255,0,0)#R,G,B
black =(0,0,0)
white = (255,255,255)
playerImage =  pygame.image.load('player.jpg')
playerImage = pygame.transform.scale(playerImage,(30,30))
playerImage = pygame.transform.flip(playerImage,True,False)
playerImage = playerImage.convert_alpha()
enemyImage =  pygame.image.load('enemy.png')
enemyImage = pygame.transform.scale(enemyImage,(30,30))
enemyImage = enemyImage.convert_alpha()
backgroundImage = pygame.image.load('maze.jpeg')
backgroundImage = pygame.transform.scale(backgroundImage,(640,480))
#screen.blit(backgroundImage,(0,0))
treasureImage = pygame.image.load('treasure.png')
treasureImage = pygame.transform.scale(treasureImage,(h,h))
treasureImage = treasureImage.convert_alpha()
#screen.blit(treasureImage,(treasureX,treasureY))
font = pygame.font.SysFont("comicsansms", 60)
level = 1

teste = rd.randint(0,3)
frame = pygame.time.Clock()
collisionTreasure = False
collisionBad = False
while finished==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pressedKeys = pygame.key.get_pressed()        
    if pressedKeys[pygame.K_DOWN] == 1:
        y +=5
    if pressedKeys[pygame.K_UP] == 1:
        y -=5
    if pressedKeys[pygame.K_LEFT] == 1:
        x -=5
        playerImage = pygame.transform.flip(playerImage,True,False)
    if pressedKeys[pygame.K_RIGHT] == 1:
        x +=5    #rectOne=pygame.Rect(x,y,30,30)#x,y,width,height
        playerImage = pygame.transform.flip(playerImage,True,False)
    if contador == True:
        x1,x2,x3,x4,x5,x6 = x1+ rd.randint(0,3)*level,x2+ rd.randint(0,3)*level,x3+ rd.randint(0,3)*level,x4+ rd.randint(0,3)*level,x5+ rd.randint(0,3)*level,x6+ rd.randint(0,3)*level
        y1,y2,y3,y4,y5,y6 = y1 +rd.randint(0,3)*level,y2 +rd.randint(0,3)*level,y3 +rd.randint(0,3)*level,y4 +rd.randint(0,3)*level,y5 +rd.randint(0,3)*level,y6 +rd.randint(0,3)*level
        contador = False
    if contador == False:
        x1,x2,x3,x4,x5,x6 = x1+ rd.randint(0,3)*-level,x2+ rd.randint(0,3)*-level,x3+ rd.randint(0,3)*-level,x4+ rd.randint(0,3)*-level,x5+ rd.randint(0,3)*-level,x6+ rd.randint(0,3)*-level
        y1,y2,y3,y4,y5,y6 = y1 +rd.randint(0,3)*-level,y2 +rd.randint(0,3)*-level,y3 +rd.randint(0,3)*-level,y4 +rd.randint(0,3)*-level,y5 +rd.randint(0,3)*-level,y6 +rd.randint(0,3)*-level
        contador = True
    screen.blit(backgroundImage,(0,0))
    screen.blit(treasureImage,(treasureX,treasureY))
    screen.blit(enemyImage,(x1,y1))
    screen.blit(enemyImage,(x2,y2))
    screen.blit(enemyImage,(x3,y3))
    screen.blit(enemyImage,(x4,y4))
    screen.blit(enemyImage,(x5,y5))
    screen.blit(enemyImage,(x6,y6))
    if not collisionBad: collisionBad= checkCollision(x,y,x1,y1)
    if not collisionBad: collisionBad= checkCollision(x,y,x2,y2)
    if not collisionBad: collisionBad= checkCollision(x,y,x3,y3)
    if not collisionBad: collisionBad= checkCollision(x,y,x4,y4)
    if not collisionBad: collisionBad= checkCollision(x,y,x5,y5)
    if not collisionBad: collisionBad= checkCollision(x,y,x6,y6)
    screen.blit(playerImage,(x,y))
    #screen.blit(textWin,(320,249))
    collisionTreasure= checkCollision(x,y,treasureX,treasureY)
    if collisionTreasure: 
        level +=1
        textWin = font.render("You've reached lvl {}".format(level),True,(black))
        screen.blit(textWin,(320 - textWin.get_width()/2,240-textWin.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
        x,y = 0,0
        x1,x2,x3,x4,x5,x6 = 60,120,240,340,360,440
        y1,y2,y3,y4,y5,y6 = 40,320,100,200,300,400
    if collisionBad:
        level =1
        textWin = font.render("You've Lost you",True,(black))
        screen.blit(textWin,(320 - textWin.get_width()/2,240-textWin.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
        collisionBad = False
        x1,x2,x3,x4,x5,x6 = 60,120,240,340,360,440
        y1,y2,y3,y4,y5,y6 = 40,320,100,200,300,400
        x,y = 0,0   
    #pygame.draw.rect(screen,color,rectOne)
    pygame.display.flip() #update the screen  
    frame.tick(30)