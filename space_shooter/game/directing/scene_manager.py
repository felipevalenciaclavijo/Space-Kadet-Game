import csv
import random
from constants import *
from game.casting.animation import Animation
from game.casting.laser import Laser
from game.casting.body import Body
# from game.casting.brick import Brick
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.racket import Racket
from game.casting.ship import Ship
from game.casting.asteroid import Asteroid
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
# from game.scripting.check_over_action import CheckOverAction
# from game.scripting.collide_borders_action import CollideBordersAction
# from game.scripting.collide_brick_action import CollideBrickAction
# from game.scripting.collide_racket_action import CollideRacketAction

from game.scripting.control_ship_action import ControlShipAction
from game.scripting.control_asteroids_action import ControlAsteroidsAction
from game.scripting.control_laser_action import ControlLaserAction
from game.scripting.draw_asteroid_action import DrawAsteroidAction

# from game.scripting.control_racket_action import ControlRacketAction
from game.scripting.draw_laser_action import DrawLaserAction
# from game.scripting.draw_bricks_action import DrawBricksAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_racket_action import DrawRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_laser_action import MoveLaserAction
from game.scripting.move_asteroid_action import MoveAsteroidAction
from game.scripting.move_racket_action import MoveRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService
from game.services.keyboard_service import KeyboardService
from game.scripting.draw_ship_action import DrawShipAction
from game.scripting.move_ship_action import MoveShipAction


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    # CHECK_OVER_ACTION = CheckOverAction()
    # COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    # COLLIDE_BRICKS_ACTION = CollideBrickAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    # COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_SHIP_ACTION = ControlShipAction(KEYBOARD_SERVICE)
    CONTROL_LASER_ACTION = ControlLaserAction(KEYBOARD_SERVICE, AUDIO_SERVICE)
    CONTROL_ASTEROIDS_ACTION = ControlAsteroidsAction(KEYBOARD_SERVICE)
    DRAW_LASER_ACTION = DrawLaserAction(VIDEO_SERVICE)
    DRAW_ASTEROID_ACTION = DrawAsteroidAction(VIDEO_SERVICE)
    # DRAW_BRICKS_ACTION = DrawBricksAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_RACKET_ACTION= DrawRacketAction(VIDEO_SERVICE)
    DRAW_SHIP_ACTION= DrawShipAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_LASER_ACTION = MoveLaserAction()
    MOVE_RACKET_ACTION = MoveRacketAction()
    MOVE_ASTEROID_ACTION = MoveAsteroidAction()
    MOVE_SHIP_ACTION = MoveShipAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    
    

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_ship(cast)
        # self._add_asteroid(cast)
        
        # self._add_bricks(cast)
        
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        # self._add_asteroid(cast)
        # self._add_bricks(cast)
        self._add_ship(cast)
        self._add_dialog(cast, HOW_TO_SHOOT)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        
        self._add_ship(cast)
        self._add_dialog(cast, HOW_TO_SHOOT)
        # self._add_asteroid(cast)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        
        cast.clear_actors(DIALOG_GROUP)
        # self._add_asteroid(cast)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_SHIP_ACTION)
        script.add_action(INPUT, self.CONTROL_LASER_ACTION)
        script.add_action(INPUT, self.CONTROL_ASTEROIDS_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
       
        self._add_ship(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    
   

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    # def _add_racket(self, cast):
    #     cast.clear_actors(RACKET_GROUP)
    #     x = CENTER_X - RACKET_WIDTH / 2
    #     y = SCREEN_HEIGHT - RACKET_HEIGHT
    #     position = Point(x, y)
    #     size = Point(RACKET_WIDTH, RACKET_HEIGHT)
    #     velocity = Point(0, 0)
    #     body = Body(position, size, velocity)
    #     animation = Animation(RACKET_IMAGES, RACKET_RATE)
    #     racket = Racket(body, animation)
    #     cast.add_actor(RACKET_GROUP, racket)

       
            
            
                
            
            
                
            
            

    
    def _add_ship(self, cast):
        cast.clear_actors(SHIP_GROUP)
        x = CENTER_X - SHIP_WIDTH / 2
        y = SCREEN_HEIGHT - SHIP_HEIGHT
        position = Point(x, y)
        size = Point(SHIP_WIDTH, SHIP_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(SHIP_IMAGES, SHIP_RATE)
        ship = Ship(body, animation)
        cast.add_actor(SHIP_GROUP, ship)
    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_LASER_ACTION)
        script.add_action(OUTPUT, self.DRAW_ASTEROID_ACTION)
        # script.add_action(OUTPUT, self.DRAW_BRICKS_ACTION)
        script.add_action(OUTPUT, self.DRAW_SHIP_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_LASER_ACTION)
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION)
        script.add_action(UPDATE, self.MOVE_ASTEROID_ACTION)
        # script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        # script.add_action(UPDATE, self.COLLIDE_BRICKS_ACTION)
        # script.add_action(UPDATE, self.COLLIDE_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION)
        # script.add_action(UPDATE, self.CHECK_OVER_ACTION)