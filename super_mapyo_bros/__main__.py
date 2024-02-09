from pygame import Surface, init, quit
from pygame.display import set_caption, set_mode
from pygame.event import Event, get
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from pygame.time import Clock
from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from super_mapyo_bros.camera import Camera
from super_mapyo_bros.level.level_one_one import LevelOneOne
from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.utils import render, tick

level: LevelOneOne
screen: Surface
camera: Camera
clock: Clock


def main() -> None:
    global level
    global screen
    global camera
    global clock

    init()
    set_caption(title)
    level = LevelOneOne(level_handle)
    screen = set_mode(screen_size)
    camera = Camera(level, screen_size)
    clock = Clock()
    event: Event

    while True:
        for event in get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                break

            elif event.type == QUIT:
                break

        tick(clock, level, camera)
        render(screen, level, camera)
        mario: Mario = level.get_mario()
        
        # If not mario is None and mario.is_dead:
        if mario and mario.y > screen_size[1] or mario.is_dead:
            break

    print(game_over)
    quit()
