from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class DrawAsteroidAction(Action):
    """Handles Drawing of the Astroid Actors"""

    def __init__(self, video_service):
        """Creates the DrawAsteroidAction
        
        Args:
            video_service: an object that handles the window of the game.
        """
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Executes the action of drawing of asteroid Actors.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
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