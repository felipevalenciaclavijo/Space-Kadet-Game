from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.laser import Laser
from game.casting.body import Body


class ControlLaserAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        
       
       if self._keyboard_service.is_key_down(SPACE): 
           laser = self._add_laser(cast)
           laser.release()
        
     

    def _add_laser(self, cast):
        # cast.clear_actors(LASER_GROUP)
        # x = CENTER_X - LASER_WIDTH / 2
        # y = SCREEN_HEIGHT - SHIP_HEIGHT - LASER_HEIGHT
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