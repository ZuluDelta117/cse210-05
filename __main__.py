import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.stopwatch_services import Stopwatch_services
from game.shared.color import Color
from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cycle", Cycle(constants.RED))
    cast.add_actor("cycle", Cycle(constants.GREEN))
    cast.add_actor("scores", Score())
    cast.add_actor("scores", Score())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    start_time = Stopwatch_services()
    

    

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    # I was trying to get calling the time to work both here adn in the handle_collisions_action.py
    # file, but I was unable to get it to call it as an int. (Zack D.)

    # HandleCollisionsAction = HandleCollisionsAction()
    
    # start_time
    # Starts the timer, this needs to be placed within the main program
            
    # check_time = start_time

    # HandleCollisionsAction._handle_food_collision(cast, check_time)

    # while True:
    #     start_time.current += check_time.add_second
    #     print(check_time.current)
    # This adds a second to the timer.

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()