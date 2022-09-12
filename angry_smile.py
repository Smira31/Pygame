import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)



# circle
pygame.draw.circle(screen, YELLOW, (200, 200), 150)
circle(screen, BLACK, (200, 200), 150, 5)

# eyes
pygame.draw.circle(screen, RED, (125, 150), 30, )
circle(screen, BLACK, (125, 150), 30, 2)
pygame.draw.circle(screen, BLACK, (125, 150), 10, )

circle(screen, RED, (275, 150), 30, )
circle(screen, BLACK, (275, 150), 30, 2)
circle(screen, BLACK, (275, 150), 10)

#Eyerbrows and smile

rect(screen, BLACK, (130, 270, 150, 30))

line(screen, RED, (100,100), (150, 150))









pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()