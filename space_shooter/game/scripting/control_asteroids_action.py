from constants import *
import random
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.asteroid import Asteroid
from game.casting.body import Body


class ControlAsteroidsAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._count = 0
        
    def execute(self, cast, script, callback):
        
       self._count += 1

       if (self._count % 10) == 0: 
           asteroid = self._add_asteroid(cast)
           asteroid.fall()
        
     
    def _add_asteroid(self, cast):
        
        asteroid_options = [GREEN_ASTEROID_IMAGE, GRAY_ASTEROID_IMAGE, BROWN_ASTEROID_IMAGE]
        image_file = random.choice(asteroid_options)
        if image_file == GREEN_ASTEROID_IMAGE:
            x = random.randint(0, (SCREEN_WIDTH - GREEN_ASTEROID_WIDTH))
            y = 0 - GREEN_ASTEROID_HEIGHT
            size = Point(GREEN_ASTEROID_WIDTH, GREEN_ASTEROID_HEIGHT)
            

        elif image_file == GRAY_ASTEROID_IMAGE:
            x = random.randint(0, (SCREEN_WIDTH - GRAY_ASTEROID_WIDTH))
            y = 0 - GRAY_ASTEROID_HEIGHT
            size = Point(GRAY_ASTEROID_WIDTH, GRAY_ASTEROID_HEIGHT)
            

        elif image_file == BROWN_ASTEROID_IMAGE:
            x = random.randint(0, (SCREEN_WIDTH - BROWN_ASTEROID_WIDTH))
            y = 0 - GREEN_ASTEROID_HEIGHT
            size = Point(BROWN_ASTEROID_WIDTH, BROWN_ASTEROID_HEIGHT)
        
        image = Image(image_file)
        position = Point(x, y)
        velocity = Point(0, ASTEROID_VELOCITY)
        body = Body(position, size, velocity)
        
        asteroid = Asteroid(body, image)
        cast.add_actor(ASTEROID_GROUP, asteroid)
        return asteroid



    