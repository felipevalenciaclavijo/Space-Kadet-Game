from constants import *
from game.scripting.action import Action


class ControlShipAction(Action):
    """Handles movement of the Ship Actor"""

    def __init__(self, keyboard_service):
        """Creates the ControlShipAction
        
        Args: 
            keyboard_service: An object that handles keyboard actions.
        """

        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        """Executes the action of controling the ship Actor.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        ship = cast.get_first_actor(SHIP_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            ship.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            ship.move_right()
        elif self._keyboard_service.is_key_down(UP):
            ship.move_up()
        elif self._keyboard_service.is_key_down(DOWN):  
            ship.move_down()
        else: 
            ship.stop_moving()  