import time
current = 0

class Stopwatch_services():
    """
    Provides a way to keep track of time during the game
    """
    def __init__(self):
        self.current = 0

    @property
    def add_second(self):
        """
        Adds a second to self.current

        Args:
        None
        """
        seconds = current
        time.sleep(1)
        seconds =+ 1
        return seconds

start_time = Stopwatch_services()
start_time
# Starts the timer, this needs to be placed within the main program
class management():
    def time_management(current):
        check_time = start_time
        while True:
            current += check_time.add_second
            return current
        # This adds a second to the timer.
