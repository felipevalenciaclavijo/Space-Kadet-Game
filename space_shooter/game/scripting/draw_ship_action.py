from constants import *
from game.scripting.action import Action


class DrawShipAction(Action):
    """Handles Drawing of the Ship Actor."""

    def __init__(self, video_service):
        """Creates the class DrawShipAction
        
        Args:
            video_service: an object that handles the window of the game.
        """
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Executes the action of drawing of the ship Actors.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        ship = cast.get_first_actor(SHIP_GROUP)
        body = ship.get_body()

        if ship.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = ship.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)