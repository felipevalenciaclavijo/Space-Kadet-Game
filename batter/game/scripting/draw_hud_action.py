from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        self._draw_label(cast, LEVEL_GROUP, LEVEL_FORMAT, stats.get_level())
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats.get_lives())
        self._draw_label(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score())

    # **********************************************************************************************
    # You found the bug. Great job!
    # **********************************************************************************************
    # todo: fix the bug by making sure the text value is set to the appropriate variable.
    def _draw_label(self, cast, group, format_str, data):
        the_value_to_display = format_str.format(data)
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str)
        position = label.get_position()
        self._video_service.draw_text(text, position)