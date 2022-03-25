from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Laser(Actor):
    """A fiery space bullet that is shot at asteroids."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Laser.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the laser's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the laser's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def release(self):
        """Release the laser straight upward."""
        
        vx = 0
        vy = -LASER_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)