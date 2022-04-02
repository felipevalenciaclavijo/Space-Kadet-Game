from game.scripting.action import Action


class EndDrawingAction(Action):
    """Handles the Buffer of drawing the screen."""

    def __init__(self, video_service):
        """Creates the class EndDrawingAction
        
        Args:
            video_service: an object that handles the window of the game.
        """
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Executes the action of flashing the drawing memory to the screen.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """

        self._video_service.flush_buffer()