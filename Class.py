import pygame
import images

class player:

    def __init__(self, posX, posY, map, room, visual):
        self.posX = posX
        self.posY = posY
        self.map = map
        self.room = room
        self.speed = 200
        self.visual = visual

    def walk(self, velX, velY, dt):
        self.posX += velX * dt / 1000.0 * self.speed
        self.posY += velY * dt / 1000.0 * self.speed

    def mapLoad(self):
        if self.map == 1:
            if self.room == 1:
                return "1_1"

class map:
    def __init__(self, nome, room, id, image, rects):
        self.nome = nome
        self.room = room
        self.id = id
        self.image = image
        self.rects = rects




def mapLOAD(string):
    map = ""
    room = ""
    stop = False
    for i in string:
        if(not stop):
            if i != "_":
                map += i
            else:
                stop = True
        else:
            room += i
    if map == "1":
        if room == "1":
            return images.lobbyTeste