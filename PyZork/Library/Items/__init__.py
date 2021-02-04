from Library import lib

class itemLib(object):
    """Items indentifier"""
    def __init__(self):
        tree = lib.mod
        self.rooms = tree[2]
        self.items = tree[3]
        self.npc = tree[4]
        self.save = tree[5]
        self.ver = lib.ver


