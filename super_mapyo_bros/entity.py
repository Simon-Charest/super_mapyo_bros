from pygame import Rect, Surface
from pygame.draw import rect
from super_mapyo_bros.camera import Camera
from typing import List, Type


class Entity(object):
    x: float = 0
    y: float = 0
    w: float = 0
    h: float = 0
    rect: Rect = Rect(x, y, w, h)
    color: List[int] = [0, 0, 0]
    direction: str = "right"
    curr_state = None
    prev_state = None
        
    def __init__(self, x: float, y: float, w: float, h: float, color: List[int]) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = Rect(x, y, w, h)
        self.all_states = {}
        self.colliding_objects = []
        self.has_collision = False

    def left(self) -> int:
        return self.x
    
    def right(self) -> int:
        return self.x + self.w
    
    def bottom(self) -> int:
        return self.y + self.h
    
    def top(self) -> int:
        return self.y
    
    def set_y(self, y: float) -> None:
        self.y = y
        self.rect = Rect(self.x, self.y, self.w, self.h)

    def set_x(self, x: float) -> None:
        self.x = x
        self.rect = Rect(self.x, self.y, self.w, self.h)

    def translate(self, dx: float, dy: float) -> None:
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

    def change_state(self, stateID: str) -> None:
        if not self.all_states.get(stateID):
            return
        
        else:
            self.new_state = self.all_states.get(stateID)
            self.curr_state.exit_state(self)
            self.prev_state = self.curr_state
            self.curr_state = self.new_state
            self.curr_state.enter_state(self)

    def add_collision(self, collided: Type["Entity"]) -> None:
        self.colliding_objects.append(collided)
        self.has_collision = True

    def draw(self, screen: Surface, camera: Camera) -> None:
        rect(screen, self.color, [self.x - camera.x, self.y - camera.y, self.w, self.h], 0)
