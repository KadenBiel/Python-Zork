class playLib(object):

    def __init__(self):
        self.desc = "Object for handling interations with the player"

class Player:

    def __init__(self, location=None, items=[], right=None, left=None, n=None):
        """
        new Player constructor
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
            direction: string, direction the player wants to move ('n', 'e', 's', 'w', 'u' or 'd')
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

    def look(self, item=None):
        """
        look around, or look at an item
        params:
            item: string, name of the item
        """
        room = self.location
        if item != None:
            try:
                return item+room.items[item]
            except:
                return 'item "'+item+'" not found'
        else:
            return room.print_details()

    def take(self, item):
        """
        take an item
        param:
            item: string, name of the item
        """
        if len(self.items) == 8:
            return None
        if item in self.location.items:
            #Takes item out of the room dictionary and places it in the player's dictionary
            self.items.append(self.location.items.pop(item))
        for k, v in self.location.items.items():
            #checks if item is in a container and pulls it out
            if type(v) == type(dict()):
                for l, w in v.items():
                    if l == item:
                        v.pop(l)
                        break
    
    def drop(self, item):
        """
        drop an item
        """
        #takes item out of player dictionary and places it in the room
        if item in self.items:
            d = self.items[item]
            self.items.pop(item)
            self.location.items.update({item:d})

    def in_hand(self, item, rl):
        """
        place an item in the player's hand
        params:
            item: object, the object to place in hand
            rl: string, right or left hand ('r', 'l')
        """
        if rl == 'r':
            self.right = item
        elif rl == 'l':
            self.left = item
        else:
            return 'Invalid hand'

    def kill(self, npc, dam):
        """
        lose health
        param:
            npc: object, npc player is fighting
            dam: interger, damage the player dealt
        """
        if dam > 0:
            npc.health -= dam
            if npc.health <= 0:
                npc.dead()
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

