import time

class Stopwatch_services():
    def __init__(self):
        self.start = 0

    @property
    def add_second(self):
        seconds = check_time.start
        time.sleep(1)
        seconds =+ 1
        return seconds

check_time = Stopwatch_services()

def return_value():
    runner = True
    while runner == True:
        print(check_time.start)
        check_time.start += check_time.add_second

print(return_value())