import time

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
        seconds = self.current
        time.sleep(1)
        seconds =+ 1
        return seconds


        
