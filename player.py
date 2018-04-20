import room


class Player:

    def __init__(self, location=None, items={}):
        """
        new Player constructor
            location and items are OPTIONAL parameters
            The values in the param list are DEFAULT values
        """
        self.location = location
        self.items = items
        self.health = 100
    
    def __str__(self):
        """
        get string representation of Player
        """
        return ''

    def go(self, direction):
        """
        go in a direction
        """
        room = self.location
        direct = list(room.doors)
        if direction in direct:
            self.location = room.doors[direction]
            return True
        else:
            return False

    def look(self, item=None):
        """
        look around, or look at an item
        """
        #mrk - typo? self.location
        room = self.location
        if item != None:
            try:
                return(item+room.items[item])
            except:
                return 'item "'+item+'" not found'
        else:
            return room.print_details()

    def take(self, item):
        """
        take an item
        """
        if item in self.location.items:
            self.items.update({item:self.location.items.pop(item)})
        for k, v in self.location.items.items():
            if type(v) == type(dict()):
                for l, w in v.items():
                    if l == item:
                        v.pop(l)
                        break
    
    def drop(self, item):
        """
        drop an item
        """
        if item in self.items:
            d = self.items[item]
            self.items.pop(item)
            self.location.items.update({item:d})

    def kill(self, npc, dam):
        """
        lose health
        """
        if dam > 0:
            npc.health -= dam
            if npc.health < 0:
                npc.dead()
                return 'You killed him!'
            return 'Hit!'
        else:
            return 'Miss!'
    def dead(self):
        """
        die
        """
        for x, y in self.items.items():
            self.location.items.update(self.items.pop(x))
