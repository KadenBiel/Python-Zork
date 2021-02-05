import Library

class map:
    def __init__(self):
        libs = Library.lib()
        self.Game = libs.gameS
        self.Player = libs.player
        self.Room = libs.room
        self.Items = libs.items
        self.NPC = libs.npc
        self.Save = libs.save

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