from constants import *
from game.scripting.action import Action


class MoveLaserAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        laser = cast.get_first_actor(LASER_GROUP)
        
        if laser == None:
            return

        
        body = laser.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)