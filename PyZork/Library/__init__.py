print("Inititializing object classes")
if Items.listed == None:
    print("Items: null")
else:
    print("Items: ready")

if NPC.listed == None:
    print("NPCs: null")
else:
    print("NPCs: ready")

if Rooms.listed == None:
    print("map: null")
else:
    print("map: ready")

print("Game status: ready")

class lib():
    def __init__(self):
        self.mod = [game.Game, Player.playLib, Rooms.roomLib, Items.itemLib, NPC.npcLib, Save.Saver, Handling.Handler]
        self.ver = "v1.3"
        self.currentMap = None

    def send(self, c):
        self.mod[6].IN(c)

    def getSaves(self):
        return self.mod[6].saves