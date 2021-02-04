from Library import lib

class Items(object):
    """Items indentifier"""
    def __init__(self):
        tree = lib.mod
        self.rooms = tree[2].roomLib
        self.items = tree[3].itemLib
        self.npc = tree[4].npcLib
        self.save = tree[5].saveLib
        self.ver = lib.ver


