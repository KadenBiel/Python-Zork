from Library import lib

class Handle(object):
    """
    Input and output handler for main
    """
    def __init__(self):
        self.name = "Handle"
        self.desc = "Main Input and Output handler for PyZork library"
        self.id = 5
        self.ver = lib.ver
        self.tree = lib.mod

    def IN(self, cmd):
        """
        Takes string "cmd" and splits it up by spaces to 
        """
        cmd = cmd.lower()
        playIN = cmd.split(' ')
        self.tree[0].cmd(playIN)