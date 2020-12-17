
from Library import Items as it
from Library import Rooms as ro
from Library import Player as pl
from Library import NPC as np

try:
    startScreen = input("PyZork v1.3\nHit enter to start\n")
except:
    print("Your version of python is not compatible with this program, please use Python 3 or up")
    end = raw_input("Hit enter to quit")
    quit()

class Game:

    def __init__(self):    
        """
        Creates a Game object and initializes the game
        """

    def process_cmd(self, c):
        """
        process given command
        params is a list of arguments
        """

if __name__ == '__main__':
    g = Game()
    g.start()