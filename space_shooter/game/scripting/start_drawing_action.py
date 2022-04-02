from game.scripting.action import Action


class StartDrawingAction(Action):
    """clears the buffer to draw a blank frame."""

    def __init__(self, video_service):
        """Creates the StartDrawingAction
        
        Args:
            video_service: an object that handles the window of the game.
        """
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Executes the action of clearing the buffer to draw a new frame. 
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        self._video_service.clear_buffer()