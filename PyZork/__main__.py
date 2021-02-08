import Library, time

try:
    """
    Try/except block to catch users running an outdated Python version
    """
    input("PyZork "+Library.lib().ver+"\nHit enter to start\n")
except EOFError:
    print("Your version of python is not compatible with this program, please use the lastest Python 3 version.")
    raw_input("Hit enter to quit")
    quit()

class Game:

    def __init__(self):    
        """
        Creates a Game object to talk to the Library
        """
        self.cmd = [] #list of previous commands a player has entered and the response given
        self.maxCMD = 5 #var for the max number of previous commands shown
        self.init = Library.mapLib()
        self.gameState = Library.lib()
        

    def start(self):
        """
        Talks with the library and shows information to the player
        """
        while True:
            #Functioning game loop
            rCMD = self.cmd.reverse()
            x = 0
            try:
                for i in rCMD:
                    #prints previous commands and responses
                    x += 1
                    print(i)
                    if x == maxCMD:
                        break
            except TypeError:
                print("rCMD empty")

            usrIn = input("\n> ")
            resp = self.gameState.send(usrIn)
            print(resp)
            self.cmd.append("\n> "+usrIn+"\n"+resp)

if __name__ == "__main__":
    g = Game()
    g.start()