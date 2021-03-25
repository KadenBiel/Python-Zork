class npcLib(object):
    """NPC object class"""
    def __init__(self):
        self.nList = []

    def listed(self):
        return self.iList

class Player:

    def __init__(self, location=None, items=[], right=None, left=None, n=None):
        """
        new NPC constructor
        params:
            location: object, the starting room object of the player
            items: list, list of the item objects the player starts with
            right: object, item object the player starts out holding in their right hand (dominant)
            left: object, item object the player starts out holding in their left hand (non-dominant)
            n: string, name of the player (input by the user)
        """
        self.location = location #If location is None, the player will start in a random room
        self.items = items
        self.health = 100 #Players hp
        self.name = n
        self.death = False #boolean for if the player dies
        self.right = right
        self.left = left

    def go(self, direction):
        """
        go in a direction
        params:
            direction: string, direction the NPC needs to move ('n', 'e', 's', 'w', 'u' or 'd')
        """
        room = self.location
        direct = list(room.doors)
        if direction in direct:
            self.location = room.doors[direction]
            if self.com == True:
                self.location.play.append(room.play.pop(self))
            return True
        else:
            return False
    
    def drop(self, item):
        """
        drop an item
        """
        #takes item out of player dictionary and places it in the room
        if item in self.items:
            self.items.remove(item)
            self.location.items.append(item)

    def attack(self, opp):
        """
        Attack a player, returns ammont of damage dealt
        note: By default, an NPC will attack with whatever is in their right hand
        param:
            opp: object, opponent to the NPC
        """
        if self.right == None:
            return 10
        else:
            return self.right.attack

    def kill(self, opp, dam):
        """
        lose health
        param:
            opp: object, opponent to the NPC
            dam: interger, damage the player dealt
        """
        if dam > 0:
            opp.health -= dam
            if opp.health <= 0:
                opp.dead()
                return 'Killed'
            return 'Hit'
        else:
            return 'Missed'

    def dead(self):
        """
        die
        """
        self.death = True
        rem = self.items
        for x, y in rem.items():
            self.location.items.update({x:self.items[x]})
        self.items = {}