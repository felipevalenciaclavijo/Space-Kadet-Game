from constants import *
from game.scripting.action import Action


class MoveAsteroidAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        asteroid = cast.get_first_actor(ASTEROID_GROUP)
        
        if asteroid == None:
            return

        
        body = asteroid.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)