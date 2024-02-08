from super_mapyo_bros.constants import *
from super_mapyo_bros.globals import *
from super_mapyo_bros.block.brick_block import BrickBlock
from super_mapyo_bros.block.ground_block import GroundBlock
from super_mapyo_bros.block.pipe import Pipe
from super_mapyo_bros.block.question_block import QuestionBlock
from super_mapyo_bros.enemy.goomba import Goomba
from super_mapyo_bros.enemy.koopa import Koopa
from super_mapyo_bros.coin.coin import Coin
from super_mapyo_bros.mario.mario import Mario
from super_mapyo_bros.power_up.mushroom import Mushroom


class Level:
    def __init__(self, fileHandle) -> None:
        self.f = open(fileHandle)
        self.tileRows = self.f.readlines()
        self.map = []
        self.entities = []
        i = 0

        for row in self.tileRows:
            j = 0

            for tile in row:
                self.load_item(tile, j, i)
                j += 1

            i += 1

        # Add reusable items.
        self.entities.append(Coin(-100, 0, 10, 30, coin_color))
        self.entities.append(Mushroom(-100, 100, tile_width, tile_width, mushroom_color, self))
        #self.entities.append(Star(-100, 200, tile_width, tile_width, star_color))
        #self.entities.append(OneUp(-100, 300, tile_width, tile_width, one_up_color))
        #self.entities.append(Flower(-100, 400, tile_width, tile_width, flower_color))

    def load_item(self, tile, x, y) -> None:
        xPos = x * tile_width
        yPos = y * tile_width

        if (tile == blank_tile):
            return
        
        elif (tile == ground_tile):
            self.map.append(GroundBlock(xPos, yPos, tile_width, tile_width, ground_brown))

        elif (tile == mario_tile):
            self.entities.append(Mario(xPos, yPos + 10, tile_width - 10, tile_width - 10, white, self))

        elif (tile == block_tile):
            self.map.append(BrickBlock(xPos, yPos, tile_width, tile_width, brick_brown))

        elif (tile == q_coin_tile):
            self.map.append(QuestionBlock(xPos, yPos, tile_width, tile_width, "coin", gold, self))

        elif (tile == q_mush_tile):
            self.map.append(QuestionBlock(xPos, yPos, tile_width, tile_width, "mushroom", gold, self))

        elif (tile == pipe_tile):
            self.map.append(Pipe(xPos, yPos, tile_width, tile_width, green))

        elif (tile == goomba_tile):
            self.entities.append(Goomba(xPos, yPos, tile_width, tile_width, xPos - screen_size[0] / 2, goomba_color))

        elif (tile == koopa_tile):
            self.entities.append(Koopa(xPos, yPos, tile_width, tile_width, xPos - screen_size[0] / 2, koopa_color))

    def update(self, delta_time) -> None:
        for tile in self.map:
            tile.update(delta_time)

        for entity in self.entities:
            entity.update(delta_time)
        
        self.check_collisions()

    def check_collisions(self) -> None:
        for entity in self.entities:
            # Check Mario/Entity collisions.
            if not isinstance(entity, Mario):
                mario = self.get_mario()

                if entity.rect.colliderect(mario.rect):
                    entity.add_collision(mario)
                    mario.add_collision(entity)

            # Check Entity/World collisions.
            for tile in self.map:
                if tile.rect.colliderect(entity.rect):
                    entity.add_collision(tile)
                    tile.add_collision(entity)

    def remove_entity(self, entity) -> None:
        self.entities.remove(entity)

    def remove_tile(self, tile) -> None:
        self.map.remove(tile)

    def add_entity(self, entity) -> None:
        self.entities.append(entity)
                
    def get_mario(self) -> Mario:
        for entity in self.entities:
            if isinstance(entity, Mario):
                return entity
            
        return None

    def draw(self, screen, camera) -> None:
        for tile in self.map:
            tile.draw(screen, camera)

        for entity in self.entities:
            entity.draw(screen, camera)
