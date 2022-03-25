from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Asteroid(Actor):
    """A space rock."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Asteroid.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the asteroid's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the asteroid's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def fall(self):
        """Release the asteroid downward."""
        
        vx = 0
        vy = ASTEROID_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)