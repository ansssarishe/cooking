import pygame as pg
import sys
from pygame import K_ESCAPE
from settings import *
from map import *
from player import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()
        self.delta_time = 1

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(60)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill("black")
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                sys.exit()


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()



