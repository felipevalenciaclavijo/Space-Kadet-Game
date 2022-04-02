from constants import *
from game.scripting.action import Action


class ChangeSceneAction(Action):
    """Changes the current scene to different scene"""

    def __init__(self, keyboard_service, next_scene):
        """Constructs a new ChangeSceneAction"""
        self._keyboard_service = keyboard_service
        self._next_scene = next_scene
        
    def execute(self, cast, script, callback):
        """Executes the scene change.

        Args:
            cast: An object the holds actors.
            script: An object that holds actions.
            callback: Calls the actions to be executed.
        """
        if self._keyboard_service.is_key_pressed(ENTER):
            callback.on_next(self._next_scene)