from Library import lib

class Handler(object):
    """
    Input and output handler for main
    """
    def __init__(self):
        self.name = "Handle"
        self.desc = "Main Input and Output handler for PyZork library"
        self.id = 6
        tree = lib.mod
        self.game = tree[0]
        self.player = tree[1]
        self.rooms = tree[2]
        self.items = tree[3]
        self.npc = tree[4]
        self.save = tree[5]
        self.ver = lib.ver

    def IN(self, cmd):
        """
        Takes string "cmd" and splits it up by spaces then sends it to the Game and returns the output
        """
        cmd = cmd.lower()
        playIN = cmd.split(' ')
        return self.game.cmd(playIN)