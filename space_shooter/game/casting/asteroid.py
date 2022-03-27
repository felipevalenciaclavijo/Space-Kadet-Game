from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Asteroid(Actor):
    """A space rock."""
    
    def __init__(self, body, image, points, debug = False):
        """Constructs a new Asteroid.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._points = points # morgan added

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
    
    def get_points(self): # morgan added
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points