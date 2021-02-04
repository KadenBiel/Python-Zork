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
        self.mod = [game, Player, Rooms, Items, NPC, Save, Handling]
        self.ver = "v1.3"