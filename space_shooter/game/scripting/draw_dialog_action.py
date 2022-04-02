from constants import *
from game.scripting.action import Action


class DrawDialogAction(Action):
    """Handles Drawing of Dialog"""

    def __init__(self, video_service):
        """Creates the class DrawDialogAction
        
        Args:
            video_service: an object that handles the window of the game.
        """
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Executes the action of drawing of Dialog.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        dialogs = cast.get_actors(DIALOG_GROUP)
        for dialog in dialogs:
            text = dialog.get_text()
            position = dialog.get_position()
            self._video_service.draw_text(text, position)