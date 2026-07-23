import pygame
import images

class player:

    def __init__(self, posX, posY, map, room, visual, rect, hp, mana):
        self.posX = posX
        self.posY = posY
        self.map = map
        self.room = room
        self.speed = 200
        self.visual = visual
        self.rect = rect
        self.maxHp = hp
        self.hp = hp
        self.maxMana = mana
        self.mana = mana

    def walk(self, velX, velY, dt):
        self.posX += velX * dt / 1000.0 * self.speed
        self.posY += velY * dt / 1000.0 * self.speed

    def mapLoad(self):
        if self.map == 1:
            if self.room == 1:
                return "1_1"

    def barPlayer(self, window, icon, bar, red, blue, posXRed, posYRed, posXBlue, posYBlue):
        window.blit(icon, (0, 0))
        window.blit(red, (posXRed, posYRed))
        window.blit(blue, (posXBlue, posYBlue))
        window.blit(bar, (0, 0))


class characters:
    def __init__(self, name, info, quests, image, position, infoimage, infoimage2, infoPosition):
        self.name = name
        self.info = info
        self.quests = quests
        self.image = image
        self.position = position
        self.infoImage = infoimage
        self.infoImage2 = infoimage2
        self.infoPosition = infoPosition
        self.infoRect = self.infoImage.get_rect()
        self.infoRect.x = infoPosition[0]
        self.infoRect.y = infoPosition[1]
        


    



class room:
    def __init__(self, name, room, id, image, rects, characters):
        self.nome = name
        self.room = room
        self.id = id
        self.image = image
        self.rects = rects
        self.chars = characters

    def collide(self, rectPlayer):
        for rect in self.rects:
            if rectPlayer.colliderect(rect):
                return True
        return False

    

def draw(mouse, window, room):
    for char in room.chars:
        window.blit(char.image, char.position)
        if(not char.infoRect.collidepoint(mouse)):
            window.blit(char.infoImage, char.infoPosition)
        else:
            window.blit(char.infoImage2, char.infoPosition)





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