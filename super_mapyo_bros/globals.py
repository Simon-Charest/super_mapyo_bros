from pathlib import Path
from super_mapyo_bros.constants import lightBlue

# Display
screenSize = [1280,720]
screenBGColor = lightBlue

# Tiles
tileWidth = 50
blankTile = " "
groundTile = "g"
marioTile = "m"
goombaTile = "@"
koopaTile = "#"
pipeTile = "p"
blockTile = "b"
qCoinTile = "-"
qMushTile = "1"
qOneUpTile = "2"
qStarTile = "3"

# Levels
levelHandle = Path(__file__).parent.joinpath("data/1-1.txt")

# Physics
gravity = 0.02
maxVelocity = 1
