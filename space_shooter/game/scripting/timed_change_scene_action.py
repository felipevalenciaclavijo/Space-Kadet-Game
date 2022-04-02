import time
from game.scripting.action import Action


class TimedChangeSceneAction(Action):
    """Handles the changing to a new scene after a given time"""

    def __init__(self, next_scene, delay):
        """Creates the CollideLaserAction
        
        Args:
            next_scene: the new scene that needs to be chagned to.
            delay: the length of the delay between changing scenes.
        """
        self._next_scene = next_scene
        self._delay = delay
        self._start = time.time()
        
    def execute(self, cast, script, callback):
        """Executes the action of changing scenes with the given delay.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        elapsed = time.time() - self._start
        if elapsed >= self._delay:
            callback.on_next(self._next_scene)