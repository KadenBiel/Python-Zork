from Library import game, Handling, Items, maps, NPC, Player, Rooms
print("Inititializing object classes")
if Items.itemLib.listed == []:
    print("Items: null")
else:
    print("Items: ready")

if NPC.npcLib.listed == []:
    print("NPCs: null")
else:
    print("NPCs: ready")

if Rooms.roomLib.listed == []:
    print("map: null")
else:
    print("map: ready")

print("Game status: ready")

class lib():
    def __init__(self):
        self.mod = [game.Game, Player.playLib, Rooms.roomLib, Items.itemLib, NPC.npcLib, None, Handling.Handler, maps.map]
        self.ver = "v1.3"
        self.currentMap = None

    def send(self, c):
        self.mod[6].IN(c)