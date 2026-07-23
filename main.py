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
posy = 190

player = Class.player(posx, posy, 1, 1, images.teste, 
                      pygame.transform.scale(images.teste, (90, 100)).get_rect(),
                      100, 100)
player.rect.x = player.posX
player.rect.y = player.posY + images.height//2

currentRoom = maps.initialMap

running = True
click = False
move = False

dt = 16

clock = pygame.time.Clock()

while running:

    realMouseX, realMouseY = pygame.mouse.get_pos()
    actuallySizeScreen = real_screen.get_size()
    reasonX = size[0] / actuallySizeScreen[0]
    reasonY = size[1] / actuallySizeScreen[1]
    MouseX = int(realMouseX * reasonX)
    MouseY = int(realMouseY * reasonY)

    stringAux = player.mapLoad()
    mapa = Class.mapLOAD(stringAux)
    gameScreen.blit(currentRoom.image, (0, 0))
    Class.draw((MouseX, MouseY), gameScreen, currentRoom)
    gameScreen.blit(player.visual, (int(player.posX), int(player.posY)))
    player.barPlayer(gameScreen, images.icon, images.bar, images.red, images.blue,
                        images.redX, images.redY, images.blueX, images.blueY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                click = False
                for char in currentRoom.chars:
                    if Class.infoRectcollide((MouseX, MouseY), char):
                        click = True
                        Char = char

                if (not click):
                    move = True
                    ClickX = MouseX
                    ClickY = MouseY
                    dx = ClickX - player.posX - (images.width // 2)
                    dy = ClickY - player.posY - images.height

                    angle = math.atan2(dy, dx)

                    velX = math.cos(angle)
                    velY = math.sin(angle)

                    
                    


    tecla = pygame.key.get_pressed()

    if click:
        move = False
        Class.quest_bar(gameScreen, Char, images.questBar, images.questBarX, images.questBarY, images.questBarX + 40, images.questBarY + 70)

    elif move:
        saveX = player.rect.x
        saveY = player.rect.y - images.height//2
        player.rect.x = player.posX
        player.rect.y = player.posY + images.height//2
        distance = math.hypot(ClickX - player.posX - (images.width // 2), ClickY - player.posY - images.height)
        if distance > 5:
            player.walk(velX, velY, dt)
            player.rect.x = player.posX
            player.rect.y = player.posY + images.height//2
            if currentRoom.collide(player.rect):
                player.rect.x = saveX
                player.posX = saveX
                player.rect.y = saveY + images.height//2
                player.posY = saveY
                move = False
        elif distance <= 5:
            move = False
            player.posX = ClickX - images.width//2
            player.posY = ClickY - images.height
            player.rect.x = player.posX
            player.rect.y = player.posY + images.height//2

    

    '''
    if tecla[pygame.K_d]:
        maps.obstacle2.x += dt / 2
    elif tecla[pygame.K_s]:
        maps.obstacle2.y += dt / 2
    elif tecla[pygame.K_a]:
        maps.obstacle2.x -= dt / 2
    elif tecla[pygame.K_w]:
        maps.obstacle2.y -= dt / 2
    '''

    #pygame.draw.rect(gameScreen, (255, 0, 0), maps.obstacle2, 4)

    actuallySizeScreen = real_screen.get_size()
    screen2 = pygame.transform.scale(gameScreen, (actuallySizeScreen))

    real_screen.blit(screen2, (0, 0))

    #print(player.posY)
    
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()