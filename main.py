import pygame
import images
import os
from pygame._sdl2.video import Window
import Class
import math
import maps


pygame.init()
size = (1024, 576)
real_screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("SAQ")

gameScreen = pygame.Surface(size)

window = Window.from_display_module()
window.maximize()

posx = 0
posy = 0

player = Class.player(posx, posy, 1, 1, images.teste)

currentMap = maps.initialMap

running = True
click = False

dt = 16

clock = pygame.time.Clock()

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
                realClickX, realClickY = event.pos

                actuallySizeScreen = real_screen.get_size()
                reasonX = size[0] / actuallySizeScreen[0]
                reasonY = size[1] / actuallySizeScreen[1]
                ClickX = int(realClickX * reasonX)
                ClickY = int(realClickY * reasonY)
                dx = ClickX - player.posX - (images.width // 2)
                dy = ClickY - player.posY - images.height

                angle = math.atan2(dy, dx)

                velX = math.cos(angle)
                velY = math.sin(angle)

    if click:
        distance = math.hypot(ClickX - player.posX - (images.width // 2), ClickY - player.posY - images.height)
        if distance > 5:
            player.walk(velX, velY, dt)
        else:
            click = False
            player.posX = ClickX - images.width//2
            player.posY = ClickY - images.height
    stringAux = player.mapLoad()
    mapa = Class.mapLOAD(stringAux)
    gameScreen.blit(currentMap.image, (0, 0))
    gameScreen.blit(player.visual, (int(player.posX), int(player.posY)))

    actuallySizeScreen = real_screen.get_size()
    screen2 = pygame.transform.scale(gameScreen, (actuallySizeScreen))

    real_screen.blit(screen2, (0, 0))
    
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()