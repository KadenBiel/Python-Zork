from Library import lib as game

try:
    """
    Try/except block to catch users running an outdated Python version
    """
    startScreen = input("PyZork v1.3\nHit enter to start\n")
except:
    print("Your version of python is not compatible with this program, please use the lastest Python 3 version")
    end = raw_input("Hit enter to quit")
    quit()

class Game:

    def __init__(self):    
        """
        Creates a Game object to talk to the Library
        """
        self.cmd = [] #list of previous commands a player has entered and the response given
        self.maxCMD = 5 #var for the max number of previous commands shown

    def gameState(self):
        """
        Talks with the library and shows information to the player
        """
        usrIn = input(game.getSaves())
        cmd = game.initData()
        while True:
            #Functioning game loop
            rCMD = self.cmd.reverse()
            x = 0
            for i in rCMD:
                #prints previous commands and responses
                x += 1
                print(i)
                if x == maxCMD:
                    break

            usrIn = input("\n> ")
            resp = game.send(usrIn)
            print(resp)
            self.cmd.append("\n> "+usrIn+"\n"+resp)