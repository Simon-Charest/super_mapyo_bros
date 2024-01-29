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
                self.loadItem(tile, j, i)
                j += 1

            i += 1

        # Add reusable items.
        self.entities.append(Coin(-100, 0, 10, 30, coinColor))
        self.entities.append(Mushroom(-100, 100, tileWidth, tileWidth, mushroomColor, self))
        #self.entities.append(Star(-100, 200, tileWidth, tileWidth, starColor))
        #self.entities.append(OneUp(-100, 300, tileWidth, tileWidth, oneUpColor))
        #self.entities.append(Flower(-100, 400, tileWidth, tileWidth, flowerColor))

    def loadItem(self, tile, x, y) -> None:
        xPos = x * tileWidth
        yPos = y * tileWidth

        if (tile == blankTile):
            return
        
        elif (tile == groundTile):
            self.map.append(GroundBlock(xPos, yPos, tileWidth, tileWidth, groundBrown))

        elif (tile == marioTile):
            self.entities.append(Mario(xPos, yPos+10, tileWidth-10, tileWidth-10, white, self))

        elif (tile == blockTile):
            self.map.append(BrickBlock(xPos, yPos, tileWidth, tileWidth, brickBrown))

        elif (tile == qCoinTile):
            self.map.append(QuestionBlock(xPos, yPos, tileWidth, tileWidth, "coin", gold, self))

        elif (tile == qMushTile):
            self.map.append(QuestionBlock(xPos, yPos, tileWidth, tileWidth, "mushroom", gold, self))

        elif (tile == pipeTile):
            self.map.append(Pipe(xPos, yPos, tileWidth, tileWidth, green))

        elif (tile == goombaTile):
            self.entities.append(Goomba(xPos, yPos, tileWidth, tileWidth, xPos - screenSize[0]/2, goombaColor))

        elif (tile == koopaTile):
            self.entities.append(Koopa(xPos, yPos, tileWidth, tileWidth, xPos - screenSize[0]/2, koopaColor))

    def update(self, deltaTime) -> None:
        for tile in self.map:
            tile.update(deltaTime)

        for entity in self.entities:
            entity.update(deltaTime)
        
        self.checkCollisions()

    def checkCollisions(self) -> None:
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

    def removeEntity(self, entity) -> None:
        self.entities.remove(entity)

    def removeTile(self, tile) -> None:
        self.map.remove(tile)

    def addEntity(self, entity) -> None:
        self.entities.append(entity)
                
    def getMario(self) -> None:
        for entity in self.entities:
            if isinstance(entity, Mario):
                return entity
            
        return None

    def draw(self, screen, camera) -> None:
        for tile in self.map:
            tile.draw(screen, camera)

        for entity in self.entities:
            entity.draw(screen, camera)
