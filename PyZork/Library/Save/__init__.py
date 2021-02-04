from Library import lib

class save(object):
    """
    Creates, stores and opens game saves
    """
    def __init__(self):
        tree = lib.mod
        self.player = tree[1].playLib
        self.items = tree[3].itemLib
        self.npc = tree[4].npcLib
        self.save = tree[5].saveLib
        self.ver = lib.ver


