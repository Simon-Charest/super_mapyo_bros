from pygame import Rect
from pygame.display import flip
from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from super_mapyo_bros.struct import Struct


def collision_sides(a, b) -> Struct:
    sides = Struct(left=False, right=False, top=False, bottom=False)
    left = Rect(a.left, a.top + 1, 1, a.height - 2)
    right = Rect(a.right, a.top + 1, 1, a.height - 2)
    top = Rect(a.left + 1, a.top, a.w - 2, 1)
    bottom = Rect(a.left + 1, a.bottom, a.width - 2, 1)

    if left.colliderect(b):
        sides.left = True

    if right.colliderect(b):
        sides.right = True

    if top.colliderect(b):
        sides.top = True

    if bottom.colliderect(b):
        sides.bottom = True

    return sides


def should_fall(entity, level) -> bool:
    for tile in level.map:
        sides = collision_sides(entity.rect, tile.rect)

        if sides.bottom:
            return False
        
    return True


def updateFall(entity, deltaTime) -> bool:
    landed = False
    
    # Check for landing
    if entity.hasCollision:
        for tile in entity.collidingObjects:
            sides = collision_sides(entity.rect, tile.rect)
            if sides.bottom:
                # If entity fell on Mario then it's an enemy
                # and this should trigger death or power-down in Mario.
                if isinstance(tile, Mario):
                    return
                
                entity.setY(tile.top() - entity.h)
                entity.changeState("idle")
                entity.hasCollision = False
                entity.collidingObjects = []

                return True 
    
    if entity.dy > maxVelocity:
        entity.dy = maxVelocity

    else:
        entity.dy += entity.velocity
        
    entity.velocity += gravity
    entity.translate(0, entity.dy * deltaTime)

    return landed


def render(screen, level, camera) -> None:
    screen.fill(screenBGColor)
    level.draw(screen, camera)
    flip()


def tick(clock, level, camera) -> None:
    deltaTime = clock.tick(60)
    level.update(deltaTime)
    camera.update()
