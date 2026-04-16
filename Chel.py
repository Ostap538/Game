import pygame

class Chel(pygame.sprite.Sprite):
    def getFrames(self, xCount, yCount):
        image = pygame.image.load('img\g.jpg')
        width, height = image.get_size()
        w = width / xCount
        h = height / yCount
        frames = []
        for j in range(int(yCount / 2)):
            miniframe = []
            for i in range(xCount):
                frame = image.subsurface(pygame.Rect(i * w, 520 + j * h, w, h))
                miniframe.append(frame)
            frames.append(miniframe)
        return frames

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.frames = Chel.getFrames(self, 10, 8)
        self.image = self.frames[1][1]
        self.rect = self.image.get_rect()
        self.index = 0
        self.tick = 0
        image = pygame.image.load('img\g.jpg')
        width, height = image.get_size()
        self.afkFrame = image.subsurface(pygame.Rect(0, 0, width/10, height/8))
    def draw(self,dir):
        if dir == 'down':
            self.screen.blit(self.frames[0][self.index],self.rect)
        elif dir == 'left':
            self.screen.blit(self.frames[1][self.index],self.rect)
        elif dir == 'up':
            self.screen.blit(self.frames[2][self.index], self.rect)
        elif dir == 'right':
            self.screen.blit(self.frames[3][self.index],self.rect)
        else:
            self.screen.blit(self.afkFrame, self.rect)
    def update(self,dir,frametick,speedlvl):
        self.tick += 1
        if self.tick >=frametick:
            self.index += 1
            self.index %= 10
            self.tick = 0
        speed = (2+speedlvl)*2
        if dir =='none':
            self.rect.y = self.rect.y
        elif dir == 'up':
            self.rect.y -= speed
        elif dir == 'down':
            self.rect.y += speed
        elif dir == 'left':
            self.rect.x -= speed
        elif dir == 'right':
            self.rect.x += speed
        if self.rect.x< 0:
            self.rect.x= 0
        elif self.rect.x>1840:
            self.rect.x = 1840
        if self.rect.y < 0:
            self.rect.y =0
        elif self.rect.y > 960:
            self.rect.y = 960
    def get_x(self):
        return self.rect.x
    def get_y(self):
        return self.rect.y