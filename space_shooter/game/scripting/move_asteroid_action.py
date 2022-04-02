from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class MoveAsteroidAction(Action):
    """Moves the astroid actors on the screen."""

    def __init__(self):
        """Creates the class MoveAsteroidAction"""
        pass
        
    def execute(self, cast, script, callback):
        """Executes the action of moving the astroid actors.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        asteroids = cast.get_actors(ASTEROID_GROUP)
        for asteroid in asteroids:
        
            if asteroid == None:
                return

            
            body = asteroid.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
            
                

               