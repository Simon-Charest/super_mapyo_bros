from pygame import init, quit
from pygame.display import set_caption, set_mode
from pygame.event import get
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from pygame.time import Clock
from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from super_mapyo_bros.camera import Camera
from super_mapyo_bros.level.level_one_one import LevelOneOne
from super_mapyo_bros.utils import render, tick


def main() -> None:
    global level
    global screen
    global camera
    global clock

    init()
    level = LevelOneOne(levelHandle)
    screen = set_mode(screenSize)
    set_caption(title)
    camera = Camera(level, screenSize)
    clock = Clock()

    while True:
        for event in get():
            if event.type == QUIT:
                break

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                break

        tick(clock, level, camera)
        render(screen, level, camera)

        mario = level.getMario()
        
        # if not mario is None and mario.isDead:
        if not mario is None and (mario.y > screenSize[1] or mario.isDead):
            print("Game Over")
            break

    quit()
