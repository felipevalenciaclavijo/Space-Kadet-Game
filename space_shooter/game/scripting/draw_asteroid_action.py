from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class DrawAsteroidAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        asteroids = cast.get_actors(ASTEROID_GROUP)
        for asteroid in asteroids:
        
            body = asteroid.get_body()

            if asteroid.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            
            image = asteroid.get_image()
            position = body.get_position()

            x = position.get_x()
            y = position.get_y()

            if y >= (FIELD_BOTTOM):
                y = FIELD_TOP
                position = Point(x, (y - 44))
                body.set_position(position)

            self._video_service.draw_image(image, position)