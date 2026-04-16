import pygame
import Chel
import random
class Enemy1(pygame.sprite.Sprite):
    def __init__(self, screen,shield):
        super().__init__()
        self.screen = screen
        self.frames = Chel.Chel.getFrames(self, 10, 8)
        self.image = self.frames[1][1]
        self.rect = self.image.get_rect()
        self.index = 0
        self.tick = 0
        self.dir = 0
        koordx = random.randint(500,1900)
        koordy = random.randint(100, 1000)
        self.rect.x = koordx
        self.rect.y = koordy
        self.shield = shield
        self.speed = 3
    def draw(self,frametick):
        self.tick += 1
        if self.tick >= frametick:
            self.index += 1
            self.index %= 10
            self.tick = 0
        if self.dir == 0:
            self.screen.blit(self.frames[0][self.index],self.rect)
        elif self.dir == 1:
            self.screen.blit(self.frames[1][self.index],self.rect)
        elif self.dir == 2:
            self.screen.blit(self.frames[2][self.index], self.rect)
        elif self.dir == 3:
            self.screen.blit(self.frames[3][self.index],self.rect)
        if self.shield == 1:
            pygame.draw.line(self.screen,(255,255,0),(self.rect.x,self.rect.y),(self.rect.x+118,self.rect.y),5)
            pygame.draw.line(self.screen, (255, 255, 0), (self.rect.x+118, self.rect.y), (self.rect.x + 118, self.rect.y+130),5)
            pygame.draw.line(self.screen, (255, 255, 0), (self.rect.x, self.rect.y+130),(self.rect.x + 118, self.rect.y + 130), 5)
            pygame.draw.line(self.screen, (255, 255, 0), (self.rect.x, self.rect.y),(self.rect.x, self.rect.y + 130), 5)
            self.speed = 6
        else:
            self.speed = 2

    def update(self,koordChelX,koordChelY):
        if self.rect.x > koordChelX:
            self.rect.x -= self.speed
            self.dir = 1
        else:
            self.rect.x += self.speed
            self.dir = 3
        if self.rect.y > koordChelY:
            self.rect.y -= self.speed
            self.dir = 2
        else:
            self.rect.y += self.speed
            self.dir = 0
class Enemy2(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('img\mob.jpeg')
        self.rect = self.image.get_rect()
        self.dir = 0
        koordx = random.randint(100,1900)
        koordy = random.randint(100, 1000)
        self.rect.x = koordx
        self.rect.y = koordy
    def draw(self,frametick):
        frametick += frametick
        self.screen.blit(self.image,self.rect)
    def update(self,koordChelX,koordChelY):
        if self.rect.x > koordChelX:
            self.rect.x -= 1
        else:
            self.rect.x += 1
        if self.rect.y > koordChelY:
            self.rect.y -= 1
        else:
            self.rect.y += 1
class Boss(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.frames = Chel.Chel.getFrames(self, 10, 8)
        self.image = self.frames[1][1]
        self.rect = self.image.get_rect()
        self.index = 0
        self.tick = 0
        self.dir = 0
        koordx = random.randint(500,1900)
        koordy = random.randint(100, 1000)
        self.rect.x = koordx
        self.rect.y = koordy
        self.speed = 1

    def draw(self,frametick):
        self.tick += 1
        if self.tick >= frametick:
            self.index += 1
            self.index %= 10
            self.tick = 0
        if self.dir == 0:
            self.screen.blit(self.frames[0][self.index],self.rect)
        elif self.dir == 1:
            self.screen.blit(self.frames[1][self.index],self.rect)
        elif self.dir == 2:
            self.screen.blit(self.frames[2][self.index], self.rect)
        elif self.dir == 3:
            self.screen.blit(self.frames[3][self.index],self.rect)
        pygame.draw.line(self.screen,(255,0,0),(self.rect.x,self.rect.y),(self.rect.x+118,self.rect.y),5)
        pygame.draw.line(self.screen, (255, 0, 0), (self.rect.x+118, self.rect.y), (self.rect.x + 118, self.rect.y+130),5)
        pygame.draw.line(self.screen, (255, 0, 0), (self.rect.x, self.rect.y+130),(self.rect.x + 118, self.rect.y + 130), 5)
        pygame.draw.line(self.screen, (255, 0, 0), (self.rect.x, self.rect.y),(self.rect.x, self.rect.y + 130), 5)
    def update(self,koordChelX,koordChelY):
        if self.rect.x > koordChelX:
            self.rect.x -= self.speed
            self.dir = 1
        else:
            self.rect.x += self.speed
            self.dir = 3
        if self.rect.y > koordChelY:
            self.rect.y -= self.speed
            self.dir = 2
        else:
            self.rect.y += self.speed
            self.dir = 0
    def get_x(self):
        return self.rect.x
    def get_y(self):
        return self.rect.y
class Straj(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('img\mob.jpeg')
        self.rect = self.image.get_rect()
        self.dir = 0
        koordx = random.randint(100, 1900)
        koordy = random.randint(100, 1000)
        self.rect.x = koordx
        self.rect.y = koordy

    def draw(self, frametick):
        frametick += frametick
        self.screen.blit(self.image, self.rect)
        pygame.draw.line(self.screen, (255, 0, 0), (self.rect.x, self.rect.y), (self.rect.x + 32, self.rect.y), 5)
        pygame.draw.line(self.screen, (255, 0, 0), (self.rect.x + 32, self.rect.y),
                         (self.rect.x + 32, self.rect.y + 32), 5)
        pygame.draw.line(self.screen, (255, 0, 0), (self.rect.x, self.rect.y + 32),
                         (self.rect.x + 32, self.rect.y + 32), 5)
        pygame.draw.line(self.screen, (255, 0, 0), (self.rect.x, self.rect.y), (self.rect.x, self.rect.y + 32), 5)
    def update(self, koordChelX, koordChelY):
        if self.rect.x > koordChelX:
            self.rect.x -= 1
        else:
            self.rect.x += 1
        if self.rect.y > koordChelY:
            self.rect.y -= 1
        else:
            self.rect.y += 1
