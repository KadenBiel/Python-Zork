import Library

class Handler(object):
    """
    Input and output handler for main
    """
    def __init__(self):
        self.name = "Handle"
        self.desc = "Main Input and Output handler for PyZork library"
        self.id = 6
        tree = Library.lib.mod
        self.game = tree[0]
        self.ver = Library.lib.ver

    def IN(self, cmd):
        """
        Takes string "cmd" and splits it up by spaces then sends it to the Game and returns the output
        """
        cmd = cmd.lower()
        playIN = cmd.split(' ')
        return self.game.cmd(playIN)