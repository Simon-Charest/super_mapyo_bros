from pygame import Rect, Surface
from pygame.display import flip
from pygame.time import Clock
from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from super_mapyo_bros.entity import Entity
from super_mapyo_bros.camera import Camera
from super_mapyo_bros.struct import Struct
from typing import Type


def collision_sides(a: Rect, b: Rect) -> Struct:
    sides: Struct = Struct(left = False, right = False, top = False, bottom = False)
    left: Rect = Rect(a.left, a.top + 1, 1, a.height - 2)
    right: Rect = Rect(a.right, a.top + 1, 1, a.height - 2)
    top: Rect = Rect(a.left + 1, a.top, a.w - 2, 1)
    bottom: Rect = Rect(a.left + 1, a.bottom, a.width - 2, 1)

    if left.colliderect(b):
        sides.left = True

    if right.colliderect(b):
        sides.right = True

    if top.colliderect(b):
        sides.top = True

    if bottom.colliderect(b):
        sides.bottom = True

    return sides


def render(screen: Surface, level: Type["LevelOneOne"], camera: Camera) -> None:
    screen.fill(screen_bg_color)
    level.draw(screen, camera)
    flip()


def should_fall(entity: Entity, level: Type["LevelOneOne"]) -> bool:
    for tile in level.map:
        sides = collision_sides(entity.rect, tile.rect)

        if sides.bottom:
            return False
        
    return True


def tick(clock: Clock, level: Type["LevelOneOne"], camera: Camera) -> None:
    delta_time: int = clock.tick(60)
    level.update(delta_time)    
    camera.update()


def update_fall(entity: Entity, delta_time: int) -> bool:
    from super_mapyo_bros.block.brick_block import BrickBlock
    from super_mapyo_bros.mario.mario import Mario
    
    landed: bool = False
    
    # Check for landing
    if entity.has_collision:
        sides: Struct
        tile: BrickBlock

        for tile in entity.colliding_objects:
            sides = collision_sides(entity.rect, tile.rect)

            if sides.bottom:
                # If entity fell on Mario then it's an enemy
                # and this should trigger death or power-down in Mario.
                if isinstance(tile, Mario):
                    return
                
                entity.set_y(tile.top() - entity.h)
                entity.change_state("idle")
                entity.has_collision = False
                entity.colliding_objects = []

                return True 
    
    if entity.dy > max_velocity:
        entity.dy = max_velocity

    else:
        entity.dy += entity.velocity
        
    entity.velocity += gravity
    entity.translate(0, entity.dy * delta_time)

    return landed
