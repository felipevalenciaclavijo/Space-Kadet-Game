from game.casting.laser import Laser
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        laser = cast.get_first_actor(LASER_GROUP)
        body = laser.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        
                
    