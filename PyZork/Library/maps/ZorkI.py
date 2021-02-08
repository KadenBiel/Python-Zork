class map:
    def __init__(self, p=None, r=None, i=None, n=None):
        self.player = p
        self.room = r
        self.items = i
        self.npc = n
        self.name = "Zork I"

    def makeRooms(self):
        """
        Make the rooms
        """

    def createItems(self):
        """
        Create the items
        """

    def createNpc(self):
        """
        Create NPC's
        """

    def createPlayer(self):
        """
        Create player object
        """

    def setup(self):
        """
        Setup the map
        """
        self.makeRooms()
        self.createItems()
        self.createNpc()
        self.createPlayer()

if __name__ == "__main__":
    init = map()
    init.setup()