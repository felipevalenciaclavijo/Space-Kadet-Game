from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideAsteroidAction(Action):
    """Handles collisions with the Asteroid Actor"""

    def __init__(self, physics_service, audio_service):
        """Creates the CollideAsteroidAction
        
        Args:
            physics_service: an object that handles the physics of Actors.
            audio_service: an object that handles the audio of the game.
        """
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        """Executes the actions when an astroid has collided with an object.

        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        ship = cast.get_first_actor(SHIP_GROUP)
        asteroids = cast.get_actors(ASTEROID_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        over_sound = Sound(OVER_SOUND)
        crash_sound = Sound(ASTEROID_HITS_SHIP_SOUND)
        
        for asteroid in asteroids:
            ship_body = ship.get_body()
            asteroid_body = asteroid.get_body()

            if self._physics_service.has_collided(ship_body, asteroid_body):
   
                hits = asteroid.get_hits()
                stats.add_hits(hits)
                points = asteroid.get_points()
                stats.add_points(points)
                cast.clear_actors(ASTEROID_GROUP) # Eliminates all the asteroids - Felipe
                cast.clear_actors(LASER_GROUP)
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
            
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN)
                    self._audio_service.play_sound(crash_sound) 
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)