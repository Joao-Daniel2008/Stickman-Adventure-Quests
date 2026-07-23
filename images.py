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

wayLobbyTeste = os.path.join(assetsPaste, "images", "maps", "initial", "lobbyTeste.png")
lobbyTeste = pygame.image.load(wayLobbyTeste)
lobbyTeste = pygame.transform.scale(lobbyTeste, size)

wayObstacle = os.path.join(assetsPaste, "images", "maps", "initial", "obstacle.png")
Obstacle = pygame.image.load(wayObstacle)




