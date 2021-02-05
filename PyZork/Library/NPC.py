import Library

class npcLib(object):
    """NPC object class"""
    def __init__(self):
        self.nList = []
        tree = Library.lib.mod
        self.rooms = tree[2]
        self.items = tree[3]
        self.npc = tree[4]
        self.save = tree[5]
        self.ver = Library.lib.ver

    def listed(self):
        return self.iList