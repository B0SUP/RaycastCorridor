import pygame
from settings import *
from player import Player
import math
from map import world_map
from raycasting import raycasting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    pygame.draw.rect(sc, RED, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, BLACK, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    raycasting(sc, player.pos, player.angle)

    pygame.display.flip()
    clock.tick(FPS)
    print(clock.get_fps())

    #в