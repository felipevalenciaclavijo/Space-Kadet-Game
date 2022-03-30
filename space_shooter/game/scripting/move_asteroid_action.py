from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class MoveAsteroidAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        asteroids = cast.get_actors(ASTEROID_GROUP)
        for asteroid in asteroids:
        
            if asteroid == None:
                return

            
            body = asteroid.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
            
                

               