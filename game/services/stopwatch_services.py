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
        seconds = check_time.current
        time.sleep(1)
        seconds =+ 1
        return seconds

start_time = Stopwatch_services()
start_time
# Starts the timer, this needs to be placed within the main program
    
check_time = Stopwatch_services()
while True:
    start_time.current += check_time.add_second
    print(check_time.current)
# This adds a second to the timer.
