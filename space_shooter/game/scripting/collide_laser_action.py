from pickle import TRUE
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideLaserAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        lasers = cast.get_actors(LASER_GROUP)
        asteroids = cast.get_actors(ASTEROID_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        if lasers != []:
            for laser in lasers:
                laser_body = laser.get_body()

                for asteroid in asteroids:
                    laser_body = laser.get_body()
                    asteroid_body = asteroid.get_body()

                    if self._physics_service.has_collided(laser_body, asteroid_body):
                        sound = Sound(LASER_HIT_SOUND)
                        self._audio_service.play_sound(sound)
                        points = asteroid.get_points()
                        stats.add_points(points)
                        cast.remove_actor(ASTEROID_GROUP, asteroid)
                        cast.remove_actor(LASER_GROUP, laser)




                    