from game.scripting.action import Action


class LoadAssetsAction(Action):
    """Loads assets that are needed for the game to run."""

    def __init__(self, audio_service, video_service):
        """Creates the class LoadAssetsAction
        
        Args:
            video_service: an object that handles the window of the game.
            audio_service: an object that handles the audio of the game.
        """
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        """Executes the action of loading assets that are needed for the function of the game.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        self._audio_service.load_sounds("space_shooter/assets/sounds")
        self._video_service.load_fonts("space_shooter/assets/fonts")
        self._video_service.load_images("space_shooter/assets/images")
        