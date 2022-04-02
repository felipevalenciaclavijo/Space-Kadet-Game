from constants import *
from game.scripting.action import Action
from game.casting.sound import Sound


class PlaySoundAction(Action):
    """Plays sounds of the game."""

    def __init__(self, audio_service, filename):
        """Creates the class PlaySoundAction
        
        Args:
            audio_service: an object that handles the audio of the game.
            filename: The file name of the sound needed to be played.
        """
        self._audio_service = audio_service
        self._filename = filename
        
    def execute(self, cast, script, callback):
        """Executes the action of playing sounds of the game.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        sound = Sound(self._filename)
        self._audio_service.play_sound(sound)
        script.remove_action(OUTPUT, self)