import Library

class playLib(object):
    """The player"""
    def __init__(self):
        tree = Library.lib.mod
        self.rooms = tree[2]
        self.items = tree[3]
        self.npc = tree[4]
        self.save = tree[5]
        self.ver = Library.lib.ver
