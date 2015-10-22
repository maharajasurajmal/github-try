import pygame
from classes import *

pygame.init()

#global variables
display_width = 800
display_height = 600
player1 = player()

#color variables
black = (0,0,0)
white = (255,255,255)

# main pygame variables
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()


def menu():
    pass

def gameinit():
    #initialise player
    player1.x = 0.0                 #already initalized while defining
    player1.y = 0.0
    player1.health = 100
    player1.speed = 0.0
    #etc
            

def gameloop():
   
    quit = False
    while quit == False:

   	    #events
        for event in pygame.event.get():
        
            # event - quit
            if event.type == pygame.QUIT:
                quit = True

            #this event runs when any key is pressed
        pressed_keys = pygame.key.get_pressed()
    +        if pressed_keys[pygame.K_LEFT] == True:
    +            player1.move('left')
    +        if pressed_keys[pygame.K_RIGHT] == True:
    +            player1.move('right')
    +        if pressed_keys[pygame.K_UP] == True:
    +            player1.move('up')
    +        if pressed_keys[pygame.K_DOWN] == True:
    +            player1.move('down')


            #used for debugging
            


        #logic
        player1.inertia()
        

	    #map draw
        gameDisplay.fill(white)
        draw(player1)

        pygame.display.update()
        clock.tick(60)


def collide(obj1,obj2):
        #obj1 is the object moving and obj2 is the object which is fixed

        if obj1.x >= obj2.x and obj1.x <= (obj2x+ obj2.w) and obj1.y >= obj2.y and obj1.y <= obj2.y+ obj2.h:
            self.can_collide = True
        #if player approaches from right
        elif obj1.x >= obj2.x and obj1.x <= (obj2.x+ obj2.w) and obj1.y + obj1.h >= obj2.y and obj1.y + obj1.h <= obj2.y + obj2.h:
            can_collide = True
        #if player approaches from left
        elif  obj1.x + obj1.w >= obj2.x and obj1.x +obj1.w <= (obj2.x+ obj2.w) and obj1.y >= obj2.y and obj1.y <= (obj2.y+ obj2.h):
            self.can_collide = True
        #if plater approaches from top
        elif (obj1.x+ obj1.w) >= obj2.x and (obj1.x+ obj1.w) <= (obj2.x + obj2.w) and obj1.y+ obj1.h >= obj2.y and obj1.y+ obj1.h <= (obj2.y + obj2.h):

            self.can_collide = True


def gameexit():
    #runs before closing the window
    pygame.quit()
    quit()


def draw(obj):
    #used to draw any object sent to it on the screen
    gameDisplay.blit(obj.image, (obj.x,obj.y))


# main code
gameinit()
gameloop()
gameexit()
