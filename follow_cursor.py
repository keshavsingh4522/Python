# Author : John Smith
# Library / Framework used : Pygame
# Simple player follow cursor
import pygame
import random
import sys
import time

pygame.init()

black = (0,0,0)
white = (255,255,255)

movement_speed = 10
FPS = 60
width = 640
height = 480
ball = pygame.Rect(0,0,20,20)
ballSize = 5

varHeight = height
ballColor = white
bgColor = black

font = pygame.font.Font('freesansbold.ttf',10)
text = font.render('Left Click to Move',True,white)
textRect = text.get_rect()
textRect.center = (width//2,height//2)

gameOver = False

display = pygame.display.set_mode((width,height))
pygame.display.set_caption('Follow')

x,y = pygame.mouse.get_pos()
clock = pygame.time.Clock()
while not gameOver:
    display.fill(bgColor)
    display.blit(text,textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            ball.center=pygame.mouse.get_pos()



    pygame.draw.rect(display,ballColor,ball)
    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)



