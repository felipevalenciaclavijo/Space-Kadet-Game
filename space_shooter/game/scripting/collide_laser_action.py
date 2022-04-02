from pickle import FALSE, TRUE
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.image import Image
from game.casting.point import Point


class CollideLaserAction(Action):
    """Handles collisions with laser actors."""

    def __init__(self, physics_service, audio_service, video_service):
        """Creates the CollideLaserAction
        
        Args:
            physics_service: an object that handles the physics of Actors.
            audio_service: an object that handles the audio of the game.
            video_service: an object that handles the window of the game.
        """
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Executes the action when a laser collides with an Asteroid actor. 
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        lasers = cast.get_actors(LASER_GROUP)
        asteroids = cast.get_actors(ASTEROID_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        if lasers != []:
            for laser in lasers:
                laser_body = laser.get_body()

                for asteroid in asteroids:
                    asteroid_body = asteroid.get_body()



                    if self._physics_service.has_collided(laser_body, asteroid_body):
                        if laser in lasers:
                            cast.remove_actor(LASER_GROUP, laser)
                        sound = Sound(LASER_HIT_SOUND)
                        self._audio_service.play_sound(sound)
                        hits = asteroid.get_hits()
                        stats.add_hits(hits)
                        points = asteroid.get_points()
                        stats.add_points(points)
                        old_image = asteroid.get_image() # get old image
                        old_image_file = old_image.get_filename() # get old image filename
                        size = asteroid_body.get_size() # get body size
                        next_image, next_size, remove = self._handle_asteroid(old_image_file, size) # handles asteroids
                        new_image = Image(next_image) 
                        asteroid.set_image(new_image) # replaces the image in asteroid
                        asteroid_body.set_size(next_size) # set new size
                        image = asteroid.get_image() # get latest asteroid image
                        position = asteroid_body.get_position() # get position of the body of the asteroid
                        self._video_service.draw_image(image, position) # use the video service to draw the new image
                        
                        if laser in lasers:
                            if remove == True:
                                cast.remove_actor(LASER_GROUP, laser)
                                cast.remove_actor(ASTEROID_GROUP, asteroid)

    
    def _handle_asteroid(self, image, size, remove = False):
        """changes asteroids images and sizes as well as decides
        when to remove asteroids.
        
        Args:
            image: The image filename of the current asteroid
            size: The current size of the asteroid.

        returns:
            A new image, new size, and a boolean value.
        """
        
        if image == GRAY_ASTEROID_IMAGE:
            new_image = GRAY_ASTEROID_B_IMAGE
            new_size = Point(GRAY_ASTEROID_B_WIDTH, GRAY_ASTEROID_B_HEIGHT)
        elif image == GRAY_ASTEROID_B_IMAGE:
            new_image = GRAY_ASTEROID_C_IMAGE
            new_size = Point(GRAY_ASTEROID_C_WIDTH, GRAY_ASTEROID_C_HEIGHT)
        elif image == BROWN_ASTEROID_IMAGE:
            new_image = BROWN_ASTEROID_B_IMAGE
            new_size = Point(BROWN_ASTEROID_B_WIDTH, BROWN_ASTEROID_B_HEIGHT)
        elif image == BROWN_ASTEROID_B_IMAGE:
            new_image = BROWN_ASTEROID_C_IMAGE
            new_size = Point(BROWN_ASTEROID_C_WIDTH, BROWN_ASTEROID_C_HEIGHT)
        elif image == GREEN_ASTEROID_IMAGE:
            new_image = GREEN_ASTEROID_B_IMAGE
            new_size = Point(GREEN_ASTEROID_B_WIDTH, GREEN_ASTEROID_B_HEIGHT)
        elif image == GREEN_ASTEROID_B_IMAGE:
            new_image = GREEN_ASTEROID_C_IMAGE
            new_size = Point(GREEN_ASTEROID_C_WIDTH, GREEN_ASTEROID_C_HEIGHT)
        else:
            new_image = image
            new_size = size
            remove = True
        return new_image, new_size, remove