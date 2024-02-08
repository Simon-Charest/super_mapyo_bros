from pathlib import Path
from typing import List
from super_mapyo_bros.constants import light_blue

# Display
screen_size: List[int] = [1280,  720]
screen_bg_color: List[int] = light_blue

# Tiles
tile_width: int = 50
blank_tile: str = " "
ground_tile: str = "g"
mario_tile: str = "m"
goomba_tile: str = "@"
koopa_tile: str = "#"
pipe_tile: str = "p"
block_tile: str = "b"
q_coin_tile: str = "-"
q_mush_tile: str = "1"
q_one_up_tile: str = "2"
q_start_tile: str = "3"

# Levels
level_handle = Path(__file__).parent.joinpath("data/1-1.txt")

# Physics
gravity: float = 0.02
max_velocity: int = 1
