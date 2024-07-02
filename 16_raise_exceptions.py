# Raise exceptions:
# standard exceptions
# user defined exceptions

# Standard exceptions
try:
    raise MemoryError('memory error')
except MemoryError as e:
    print(e)

# The above exceptions can also be written as, but above is recommended

try:
    raise Exception('memory error')
except Exception as e:
    print(e)

# User defined exceptions

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print(f"user defined exception: {self.msg}")

try:
    raise Accident ('Crash occur between 2 cars')
except Accident as e:
    e.print_exception()

    # OR

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print(f"accident occured take detour {self.msg}")

try:
    raise Accident ('Crash occur between 2 cars')
except Accident as e:
    e.handle()
