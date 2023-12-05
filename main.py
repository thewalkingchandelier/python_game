import pygame

import time

import random

 

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("space.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40

PLAYER_HEIGHT = 60

PLAYER_VEL = 5

 

def draw(player):

    WIN.blit(BG, (0,0)) #use this function whenever we want to draw something on the window where the coordinates are the top left of the image should be placed

   

    pygame.draw.rect(WIN, "red", player)

 

    pygame.display.update()

   

    

# the main fuction is where we will write our code

# the run while loop will determin if the game will run based on if the window is open or closed

 

def main():

    run = True

 

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

 

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

                break

 

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            player.x -= PLAYER_VEL

 

        draw(player)      

    pygame.quit()

 

if __name__ == "__main__":

    main()
