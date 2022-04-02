from game.scripting.action import Action


class UnloadAssetsAction(Action):
    """Handles unloading assets of the video and audio services."""

    def __init__(self, audio_service, video_service):
        """Creates the UnloadAssetsAction
        
        Args:
            audio_service: an object that handles the audio of the game.
            video_service: an object that handles the window of the game.
        """
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        """Executes the action when a laser collides with an Asteroid actor. 
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        self._audio_service.unload_sounds()
        self._video_service.unload_fonts()
        self._video_service.unload_images()