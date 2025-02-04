import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.stopwatch_services import Stopwatch_services

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the cycle collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        scores = cast.get_actors("scores")
        score1 = scores[0]
        score2 = scores[1]
        
        # food = cast.get_first_actor("foods")
        cycles = cast.get_actors("cycle")
        for cycle in cycles:
            points = 0
            length = 1
            cycle.grow_tail(length)
            score1.add_points(points)
            score2.add_points(points)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycles = cast.get_actors("cycle")
        for i in range(len(cycles)):
            head = cycles[i].get_segments()[0]
            segments = cycles[i].get_segments()[1:]
            
            for segment in segments:
                if head.get_position().equals(segment.get_position()):
                    self._is_game_over = True
                elif cycles[0].get_segments()[0].get_position().equals(segment.get_position()):
                    self._is_game_over = True
                elif cycles[1].get_segments()[0].get_position().equals(segment.get_position()):
                    self._is_game_over = True
                    
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle = cast.get_first_actor("cycle")
            segments = cycle.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
            cycles = cast.get_actors("cycle")
            for cycle in cycles:
                segments = cycle.get_segments()
                for segment in segments:
                    segment.set_color(constants.WHITE)
            # food.set_color(constants.WHITE)