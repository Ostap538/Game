import pygame

class Sword(pygame.sprite.Sprite):
    def __init__(self,screen: pygame.Surface,koordx,koordy):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,16,200)
        self.rect.x = koordx+64
        self.rect.y = koordy-96
        self.xx = 0
        self.yy = 0

    def draw(self):
        pygame.draw.rect(self.screen,(0,0,0),self.rect)
    def update(self,koordx,koordy,mousekoords,swordlvl):
        if mousekoords[0] > koordx and mousekoords[0]<koordx+96:
            if mousekoords[1]<koordy:
                self.rect = pygame.Rect(0, 0, 16, 150+swordlvl*50)
                self.xx = 48
                self.yy = -200-(swordlvl-1)*50
            else:
                self.rect = pygame.Rect(0, 0, 16, 150+swordlvl*50)
                self.xx = 48
                self.yy = 128
        else:
            if mousekoords[1] >koordy and mousekoords[1] < koordy+96:
                if mousekoords[0]>koordx:
                    self.rect = pygame.Rect(0, 0, 150+swordlvl*50, 16)
                    self.xx = 118
                    self.yy = 64
                else:
                    self.rect = pygame.Rect(0, 0, 150+swordlvl*50, 16)
                    self.xx = -200-(swordlvl-1)*50
                    self.yy = 64
        self.rect.x = koordx + self.xx
        self.rect.y = koordy + self.yy
