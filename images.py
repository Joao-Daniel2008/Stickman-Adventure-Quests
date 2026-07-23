import pygame
import os # Important: Python's library to deal with ways archirves
from pygame._sdl2.video import Window

pygame.init()

size = (1024, 576)

# --- CONFIGURAÇÃO DE CAMINHOS ---
# Descobre o caminho exato onde este arquivo .py está rodando
baseDirectory = os.path.dirname(__file__)

# Cria o caminho até a pasta 'assets' (funciona no Windows, Mac e Linux)
assetsPaste = os.path.join(baseDirectory, "assets")

waySTeste = os.path.join(assetsPaste, "images", "stickman", "sTeste.png")
teste = pygame.image.load(waySTeste)
height = 200
width = 90
teste = pygame.transform.scale(teste, (width, height))
rteste = teste.get_rect()
rteste.x = 0
rteste.y = 0
cut = pygame.Rect(0, 0, 90, 65)
icon = teste.subsurface(cut)

wayLobbyTeste = os.path.join(assetsPaste, "images", "maps", "initial", "lobbyTeste.png")
lobbyTeste = pygame.image.load(wayLobbyTeste)
lobbyTeste = pygame.transform.scale(lobbyTeste, size)

wayObstacle = os.path.join(assetsPaste, "images", "maps", "initial", "obstacle.png")
Obstacle = pygame.image.load(wayObstacle)

wayBar = os.path.join(assetsPaste, "images", "stickman", "bar.png")
bar = pygame.image.load(wayBar)
bar = pygame.transform.scale(bar, (300, 75))

#colors
wayRed = os.path.join(assetsPaste, "images", "stickman", "red.png")
red = pygame.image.load(wayRed)
red = pygame.transform.scale(red, (200, 20))
redX = 84
redY = 12
wayBlue = os.path.join(assetsPaste, "images", "stickman", "blue.png")
blue = pygame.image.load(wayBlue)
blue = pygame.transform.scale(blue, (200, 20))
blueX = 84
blueY = 39

wayInfo = os.path.join(assetsPaste, "images", "stickman", "info.png")
info = pygame.image.load(wayInfo)
info = pygame.transform.scale(info, (50, 50))

wayInfo2 = os.path.join(assetsPaste, "images", "stickman", "info2.png")
info2 = pygame.image.load(wayInfo2)
info2 = pygame.transform.scale(info2, (50, 50))




