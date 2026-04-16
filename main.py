import pygame
import Game

def run():
    game = Game.Game()
    while game.running:
        game.getEvents()

        game.draw()
        game.update()
        game.checkCollides()

run()
pygame.quit()
