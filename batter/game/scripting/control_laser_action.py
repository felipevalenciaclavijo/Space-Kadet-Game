from constants import *
from game.scripting.action import Action


class ControlLaserAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        laser = cast.get_first_actor(LASER_GROUP)
       
        if self._keyboard_service.is_key_down(SPACE): 
            laser.release()
        
        else: 
            laser.get_body()
            laser.get_image() 