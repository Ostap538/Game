import pygame
import Chel
import Sword
import Enemy
import PowerUps
import random
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.screen = pygame.display.set_mode((1960, 1080))
        self.FPS = 60
        self.running = True
        pygame.init()
        pygame.display.set_caption("")
        self.bg_color = (255, 255, 255)
        #pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.PowerUps = PowerUps.PowerUps(self.screen)
        self.chels = pygame.sprite.Group()
        self.chel = Chel.Chel(self.screen)
        self.chels.add(self.chel)
        self.swords = pygame.sprite.Group()
        self.sword = Sword.Sword(self.screen, self.chel.get_x(), self.chel.get_y() )
        self.swords.add(self.sword)
        self.enemys = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()
        self.strajs = pygame.sprite.Group()
        self.dir = 'none'
        self.frame_tick = self.FPS/8
        self.k = 0
        self.mode = 2
        self.max_enemys = 15
        self.hp = 50
        self.HpRect = pygame.Rect(0, 0, 5, 20)
        self.neyaz = 0
        self.kills = 0
        self.lvl_cup = 10
        self.kills_for_lvl_cup =0
        self.modePowerUps = 0
        self.bosscoming = 30
        self.new_boss = Enemy.Boss(self.screen)
        self.q = 1
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.dir = 'right'
                elif event.key == pygame.K_w:
                    self.dir = 'up'
                elif event.key == pygame.K_s:
                    self.dir = 'down'
                elif event.key == pygame.K_a:
                    self.dir = 'left'
                elif event.key == pygame.K_SPACE:
                    self.mode += 1



            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.sword.draw()
                self.modePowerUps = self.PowerUps.update(pygame.mouse.get_pos())
                self.FPS = 60
                #print(self.modePowerUps)
    def checkCollides(self):
        k = len(self.enemys)
        pygame.sprite.groupcollide(self.swords, self.enemys, False, True)
        self.kills_for_lvl_cup += k - len(self.enemys)
        self.kills += k - len(self.enemys)
        k = len(self.enemys)
        pygame.sprite.groupcollide(self.chels, self.enemys, False, True)
        if k> len(self.enemys):
            if self.neyaz > 60:
                self.hp -=10
                self.neyaz = 0
        if len(self.strajs) == 0:
            pygame.sprite.groupcollide(self.swords, self.bosses, False, True)
        pygame.sprite.groupcollide(self.swords, self.strajs, False, True)
        k = len(self.strajs)
        pygame.sprite.groupcollide(self.chels,self.strajs,False,True)
        if k> len(self.strajs):
            if self.neyaz > 60:
                self.hp -=20
                self.neyaz = 0
            new_straj = Enemy.Straj(self.screen)
            self.strajs.add(new_straj)
            new_straj = Enemy.Straj(self.screen)
            self.strajs.add(new_straj)
        k = len(self.bosses)
        pygame.sprite.groupcollide(self.chels, self.bosses, False, True)
        if k > len(self.bosses):
            if self.neyaz > 60:
                self.hp -= int(self.hp/2)+20
                self.neyaz = 0
            self.bosses.add(self.new_boss)


    def draw(self):
        self.screen.fill(self.bg_color)
        self.chel.draw(self.dir)

        self.sword.draw()
        for b in self.enemys:
            b.draw(self.frame_tick)
        for b in self.strajs:
            b.draw(self.frame_tick)
        for b in self.bosses:
            b.draw(self.frame_tick)
        for i in range(int(self.hp)):
            self.HpRect.y = 20
            self.HpRect.x = i * 5
            pygame.draw.rect(self.screen, (255, 0, 0), self.HpRect)
        if self.modePowerUps == 1:
            self.PowerUps.draw()
            self.FPS = 1

    def update(self):
        if self.mode %2 == 0:
            self.chel.update(self.dir, self.frame_tick,self.PowerUps.getspeedlvl())
        for b in self.enemys:
            b.update(self.chel.get_x(),self.chel.get_y())
        for b in self.strajs:
            b.update(self.chel.get_x(),self.chel.get_y())
        for b in self.bosses:
            b.update(self.chel.get_x(),self.chel.get_y())
        self.max_enemys += 0.005
        if len(self.enemys)<int(self.max_enemys):
            a = random.randint(0,1)
            new_enemy = Enemy.Enemy1(self.screen,a)
            self.enemys.add(new_enemy)
            new_enemy = Enemy.Enemy2(self.screen)
            self.enemys.add(new_enemy)
        self.sword.update(self.chel.get_x(), self.chel.get_y(),pygame.mouse.get_pos(),self.PowerUps.getswordlvl())
        if self.hp <= 0:
            print(f"Убийств:{self.kills}")
            self.running = False
        self.hp += self.PowerUps.getregen()

        if self.kills_for_lvl_cup > self.lvl_cup:
            self.kills_for_lvl_cup = self.kills_for_lvl_cup - self.lvl_cup
            self.lvl_cup = int(self.lvl_cup *1.1)
            self.modePowerUps = 1

        if self.kills > self.bosscoming:
            self.bosscoming += 100
            self.q += 2
            for i in range(4+self.q):
                new_straj = Enemy.Straj(self.screen)
                self.strajs.add(new_straj)
            self.new_boss = Enemy.Boss(self.screen)
            self.bosses.add(self.new_boss)


        self.neyaz += 1
        pygame.display.flip()
        self.clock.tick(self.FPS)
