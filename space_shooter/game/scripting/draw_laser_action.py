from constants import *
from game.scripting.action import Action


class DrawLaserAction(Action):
    """Handles Drawing of the laser Actor."""

    def __init__(self, video_service):
        """Creates the class DrawLaserAction
        
        Args:
            video_service: an object that handles the window of the game.
        """
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Executes the action of drawing of the Laser Actors.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        
        lasers = cast.get_actors(LASER_GROUP)
        for laser in lasers:

            if laser == None:
                return

            else:
                body = laser.get_body()

                if laser.is_debug():
                    rectangle = body.get_rectangle()
                    self._video_service.draw_rectangle(rectangle, PURPLE)
                    
                image = laser.get_image()
                position = body.get_position()

                y = position.get_y()
                if y <= FIELD_TOP:
                    cast.remove_actor(LASER_GROUP, laser)


                self._video_service.draw_image(image, position)