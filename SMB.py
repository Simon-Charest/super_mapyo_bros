import pygame
import sys
from pygame.locals import *

####################################
# Constants
####################################

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
lightBlue = [135,206,250]
white = [255,255,255]
black = [0,0,0]
gold = [255,215,0]
groundBrown = [160,82,45]
brickBrown = [205,133,63]

koopaColor = [50, 205, 50]
goombaColor = [220, 110, 75]
marioColor = white

####################################
# Classes
####################################

# Camera
class Camera:
    def __init__ (self):
        self.getValues()
        self.x = 0
        self.y = 0
        self.w = screenSize[0]
        self.h = screenSize[1]

    def update (self):
        self.getValues()

    def getValues (self):
        mario = level.getMario()
        if mario is None:
            return
        if mario.x < screenSize[0]/2:
            self.x = 0
        else:
            self.x = level.getMario().x - screenSize[0]/2 + tileWidth/2

# Struct
class Struct (object):
    def __init__ (self, **entries):
        self.__dict__.update(entries)

# Entity
class Entity (object):
    x = 0
    y = 0
    w = 0
    h = 0
    rect = Rect(x,y,w,h)
    color = [0,0,0]
    direction = "right"
    currState = None
    prevState = None
        
    def __init__ (self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = Rect(x,y,w,h)
        self.allStates = {}
        self.collidingObjects = []
        self.hasCollision = False

    def left (self):
        return self.x
    def right (self):
        return self.x + self.w
    def bottom (self):
        return self.y + self.h
    def top (self):
        return self.y
    def setY (self, y):
        self.y = y
        self.rect = Rect(self.x, self.y, self.w, self.h)
    def setX (self, x):
        self.x = x
        self.rect = Rect(self.x, self.y, self.w, self.h)

    def translate (self, dx, dy):
        if dx < 0:
            self.direction = "left"
        elif dx > 0:
            self.direction = "right"

        self.x += dx

        if isinstance(self, Mario) and self.x < 0:
            self.x = 0
        
        self.y += dy
        self.rect = Rect(self.x,self.y,self.w,self.h)

    def changeState (self, stateID):
        if self.allStates.get(stateID) is None:
            return
        else:
            self.newState = self.allStates.get(stateID)
            self.currState.exitState(self)
            self.prevState = self.currState
            self.currState = self.newState
            self.currState.enterState(self)

    def addCollision (self, collided):
        self.collidingObjects.append(collided)
        self.hasCollision = True

    def draw (self):
        pygame.draw.rect(screen, self.color, [self.x - camera.x, self.y - camera.y, self.w, self.h], 0)

# Enemy
class Enemy (Entity):
    def __init__ (self, x, y, w, h, color):
        Entity.__init__(self, x, y, w, h, color)

# Coin
class Coin (Entity):
    def __init__ (self, x, y, w, h, color):
        Entity.__init__(self, x, y, w, h, color)
        self.allStates = { "idle":CoinStateIdle() }

    def update (self, deltaTime):
        self.currState.execute(self, deltaTime)    

# BrickBlock
class BrickBlock (Entity):
    def __init__ (self, x, y, w, h, color):
        Entity.__init__(self, x, y, w, h, color)
        self.allStates = { "idle":BrickBlockStateIdle() } #, "hit_light":BrickBlockStateHitLight(), "hit_hard":BrickBlockStateHitHard() }   
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState
        
    def update (self, deltaTime):
        self.currState.execute(self, deltaTime)

# QuestionBlock
class QuestionBlock (Entity):
    def __init__ (self, x, y, w, h, color):
        Entity.__init__(self, x, y, w, h, color)
        self.allStates = { "idle":QuestionBlockStateIdle() } #, "hit":QuestionBlockStateHit() }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState

    def update (self, deltaTime):
        self.currState.execute(self, deltaTime)

# GroundBlock 
class GroundBlock (Entity):
    def __init__ (self, x, y, w, h, color):
        Entity.__init__(self, x, y, w, h, color)
        self.allStates = { "idle":GroundBlockStateIdle() }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState

    def update (self, deltaTime):
        self.currState.execute(self, deltaTime)

# Mushroom
class Mushroom (Entity):
    def __init__ (self, x, y, w, h, color):
        Entity.__init__(self, x, y, w, h, color)
        self.allStates = { "spawn":MushroomStateSpawn(), "move":MushroomStateMove() }

    def update (self, deltaTime):
        self.currState.execute(self, deltaTime)

# Goomba
class Goomba (Enemy):
    def __init__ (self, x, y, w, h, spawnX, color):
        Enemy.__init__(self, x, y, w, h, color)
        self.allStates = { "wait":EnemyStateWait(), "move":EnemyStateMove(), "fall":EnemyStateFall(), "stomped":GoombaStateStomped() }
        self.prevState = self.allStates.get("wait")
        self.currState = self.prevState
        self.spawnX = spawnX
        self.direction = "left"
        self.isSpawned = False
        self.isDead = False
        self.isDeadDead = False #lulz
        self.velocity = 0
        self.dy = 0

    def update (self, deltaTime):
        if not self.isDeadDead:
            self.currState.execute(self, deltaTime)

    def draw (self):
        if self.isSpawned and not self.isDeadDead:
            Entity.draw(self)

# Koopa
class Koopa (Enemy):
    def __init__ (self, x, y, w, h, spawnX, color):
        Enemy.__init__(self, x, y, w, h, color)
        self.allStates = { "wait":EnemyStateWait(), "move":EnemyStateMove(), "fall":EnemyStateFall(), "stomped":KoopaStateStomped(), "shellMove":KoopaStateShellMove() }
        self.prevState = self.allStates.get("wait")
        self.currState = self.prevState
        self.spawnX = spawnX
        self.direction = "left"
        self.isSpawned = False
        self.isDead = False
        self.isDeadDead = False 
        self.velocity = 0
        self.dy = 0

    def update (self, deltaTime):
        if not self.isDeadDead:
            self.currState.execute(self, deltaTime)

    def draw (self):
        if self.isSpawned and not self.isDeadDead:
            Entity.draw(self)

# Pipe
class Pipe (Entity):
    def __init__ (self, x, y, w, h, color):
        Entity.__init__(self, x, y, w, h, color)
        self.allStates = { "idle":PipeStateIdle() }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState

    def update (self, deltaTime):
        self.currState.execute(self, deltaTime)

# Mario
class Mario (Entity):
    def __init__ (self, x, y, w, h, color):
        Entity.__init__(self, x, y, w, h, color)
        self.allStates = { "idle":MarioStateIdle(), "move":MarioStateMove(), "jump":MarioStateJump(), "fall":MarioStateFall() }
        self.prevState = self.allStates.get("idle")
        self.currState = self.prevState
        self.speed = 0.5
        self.isDead = False
        self.dy = 0
        self.velocity = 0
        
    def update (self, deltaTime):
        self.currState.execute(self, deltaTime)


# State
class State (object):

    def enterState (self, entity):
        raise NotImplementedError("Please Implement enter() in State subclass.")

    def execute (self, entity, deltaTime):
        raise NotImplementedError("Please Implement execute() in State subclass.")

    def exitState (self, entity):
        raise NotImplementedError("Please Implement exit() in State subclass.")

# MarioStateIdle
class MarioStateIdle (State):
    def enterState (self, entity):
        return

    def execute (self, entity, deltaTime):
        key = pygame.key.get_pressed()
        if key[K_SPACE]:
            entity.changeState("jump")
        elif key[K_a]:
            entity.direction = "left"
            entity.changeState("move")
        elif key[K_d]:
            entity.direction = "right"
            entity.changeState("move")

        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if isinstance(tile, Enemy) and not tile.isDead and (sides.left or sides.right or sides.top):
                    entity.isDead = True
            entity.hasCollision = False
            entity.collidingObjects = []

    def exitState (self, entity):
        entity.hasCollision = False
        entity.collidingObjects = []

# MarioStateMove
class MarioStateMove (State):
    def enterState (self, entity):
        self.run = False
    
    def execute (self, entity, deltaTime):
        key = pygame.key.get_pressed()

        # Check for move off of any platform
        shouldFall = should_fall(entity)
        
        if shouldFall:
            entity.changeState("fall")

        if key[K_SPACE]:
            entity.changeState("jump")
        
        if key[K_LSHIFT]:
            self.run = True
            
        if key[K_a]:
            if self.run:
                entity.translate(-(entity.speed) * 2 * deltaTime, 0)
            else:
                entity.translate(-(entity.speed) * deltaTime, 0)
            entity.direction = "left"
            
        if key[K_d]:
            if self.run:
                entity.translate(entity.speed * 2 * deltaTime, 0)
            else:
                entity.translate(entity.speed * deltaTime, 0)
            entity.direction = "right"

        if not key[K_LSHIFT]:
            self.run = False

        if not key[K_a] and not key[K_d]:
            entity.changeState("idle")

        # Check for move into something.
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if isinstance(tile, Enemy) and (sides.left or sides.right or sides.top):
                    # If an enemy and still alive then hurt mario.
                    if not tile.isDead:
                        entity.isDead = True
                if sides.left:
                    entity.setX(tile.x + tile.w)
                elif sides.right:
                    entity.setX(tile.x - entity.w)
            entity.hasCollision = False
            entity.collidingObjects = []
 
    def exitState (self, entity):
        entity.hasCollision = False
        entity.collidingObjects = []

# MarioStateJump
class MarioStateJump (State):
    def enterState (self, entity):
        entity.dy = 0
        entity.velocity = -0.2
        self.startHeight = entity.y
        self.dx = 0

    def execute (self, entity, deltaTime):
        # Check in-air movement.
        key = pygame.key.get_pressed()
        speed = entity.speed
        jumpGravity = gravity

        if key[K_LSHIFT]:
            speed *= 2
            jumpGravity *= 0.9
        if key[K_a]:
            entity.direction = "left"
            self.dx = -speed
        if key[K_d]:
            entity.direction = "right"
            self.dx = speed

        # Check collisions.
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if sides.top:
                    entity.setY(tile.bottom() + (entity.y - tile.y))
                    entity.velocity = 0
                    entity.dy = 0
                if sides.bottom:
                    if isinstance(tile, Enemy) and not tile.isDead:
                        entity.dy = 0
                        entity.velocity = -0.15
                    else:
                        entity.setY(tile.top() - entity.h)
                        entity.changeState("idle")
                        return

        # Don't go so fast that collisions are missed
        if entity.dy > maxVelocity:
            entity.dy = maxVelocity
        else:
            entity.dy += entity.velocity
        
        entity.velocity += jumpGravity
        entity.translate(self.dx * deltaTime, entity.dy * deltaTime)

    def exitState (self, entity):
        entity.hasCollision = False
        entity.collidingObjects = []
    

# MarioStateFall
class MarioStateFall (State):
    def enterState (self, entity):
        self.dx = 0
        entity.velocity = 0
    
    def execute (self, entity, deltaTime):
        # Check in-air movement.
        key = pygame.key.get_pressed()
        speed = entity.speed

        if key[K_LSHIFT]:
            speed *= 2
        if key[K_a]:
            entity.direction = "left"
            self.dx = -speed
        if key[K_d]:
            entity.direction = "right"
            self.dx = speed

        # Check for landing
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if sides.bottom:
                    if isinstance(tile, Enemy) and not tile.isDead:
                        entity.dy = 0
                        entity.velocity = -0.15
                    else:
                        entity.setY(tile.top() - entity.h)
                        entity.changeState("idle")
                        return
        
        if entity.dy > maxVelocity:
            entity.dy = maxVelocity
        else:
            entity.dy += entity.velocity
            
        entity.velocity += gravity
        entity.translate(self.dx * deltaTime, entity.dy * deltaTime)

    def exitState (self, entity):
        entity.hasCollision = False
        entity.collidingObjects = []

# EnemyStateWait
class EnemyStateWait (State):
    def enterState (self, entity):
        return

    def execute (self, entity, deltaTime):
        # Wait until player reaches some X position on the
        # level before updating and drawing this goomba instance.
        if level.getMario().x > entity.spawnX:
            entity.changeState("move")

    def exitState(self, entity):
        entity.isSpawned = True

# EnemyStateMove
class EnemyStateMove (State):
    def enterState (self, entity):
        return

    def execute (self, entity, deltaTime):
        if entity.direction == "left":
            entity.translate(-(0.1 * deltaTime), 0)
        else:
            entity.translate(0.1 * deltaTime, 0)

        # Check if should fall.
        shouldFall = should_fall(entity)
        if shouldFall:
            entity.changeState("fall")

        # Check for move into something.
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                
                # That something was Mario.
                if sides.top and isinstance(tile, Mario):
                    entity.changeState("stomped")
                    
                if sides.left:
                    entity.setX(tile.x + tile.w)
                    entity.direction = "right"
                elif sides.right:
                    entity.setX(tile.x - entity.w)
                    entity.direction = "left"
                
            entity.hasCollision = False
            entity.collidingObjects = []

    def exitState(self, entity):
        return

# EnemyStateFall
class EnemyStateFall (State):
    def enterState (self, entity):
        entity.velocity = 0

    def execute (self, entity, deltaTime):
        # Update X
        if entity.direction == "left":
            entity.translate(-(0.1 * deltaTime), 0)
        else:
            entity.translate(0.1 * deltaTime, 0)

        # Update Y
        landed = updateFall(entity, deltaTime)

        # Check land
        if landed:
            entity.changeState("move")

    def exitState(self, entity):
        return

# GoombaStateStomped
class GoombaStateStomped (State):
    def enterState (self, entity):
        self.time = 0
        self.squishTime = 1000 # one second
        entity.y += entity.h/2
        entity.h /= 2
        entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)
        entity.isDead = True

    def execute (self, entity, deltaTime):
        self.time += deltaTime

        # When time is up, switch to any state to remove goomba for good.
        if self.time > self.squishTime:
            entity.changeState("move")

    def exitState(self, entity):
        entity.isDeadDead = True
        level.removeEntity(entity)

# KoopaStateStomped
class KoopaStateStomped (State):
    def enterState (self, entity):
        self.time = 0
        self.recoverTime = 5000 # five seconds
        entity.y += entity.h/2
        entity.h /= 2
        entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)
        entity.isDead = True

    def execute (self, entity, deltaTime):
        self.time += deltaTime

        # Come back out of shell.
        if self.time > self.recoverTime:
            entity.isDead = False
            entity.changeState("move")
            entity.y -= entity.h*2
            entity.h *= 2
            entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)
            return

        # Otherwise check for mario hitting it in some direction.
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                if isinstance(tile, Mario):
                    # Decide which way to shoot shell.
                    if tile.x <= entity.x:
                        entity.direction = "right"
                    else:
                        entity.direction = "left"
                    # Shoot shell.
                    entity.changeState("shellMove")

            entity.hasCollision = False
            entity.collidingObjects = []

    def exitState (self, entity):
        return

# KoopaStateShellMove
class KoopaStateShellMove (State):
    def enterState (self, entity):
        return

    def execute (self, entity, deltaTime):
        if entity.direction == "left":
            entity.translate(-(0.6 * deltaTime), 0)
        else:
            entity.translate(0.6 * deltaTime, 0)

        # Check if should fall.
        shouldFall = should_fall(entity)
        if shouldFall:
            entity.changeState("fall")

        # Check for move into something.
        if entity.hasCollision:
            for tile in entity.collidingObjects:
                sides = collision_sides(entity.rect, tile.rect)
                
                # That something was Mario.
                if sides.top and isinstance(tile, Mario):
                    entity.y -= entity.h*2
                    entity.h *= 2
                    entity.rect = Rect(entity.x, entity.y, entity.w, entity.h)
                    entity.changeState("stomped")
                    
                if sides.left:
                    entity.setX(tile.x + tile.w)
                    entity.direction = "right"
                elif sides.right:
                    entity.setX(tile.x - entity.w)
                    entity.direction = "left"
                
            entity.hasCollision = False
            entity.collidingObjects = []

    def exitState(self, entity):
        return

# QuestionBlockStateIdle
class QuestionBlockStateIdle (State):
    def enterState (self, entity):
        return

    def execute (self, entity, deltaTime):
        return

    def exitState(self, entity):
        return

# BrickBlockStateIdle
class BrickBlockStateIdle (State):
    def enterState (self, entity):
        return

    def execute (self, entity, deltaTime):
        return

    def exitState(self, entity):
        return

# GroundBlockStateIdle
class GroundBlockStateIdle (State):
    def enterState (self, entity):
        return

    def execute (self, entity, deltaTime):
        return
        
    def exitState(self, entity):
        return

# PipeStateIdle
class PipeStateIdle (State):
    def enterState (self, entity):
        return

    def execute (self, entity, deltaTime):
        if entity.hasCollision:
            entity.hasCollision = False
            entity.collidingObjects = []
        
    def exitState(self, entity):
        return

# CoinStateIdle
class CoinStateIdle (State):
    def enterState (self, entity):
       return

    def execute (self, entity, deltaTime):
        return

    def exitState(self, entity):
        return

####################################
# Levels
####################################

# Level
class Level:
    
    def __init__ (self, fileHandle):
        self.f = open(fileHandle)
        self.tileRows = self.f.readlines()
        self.map = []
        self.entities = []
        i = 0
        for row in self.tileRows:
            j = 0
            for tile in row:
                self.loadItem(tile, j, i)
                j += 1
            i += 1

    def loadItem (self, tile, x, y):
        xPos = x * tileWidth
        yPos = y * tileWidth

        if (tile == blankTile):
            return
        
        elif (tile == groundTile):
            self.map.append(GroundBlock(xPos, yPos, tileWidth, tileWidth, groundBrown))

        elif (tile == marioTile):
            self.entities.append(Mario(xPos, yPos, tileWidth, tileWidth, white))

        elif (tile == blockTile):
            self.map.append(BrickBlock(xPos, yPos, tileWidth, tileWidth, brickBrown))

        elif (tile == questionTile):
            self.map.append(QuestionBlock(xPos, yPos, tileWidth, tileWidth, gold))

        elif (tile == pipeTile):
            self.map.append(Pipe(xPos, yPos, tileWidth, tileWidth, green))

        elif (tile == goombaTile):
            self.entities.append(Goomba(xPos, yPos, tileWidth, tileWidth, xPos - screenSize[0]/2, goombaColor))

        elif (tile == koopaTile):
            self.entities.append(Koopa(xPos, yPos, tileWidth, tileWidth, xPos - screenSize[0]/2, koopaColor))

    def update (self, deltaTime):
        for tile in self.map:
            tile.update(deltaTime)
        for entity in self.entities:
            entity.update(deltaTime)
        
        self.checkCollisions()

    def checkCollisions (self):
        for entity in self.entities:
            # Check Mario/Entity collisions.
            if not isinstance(entity, Mario):
                mario = self.getMario()
                if entity.rect.colliderect(mario.rect):
                    entity.addCollision(mario)
                    mario.addCollision(entity)

            # Check Entity/World collisions.
            for tile in self.map:
                if tile.rect.colliderect(entity.rect):
                    entity.addCollision(tile)
                    tile.addCollision(entity)

    def removeEntity (self, entity):
        self.entities.remove(entity)

    def removeTile (self, tile):
        self.map.remove(tile)
                
    def getMario (self):
        for entity in self.entities:
            if isinstance(entity, Mario):
                return entity
        return None

    def draw (self):
        for tile in self.map:
            tile.draw()
        for entity in self.entities:
            entity.draw()

# 1-1
class LevelOneOne (Level):
    def __init__ (self, fileHandle):
        Level.__init__(self, fileHandle)

    def update (self, deltaTime):
        Level.update(self, deltaTime)
        return


####################################
# Globals
####################################

# Display
pygame.init()
screenSize = [1280,720]
screenBGColor = lightBlue

# Tiles
tileWidth = 50
blankTile = ' '
groundTile = 'g'
marioTile = 'm'
goombaTile = '@'
koopaTile = '#'
pipeTile = 'p'
blockTile = 'b'
questionTile = 'q'

# Levels
levelHandle = "1-1.txt"
level = LevelOneOne(levelHandle)

# Physics
gravity = 0.02
maxVelocity = 1

# Game
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("SMB")
camera = Camera()
clock = pygame.time.Clock()
running = True


####################################
# Functions
####################################

def collision_sides (a, b):
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

def should_fall (entity):
    for tile in level.map:
        sides = collision_sides(entity.rect, tile.rect)
        if sides.bottom:
            return False
    return True

def updateFall (entity, deltaTime):
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

def render ():
    screen.fill(screenBGColor)
    level.draw()
    pygame.display.flip()

def tick ():
    deltaTime = clock.tick(60)
    level.update(deltaTime)
    camera.update()
    

####################################
# Main loop
####################################

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    tick()
    render()

    mario = level.getMario()
    #if not mario is None and mario.isDead:
    if not mario is None and (mario.y > screenSize[1] or mario.isDead):
        print "Game Over"
        running = False

pygame.quit()



















