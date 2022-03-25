from constants import *
from game.scripting.action import Action


class DrawLaserAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        
        laser = cast.get_first_actor(LASER_GROUP)

        if laser == None:
            return

        else:
            body = laser.get_body()

            if laser.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = laser.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)