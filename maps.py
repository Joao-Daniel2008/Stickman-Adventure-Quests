import pygame
import images
import Class
import chars

def scaler(image, scalee):
    return pygame.transform.scale(image, scalee)

pygame.init()
obstacle1 = scaler(images.Obstacle, (534, 20)).get_rect()
obstacle1.x = 490
obstacle1.y = 392
obstacle2 = scaler(images.Obstacle, (1024, 230)).get_rect()
obstacle2.x = 0
obstacle2.y = 0
obstaclesInital = (obstacle1, obstacle2)
chars1 = (chars.charTeste, chars.charTeste)
initialMap = Class.room("initial", 1, 1, images.lobbyTeste, obstaclesInital, chars1)