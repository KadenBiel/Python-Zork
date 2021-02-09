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
        self.hw = self.room.create('West of House', 'This is an open field west of a white house, with a boarded front door.')
        self.hn = self.room.create('North of House', 'You are facing the north side of a white house.  There is no door here, and all the windows are barred.')
        self.he = self.room.create('Behind House', 'You are behind the white house.')
        self.hs = self.room.create('South of House', 'You are facing the south side of a white house.  There is no door here, and all the windows are barred.')
        self.k = self.room.create('Kitchen', 'You are in the kitchen of the white house. A table seems to have been used recently for the preparation of food. A passage leads to the west and a dark staircase can be seen leading upward.')
        self.a = self.room.create('Attic', 'This is the attic. The only exit is stairs that lead down.')
        self.lr = self.room.create('Living Room', 'You are in the living room.  There is a door to the east, a wooden door with strange gothic lettering to the west, which appears to be nailed shut, and a large oriental rug in the center of the room.')
        self.f1 = self.room.create('Forest', 'This is a forest, with trees in all directions around you.')
        self.fp = self.room.create('Forest', 'This is a dimly lit forest, with large trees all around.  One particularly large tree with some low branches stands here.')
        self.t = self.room.create('Up a Tree', 'You are about 10 feet above the ground nestled among some large branches.  The nearest branch above you is above your reach.')
        self.f2 = self.room.create('Forest', 'This is a dimly lit forest, with large trees all around.  To the east, there appears to be sunlight.')
        self.c1 = self.room.create('Clearing', 'You are in a clearing, there is a pile of leaves on the ground')
        self.f3 = self.room.create('Forest', 'This is a large forest, with trees obstructing all views except to the east, where a small clearing may be seen through the trees.')
        self.f4 = self.room.create('Forest', 'This is a dimly lit forest, with large trees all around.')
        self.c2 = self.room.create('Clearing', 'You are in a clearing, with a forest surrounding you on the south and west.')
        self.cv = self.room.create('Canyon View', 'You are at the top of the Great Canyon on its south wall. From here there is a marvelous view of the Canyon and parts of the Frigid River upstream. Across the canyon, the walls of the White Cliffs still appear to loom far above. Following the Canyon upstream (north and northwest), Aragian Falls may be seen, complete with rainbow. Fortunately, my vision is better than average and I can discern the top of the Flood Control Dam #3 far to the distant north. To the west and south can be seen an immense forest, stretching for miles around. It is possible to climb down the canyon from here.')
        self.rl = self.room.create('Rocky Ledge', 'You are on a ledge about halfway up to wall of the river canyon. You can see from here that the main flow from Aragian Falls twist along a passage which it is impossible to enter. Below you is the canyon bottom. Above you is more cliff, which still appears climbable.')
        self.cb = self.room.create('Canyon Bottom', 'You are beneath the walls of the river canyon which may be climbable here. There is a small stream here, which is the lesser part of the runoff of Aragain Falls. to the north is a narrow path')
        self.er = self.room.create('End of Rainbow', 'You are on a small, rocky beach on the continuation of the Frigid River past the Falls. The beach is narrow due to the presence of the White Cliffs. The river canyon opens here and sunlight shines in from above. A rainbow crosses over the falls to the west and a narrow path continues to the south.')
        self.c = self.room.create('Cellar', 'You are in a dark and damp cellar with a narrow passageway leading east, and a crawlway to the south.  On the west is the bottom of a steep metal ramp which is unclimbable. (The rest off the dungeon is still a work in progress, sorry for the inconvenice!)', False)

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