from game.casting.laser import Laser
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):
    """Handles collisions with the window borders."""

    def __init__(self, physics_service, audio_service):
        """Creates the CollideBordersAction
        
        Args:
            physics_service: an object that handles the physics of Actors.
            audio_service: an object that handles the audio of the game.
        """
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        """Executes the action when an Actor collides with the border of the game window.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        laser = cast.get_first_actor(LASER_GROUP)
        body = laser.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        
                
    