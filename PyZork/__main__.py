from Library import Items as it
from Library import Rooms as ro
from Library import Player as pl
from Library import NPC as np
from Library import * as lib

try:
    """
    Try/except block to catch users running an outdated Python version
    """
    startScreen = input("PyZork v1.3\nHit enter to start\n")
except:
    print("Your version of python is not compatible with this program, please use the lastest Python 3 version")
    end = raw_input("Hit enter to quit")
    quit()

class Handler:

    def __init__(self):    
        """
        Creates a Handler object to talk to the Library
        """

    def process_cmd(self, c):
        """
        process given command
        Turns command into list of arguments and sends to the library
        """