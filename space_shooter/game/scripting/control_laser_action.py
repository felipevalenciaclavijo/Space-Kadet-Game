from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.laser import Laser
from game.casting.body import Body
from game.casting.sound import Sound



class ControlLaserAction(Action):
    """Handles the actions of the laser Actor."""

    def __init__(self, keyboard_service, audio_service):
        """Creates the ControlLaserAction

        Args:
            keyboard_service: An object that handles keyboard actions.
            audio_service: an object that handles the audio of the game.
        """
        self._keyboard_service = keyboard_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        """Executes the action when a laser collides with an Asteroid actor. 
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        
        if self._keyboard_service.is_key_pressed(SPACE): 
           laser = self._add_laser(cast)
           sound = Sound(LASER_SHOOT_SOUND)
           self._audio_service.play_sound(sound)
           laser.release()
        
     

    def _add_laser(self, cast):
        """Adds laser Actors to the cast.
        
        Args:
            cast: an object that holds all actors needed for the scene
        """
        
        ship = cast.get_first_actor(SHIP_GROUP)
        ship_position = ship.get_body().get_position()
        x = ship_position.get_x() + (SHIP_WIDTH / 2) - (LASER_WIDTH / 2)
        y = ship_position.get_y() - 2  
        position = Point(x, y)
        size = Point(LASER_WIDTH, LASER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(LASER_IMAGE)
        laser = Laser(body, image, True)
        cast.add_actor(LASER_GROUP, laser)
        return laser