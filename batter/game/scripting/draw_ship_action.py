from constants import *
from game.scripting.action import Action


class DrawShipAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        body = ship.get_body()

        if ship.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        
        image = SHIP_IMAGE
        position = body.get_position()
        self._video_service.draw_image(image, position)