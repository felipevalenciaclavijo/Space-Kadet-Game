from constants import *
from game.scripting.action import Action


class ControlShipAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
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