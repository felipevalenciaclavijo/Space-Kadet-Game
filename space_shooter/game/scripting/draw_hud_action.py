from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):
    """Handles Drawing of the HUD"""

    def __init__(self, video_service):
        """Creates the class DrawHudAction
        
        Args:
            video_service: an object that handles the window of the game.
        """
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """Executes the action of drawing of the HUD
        
        Args:
            cast: an object that holds all actors needed for the scene 
            script: an object that tells the actors what to do.
            callback: Calls the actions to be executed.
        """
        stats = cast.get_first_actor(STATS_GROUP)
        self._draw_label(cast, HITS_GROUP, HITS_FORMAT, stats.get_hits())
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats.get_lives())
        self._draw_label(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score())

    def _draw_label(self, cast, group, format_str, data):
        """Draws messages to the game window.
        
        Args:
            cast: an object that holds all actors needed for the scene 
            group: a string that is a key to access the specified group of the cast.
            format_str: a string that holds space for formating.
            data: the data to be formated into the format_str.
        """
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)