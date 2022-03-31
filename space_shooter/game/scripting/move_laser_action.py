from constants import *
from game.scripting.action import Action


class MoveLaserAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        lasers = cast.get_actors(LASER_GROUP)
        for laser in lasers:
        
            if laser == None:
                return

            
            body = laser.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)

            
            
            

            

            