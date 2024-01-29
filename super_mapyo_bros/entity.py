from pygame import Rect
from pygame.draw import rect
    

class Entity(object):
    x = 0
    y = 0
    w = 0
    h = 0
    rect = Rect(x,y,w,h)
    color = [0,0,0]
    direction = "right"
    currState = None
    prevState = None
        
    def __init__(self, x, y, w, h, color) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = Rect(x,y,w,h)
        self.allStates = {}
        self.collidingObjects = []
        self.hasCollision = False

    def left(self) -> int:
        return self.x
    
    def right(self) -> int:
        return self.x + self.w
    
    def bottom(self) -> int:
        return self.y + self.h
    
    def top(self) -> int:
        return self.y
    
    def setY(self, y) -> None:
        self.y = y
        self.rect = Rect(self.x, self.y, self.w, self.h)

    def setX(self, x) -> None:
        self.x = x
        self.rect = Rect(self.x, self.y, self.w, self.h)

    def translate(self, dx, dy) -> None:
        from super_mapyo_bros.mario.mario import Mario

        if dx < 0:
            self.direction = "left"

        elif dx > 0:
            self.direction = "right"

        self.x += dx

        if isinstance(self, Mario) and self.x < 0:
            self.x = 0
        
        self.y += dy
        self.rect = Rect(self.x,self.y,self.w,self.h)

    def changeState(self, stateID) -> None:
        if self.allStates.get(stateID) is None:
            return
        
        else:
            self.newState = self.allStates.get(stateID)
            self.currState.exitState(self)
            self.prevState = self.currState
            self.currState = self.newState
            self.currState.enterState(self)

    def addCollision(self, collided) -> None:
        self.collidingObjects.append(collided)
        self.hasCollision = True

    def draw(self, screen, camera) -> None:
        rect(screen, self.color, [self.x - camera.x, self.y - camera.y, self.w, self.h], 0)
