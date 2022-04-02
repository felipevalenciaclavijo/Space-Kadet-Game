from game.scripting.action import Action


class InitializeDevicesAction(Action):

    def __init__(self, audio_service, video_service):
        """Creates the class InitializeDevicesAction
        
        Args:
            video_service: an object that handles the window of the game.
            audio_service: an object that handles the audio of the game.
        """
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        """Executes the action of initializing the audio and video services.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        self._audio_service.initialize()
        self._video_service.initialize()