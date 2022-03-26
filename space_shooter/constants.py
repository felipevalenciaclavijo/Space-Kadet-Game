from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Space Shooter"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 0
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "space_shooter/assets/fonts\\zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "space_shooter/assets/sounds\\laser_shoot.mp3"
WELCOME_SOUND = "space_shooter/assets/sounds\\space_music.mp3"
OVER_SOUND = "space_shooter/assets/sounds\\game_over.mp3"
LASER_SHOOT_SOUND = "space_shooter/assets/sounds\\laser_shoot.mp3"
LASER_HIT_SOUND = "space_shooter/assets/sounds\\laser_hit.mp3"
ASTEROID_HITS_SHIP_SOUND = "space_shooter/assets/sounds\\ship_crash.mp3"


# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
#LEVEL_FILE = "space_shooter/assets/data\\level-{:03}.txt"
#BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
#LEVEL_GROUP = "level"
HITS_GROUP = "hits"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
HITS_FORMAT = "HITS: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# # BALL
# BALL_GROUP = "balls"
# BALL_IMAGE = "space_shooter/assets/images\\000.png"
# BALL_WIDTH = 28
# BALL_HEIGHT = 28
# BALL_VELOCITY = 6

# # FANCIER ASTEROID GROUP WITH MULTIPLE ATTRIBUTES - NEEDS WORK
# ASTEROID_GROUP = "asteroids"
# ASTEROID_IMAGES = {
#     "gray": [["space_shooter/assets/images\\asteroid1.png"], 44, 44],
#     "green": [["space_shooter/assets/images\\asteroid3.png"], 43, 44],
#     "brown": [["space_shooter/assets/images\\asteroid2.png"], 39, 44]
# }
# ASTEROID_WIDTH = ASTEROID_IMAGES[key][1]
# ASTEROID_HEIGHT = ASTEROID_IMAGES[key][2]
# ASTEROID_VELOCITY = 6


# ASTEROIDS
ASTEROID_GROUP = "asteroids"
ASTEROID_VELOCITY = 3
GRAY_ASTEROID_IMAGE = "space_shooter/assets/images\\asteroid1.png"
GRAY_ASTEROID_WIDTH = 44
GRAY_ASTEROID_HEIGHT = 44
BROWN_ASTEROID_IMAGE = "space_shooter/assets/images\\asteroid2.png"
BROWN_ASTEROID_WIDTH = 39
BROWN_ASTEROID_HEIGHT = 44
GREEN_ASTEROID_IMAGE = "space_shooter/assets/images\\asteroid3.png"
GREEN_ASTEROID_WIDTH = 43
GREEN_ASTEROID_HEIGHT = 44





# LASER
LASER_GROUP = "lasers"
LASER_IMAGE = "space_shooter/assets/images\\laser.png"
LASER_WIDTH = 4
LASER_HEIGHT = 6
LASER_VELOCITY = 6

# RACKET
# RACKET_GROUP = "rackets"
# RACKET_IMAGES = ["space_shooter/assets/images\\ship.png"]
# RACKET_WIDTH = 106
# RACKET_HEIGHT = 28
# RACKET_RATE = 6
# RACKET_VELOCITY = 7

# SHIP
SHIP_GROUP = "ships"
SHIP_IMAGES = ["space_shooter/assets/images\\ship.png"]
SHIP_WIDTH = 28
SHIP_HEIGHT = 39
SHIP_RATE = 6
SHIP_VELOCITY = 4

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "b": [f"space_shooter/assets/images\\{i:03}.png" for i in range(10,19)],
    "g": [f"space_shooter/assets/images\\{i:03}.png" for i in range(20,29)],
    "p": [f"space_shooter/assets/images\\{i:03}.png" for i in range(30,39)],
    "y": [f"space_shooter/assets/images\\{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
HOW_TO_SHOOT = "PRESS SPACE BAR TO SHOOT"
WAS_GOOD_GAME = "GAME OVER"