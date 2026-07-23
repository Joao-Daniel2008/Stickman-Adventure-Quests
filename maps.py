import pygame
import images
import Class

pygame.init()
obstacle = images.Obstacle.get_rect()
obstaclesInital = tuple(obstacle)
initialMap = Class.map("initial", 1, 1, images.lobbyTeste, obstaclesInital)