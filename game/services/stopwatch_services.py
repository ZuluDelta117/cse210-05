import time

class Stopwatch_services():
    def __init__(self):
        self.current = 0

    @property
    def add_second(self):
        seconds = check_time.current
        time.sleep(1)
        seconds =+ 1
        return seconds

check_time = Stopwatch_services()

def return_value():
    runner = True
    while runner == True:
        check_time.current += check_time.add_second
