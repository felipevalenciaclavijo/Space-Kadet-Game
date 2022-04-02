from constants import *
from game.casting.animation import Animation
from game.casting.laser import Laser
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.ship import Ship
from game.casting.asteroid import Asteroid
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.collide_asteroid_action import CollideAsteroidAction # Added this one - Felipe
from game.scripting.collide_laser_action import CollideLaserAction
from game.scripting.control_ship_action import ControlShipAction
from game.scripting.control_asteroids_action import ControlAsteroidsAction
from game.scripting.control_laser_action import ControlLaserAction
from game.scripting.draw_asteroid_action import DrawAsteroidAction
from game.scripting.draw_laser_action import DrawLaserAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_laser_action import MoveLaserAction
from game.scripting.move_asteroid_action import MoveAsteroidAction
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
    COLLIDE_ASTEROIDS_ACTION = CollideAsteroidAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_LASER_ACTION = CollideLaserAction(PHYSICS_SERVICE, AUDIO_SERVICE, VIDEO_SERVICE)
    CONTROL_SHIP_ACTION = ControlShipAction(KEYBOARD_SERVICE)
    CONTROL_LASER_ACTION = ControlLaserAction(KEYBOARD_SERVICE, AUDIO_SERVICE)
    CONTROL_ASTEROIDS_ACTION = ControlAsteroidsAction(KEYBOARD_SERVICE)
    DRAW_LASER_ACTION = DrawLaserAction(VIDEO_SERVICE)
    DRAW_ASTEROID_ACTION = DrawAsteroidAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_SHIP_ACTION= DrawShipAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_LASER_ACTION = MoveLaserAction()
    MOVE_ASTEROID_ACTION = MoveAsteroidAction()
    MOVE_SHIP_ACTION = MoveShipAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    
    

    def __init__(self):
        """Constructs a new SceneManager."""
        pass

    def prepare_scene(self, scene, cast, script):
        """Prepares each scene of the instance of the game.
        
        Args:
            scene: an integer that chooses which scene to play
            cast: an object that holds all actors needed for the scene
            script: an object that tells the actors what to do.
        """
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
        """Prepares a new game scene to be displayed in the game window
        
            Args:
                cast: an object that holds all actors needed for the scene
                script: an object that tells the actors what to do.
        """
        self._add_stats(cast)
        self._add_hits(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_ship(cast)
        self._add_dialog(cast, ENTER_TO_START)
        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        """Prepares a level to be displayed in the game window
        
            Args:
                cast: an object that holds all actors needed for the scene
                script: an object that tells the actors what to do.
        """
        self._add_ship(cast)
        self._add_dialog(cast, HOW_TO_SHOOT)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        """Prepares the new game scene to be displayed in the game window
        
            Args:
                cast: an object that holds all actors needed for the scene
                script: an object that tells the actors what to do.
        """
        self._add_ship(cast)
        self._add_dialog(cast, HOW_TO_SHOOT)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        """Prepares the scene where the player can play the game.
        
            Args:
                cast: an object that holds all actors needed for the scene
                script: an object that tells the actors what to do.
        """
        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_SHIP_ACTION)
        script.add_action(INPUT, self.CONTROL_LASER_ACTION)
        script.add_action(INPUT, self.CONTROL_ASTEROIDS_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        """Prepares the game over screen when the player loses all lives.
        
            Args:
                cast: an object that holds all actors needed for the scene
                script: an object that tells the actors what to do.
        """
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
        """Adds a message to the center of the screen to inform the user.
        
            Args:
                cast: an object that holds all actors needed for the scene.
                message: a string that tells the message to be displayed in the scene.
        """
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_hits(self, cast):
        """Adds hits to the HUD to be diplayed.
        
            Args:
                cast: an object that holds all actors needed for the scene.
        """
        cast.clear_actors(HITS_GROUP)
        text = Text(HITS_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(HITS_GROUP, label)

    def _add_lives(self, cast):
        """Adds lives left to the HUD to be diplayed.
        
            Args:
                cast: an object that holds all actors needed for the scene.
        """
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        """Adds the accumulated score to the HUD to be diplayed.
        
            Args:
                cast: an object that holds all actors needed for the scene.
        """
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        """Adds the stats to the HUD to be diplayed.
        
            Args:
                cast: an object that holds all actors needed for the scene.
        """
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_ship(self, cast):
        """Adds the ship Actor object to the cast.
        
            Args:
                cast: an object that holds all actors needed for the scene.
        """
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
        """Adds the script to initalize actions in the script.

        Args:
            script: An oject that holds the game actions
        """
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        """Adds the script to load all the assets needed.

        Args:
            script: An oject that holds the game actions
        """
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        """Adds the script to draw the needed actors from the script to the screen.

        Args:
            script: An oject that holds the game actions
        """
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_LASER_ACTION)
        script.add_action(OUTPUT, self.DRAW_ASTEROID_ACTION)
        script.add_action(OUTPUT, self.DRAW_SHIP_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        """Adds the script to release all the devices that were used.

        Args:
            script: An oject that holds the game actions
        """
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        """Unloads the script

        Args:
            script: An oject that holds the game actions
        """
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        """Adds updates to the script.

        Args:
            script: An oject that holds the game actions
        """
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_LASER_ACTION)
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION)
        script.add_action(UPDATE, self.MOVE_ASTEROID_ACTION)
        script.add_action(UPDATE, self.COLLIDE_ASTEROIDS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_LASER_ACTION) # morgan added
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION)