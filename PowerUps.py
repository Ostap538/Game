import pygame
import random
class PowerUps:
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.rect1 = pygame.Rect(200,150,400,600)
        self.rect11 = pygame.Rect(300,200,200,200)
        self.rect2 = pygame.Rect(790, 150, 400, 600)
        self.rect22 = pygame.Rect(890, 200, 200, 200)
        self.rect3 = pygame.Rect(1380, 150, 400, 600)
        self.rect33 = pygame.Rect(1480, 200, 200, 200)
        self.vibor = 0
        self.speedlvl = 1
        self.swordlvl = 1
        self.regen = 0.01
    def draw(self):
        pygame.draw.rect(self.screen,(0,0,0),self.rect1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect11)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect2)
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect22)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect3)
        pygame.draw.rect(self.screen, (0, 0, 255), self.rect33)
    def update(self,koords):
        self.vibor = 1
        if koords[0] >= self.rect1.x and koords[0] <= self.rect1.x+400 and koords[1] >= self.rect1.y and koords[1] <= self.rect1.y+600:
            self.vibor = 2
            self.regen += 0.01
        elif koords[0] >= self.rect2.x and koords[0] <= self.rect2.x+400 and koords[1] >= self.rect2.y and koords[1] <= self.rect2.y+600:
            self.vibor = 3
            self.speedlvl += 1
        elif koords[0] >= self.rect3.x and koords[0] <= self.rect3.x+400 and koords[1] >= self.rect3.y and koords[1] <= self.rect3.y+600:
            self.vibor = 4
            self.swordlvl += 1
        return self.vibor
    def getspeedlvl(self):
        return(self.speedlvl)
    def getswordlvl(self):
        return(self.swordlvl)
    def getregen(self):
        return(self.regen)