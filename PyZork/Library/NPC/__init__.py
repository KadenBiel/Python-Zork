class NPC(object):
    """NPC object class"""
    def __init__(self, *args, **kwargs):
        self.name = *args[0]
        self.desc = *args[1]
        self.loc = **kwargs[0]
        self.playerID = **kwargs[1]
        return self.name + " - Finish init"