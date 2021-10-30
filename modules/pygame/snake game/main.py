__author__ = "Ran Crump"

import os
import sys
import pygame
import random
from pygame import *

pygame.init()

scr_size = (width,height) = (600,600)
FPS = 30

black = (0,0,0)
white = (255,255,255)
background_col = (235,235,235)

high_score = 0

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")

eat_sound = pygame.mixer.Sound('sounds/snake_eat.wav')
move_sound = pygame.mixer.Sound('sounds/snake_move.wav')
game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')

def load_image(
    name,
    sizex=-1,
    sizey=-1,
    colorkey=None,
    ):

    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

def load_sprite_sheet(
        sheetname,
        nx,
        ny,
        scalex = -1,
        scaley = -1,
        colorkey = None,
        ):
    fullname = os.path.join('sprites',sheetname)
    sheet = pygame.image.load(fullname)
    sheet = sheet.convert()

    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i in range(0,ny):
        for j in range(0,nx):
            rect = pygame.Rect((j*sizex,i*sizey,sizex,sizey))
            image = pygame.Surface(rect.size)
            image = image.convert()
            image.blit(sheet,(0,0),rect)

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey,RLEACCEL)

            if scalex != -1 or scaley != -1:
                image = pygame.transform.scale(image,(scalex,scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()

    return sprites,sprite_rect

def disp_gameOver_msg(retbutton_image,gameover_image):
    retbutton_rect = retbutton_image.get_rect()
    retbutton_rect.centerx = width / 2
    retbutton_rect.top = height*0.52

    gameover_rect = gameover_image.get_rect()
    gameover_rect.centerx = width / 2
    gameover_rect.centery = height*0.35

    screen.blit(retbutton_image, retbutton_rect)
    screen.blit(gameover_image, gameover_rect)

def extractDigits(number):
    if number > -1:
        digits = []
        i = 0
        while(number/10 != 0):
            digits.append(number%10)
            number = int(number/10)

        digits.append(number%10)
        for i in range(len(digits),5):
            digits.append(0)
        digits.reverse()
        return digits

class Snake():
    def __init__(self,sizex=-1,sizey=-1):
        self.head,self.head_rect = load_image('snek_head.png',25,25,1)
        self.body,self.body_rect = load_image('snek_body.png',25,25,1)        
        self.tail,self.tail_rect = load_image('snek_body.png',25,25,1)
        self.head_rect.bottom = int(0.5*height)+200
        self.head_rect.left = int(0.5*height)
        self.body_rect.bottom = int(0.5*height)+200
        self.body_rect.left = int(0.5*height)
        self.index = 0
        self.speed = 25
        self.counter = 0
        self.score = 0
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.isDead = False
        self.isMoving = False
        self.movement = [0,0]
        self.velocity = [self.speed,0]
        self.length = 1
        self.tail = []

    def draw(self):
        self.tail.insert(0, self.body_rect)
        for i in range(self.length):
            if i > 0:
                screen.blit(self.body, self.tail[i])    

        rotation = 0
        if (self.up):
            rotation = 90
        if (self.left):
            rotation = 180
        if (self.down):
            rotation = 270        

        headOrentiation = pygame.transform.rotate(self.head, rotation)
        screen.blit(headOrentiation,self.head_rect)

    def direction(self, dir):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        if (dir == 'UP'):
            self.up = True
        if (dir == 'Down'):
            self.down = True
        if (dir == 'Left'):
            self.left = True
        if (dir == 'Right'):
            self.right = True

    def restart(self):
        self.head_rect.bottom = int(0.5*height)+200
        self.head_rect.left = int(0.5*height)
        self.body_rect.bottom = int(0.5*height)+200
        self.body_rect.left = int(0.5*height)
        self.isDead = False
        self.length = 1
        self.tail = []
        self.velocity = [self.speed,0]
        self.up = False
        self.down = False
        self.left = False
        self.right = True

    def addTail(self):
        self.length = self.length+1

    def checkbounds(self):        
        #Top
        if self.head_rect.top < 0:
            self.isDead = True
            self.head_rect.top = 0
        #Bottom
        if self.head_rect.bottom > int(height):
            self.isDead = True
            self.head_rect.bottom = int(height)
        #Left
        if self.head_rect.left < 0:
            self.isDead = True
            self.head_rect.left = 0
        #Right
        if self.head_rect.left > int(width)-25:
            self.isDead = True
            self.head_rect.left = int(width)-25

        if (self.length > 1):
            for i in range(self.length):
                if int(self.head_rect.left) == self.tail[i].left and int(self.head_rect.bottom) == self.tail[i].bottom:
                    self.isDead = True

    def update(self):

        if self.up:
            self.index = 0
        elif self.down:
            self.index = 1
        elif self.left:
            self.index = 2
        elif self.right:
            self.index = 3

        if self.isDead:
           self.index = 4

        self.body_rect = self.body_rect.move(self.movement)
        self.head_rect = self.head_rect.move(self.movement)
        self.checkbounds()

class Banana():
    def __init__(self):
        self.image,self.rect = load_image('bananas.png', 25, 25, -1)
        self.rect.left = (random.randint(1,24) * 25)-25
        self.rect.bottom = (random.randint(1,24) * 25)

    def draw(self):
        screen.blit(self.image,self.rect)

    def checkbounds(self, snake):
        if int(self.rect.left) == int(snake.head_rect.left) and int(self.rect.bottom) == int(snake.head_rect.bottom):
            self.rect.left = (random.randint(1,24) * 25)-25
            self.rect.bottom = (random.randint(1,24) * 25)
            eat_sound.play()
            snake.addTail()
            return True

    def update(self, snake):
        return self.checkbounds(snake)

class Scoreboard():
    def __init__(self,x=-1,y=-1):
        self.score = 0
        self.tempimages,self.temprect = load_sprite_sheet('numbers.png',12,1,11,int(11*6/5),-1)
        self.image = pygame.Surface((55,int(11*6/5)))
        self.rect = self.image.get_rect()
        if x == -1:
            self.rect.left = width*0.89
        else:
            self.rect.left = x
        if y == -1:
            self.rect.top = height*0.1
        else:
            self.rect.top = y

    def draw(self):
        screen.blit(self.image,self.rect)

    def update(self,score):
        score_digits = extractDigits(score)
        self.image.fill(background_col)
        for s in score_digits:
            self.image.blit(self.tempimages[s],self.temprect)
            self.temprect.left += self.temprect.width
        self.temprect.left = 0


def introscreen():
    temp_Snake = Snake(25,25)    
    gameStart = False

    temp_ground,temp_ground_rect = load_image('ground.png', 600, 600, 1)
    temp_ground_rect.left = 0
    temp_ground_rect.bottom = 600

    logo,logo_rect = load_image('logo.png',300,300,-1)
    logo_rect.centerx = (width*0.5)
    logo_rect.centery = (height*0.5)
    while not gameStart:
        if pygame.display.get_surface() == None:
            print("Couldn't load display surface")
            return True
        else:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:                    
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        temp_Snake.isMoving = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        temp_Snake.isMoving = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        temp_Snake.isMoving = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        temp_Snake.isMoving = True

        if pygame.display.get_surface() != None:
            screen.fill(background_col)
            screen.blit(temp_ground,temp_ground_rect)
            screen.blit(logo,logo_rect)
        
        temp_Snake.update()
        temp_Snake.draw()

        if temp_Snake.isMoving:
            gameStart = True

        pygame.display.update()

        clock.tick(FPS)        

    gameplay()

def gameplay():
    global high_score
    gamespeed = 1
    startMenu = False
    gameOver = False
    gameQuit = False
    playerSnake = Snake(25,25)
    banana = Banana()
    ground,ground_rect = load_image('ground.png', 600, 600, 1)
    ground_rect.left = 0
    ground_rect.bottom = 600
    scb = Scoreboard()
    highsc = Scoreboard(width*0.78)

    retbutton_image,retbutton_rect = load_image('replay_button.png',35,31,-1)
    gameover_image,gameover_rect = load_image('game_over.png', 600,200,-1)

    temp_images,temp_rect = load_sprite_sheet('numbers.png',12,1,11,int(11*6/5),-1)
    HI_image = pygame.Surface((22,int(11*6/5)))
    HI_rect = HI_image.get_rect()
    HI_image.fill(background_col)
    HI_image.blit(temp_images[10],temp_rect)
    temp_rect.left += temp_rect.width
    HI_image.blit(temp_images[11],temp_rect)
    HI_rect.top = height*0.1
    HI_rect.left = width*0.73

    while not gameQuit:
        while startMenu:
            pass
        while not gameOver:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                gameQuit = True
                gameOver = True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameQuit = True
                        gameOver = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            playerSnake.velocity = [0,-playerSnake.speed]
                            playerSnake.direction('UP')
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            playerSnake.velocity = [0,playerSnake.speed]
                            playerSnake.direction('Down')
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            playerSnake.velocity = [-playerSnake.speed,0]
                            playerSnake.direction('Left')
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            playerSnake.velocity = [playerSnake.speed,0]
                            playerSnake.direction('Right')

            playerSnake.movement = playerSnake.velocity
            playerSnake.update()
            scb.update(playerSnake.score)
            highsc.update(high_score)
            
            # Check if it ate a banana
            if (banana.update(playerSnake)):
                playerSnake.score = playerSnake.score+1

            if pygame.display.get_surface() != None:
                screen.fill(background_col)
                screen.blit(ground,ground_rect)                
                scb.draw()
                banana.draw()
                highsc.draw()
                screen.blit(HI_image,HI_rect)
                playerSnake.draw()

                pygame.display.update()    

            move_sound.play()
            clock.tick(FPS/4)

            # On Eat Banana
            #playerSnake.score

            if playerSnake.score > high_score:
                high_score = playerSnake.score

            if playerSnake.isDead:
                gameOver = True
                game_over_sound.play()
                playerSnake.score = 0

        if gameQuit:
            break

        while gameOver:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                gameQuit = True
                gameOver = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameQuit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameQuit = True
                            gameOver = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                gameOver = False
                                playerSnake.restart()
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                gameOver = False
                                playerSnake.restart()
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                gameOver = False
                                playerSnake.restart()
                            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                gameOver = False
                                playerSnake.restart()

            highsc.update(high_score)
            if pygame.display.get_surface() != None:
                disp_gameOver_msg(retbutton_image,gameover_image)
                if high_score != 0:
                    highsc.draw()
                    screen.blit(HI_image,HI_rect)
                pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
    quit()

def main():
    isGameQuit = introscreen()
    if not isGameQuit:
        gameplay()

main()
