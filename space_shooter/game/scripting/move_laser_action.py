from constants import *
from game.scripting.action import Action


class MoveLaserAction(Action):
    """Moves the Laser actors on the screen."""

    def __init__(self):
        """Creates the class MoveLaserAction"""
        pass
        
    def execute(self, cast, script, callback):
        """Executes the action of moving the Laser actors.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        lasers = cast.get_actors(LASER_GROUP)
        for laser in lasers:
        
            if laser == None:
                return

            
            body = laser.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)

            
            
            

            

            