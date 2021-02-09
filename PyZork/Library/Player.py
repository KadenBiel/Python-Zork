class playLib(object):

    def __init__(self):
        self.desc = "Object for handling interations with the player"

class Player:

    def __init__(self, location=None, items={}, n=None):
        """
        new Player constructor
            location and items are OPTIONAL parameters
            The values in the param list are DEFAULT values
        """
        self.location = location #defines starting laction for the player
        self.items = items #defines staring items for the player
        self.health = 100 #defines starting health for player
        self.com = NPC #defines if player object is an NPC or not
        self.name = n #defines player name
        self.death = False #boolean to check if object is dead

    def go(self, direction):
        """
        go in a direction
        """
        room = self.location #defines room you are in
        direct = list(room.doors) #gets the list of directions you can move
        if direction in direct:
            self.location = room.doors[direction] #puts player object in room if they can move there
            if self.com == True:
                self.location.play.append(room.play.pop(self)) #if player object is and NPC this will upadte the room list or NPC's
            return True
        else:
            return False

    def look(self, item=None):
        """
        look around, or look at an item
        """
        room = self.location #gets room you are in
        if item != None:
            try:
                return(item+room.items[item]) #gets item description and item name then returns it to the processer
            except:
                return 'item "'+item+'" not found' #returns item name if item wasnt in the room
        else:
            return room.print_details() #returns the rooms description if items were not listed

    def take(self, item):
        """
        take an item
        """
        if len(self.items) == 8:
            #Stop code if you've maxed out on items
            return
        if item in self.location.items:
            #Takes item out of the room dictionary and places it in the player's dictionary
            self.items.update({item:self.location.items.pop(item)})
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
            d = self.items[item] #gets item description
            self.items.pop(item) #removes item from player
            self.location.items.update({item:d}) #places item  in room

    def kill(self, npc, dam):
        """
        lose health
        """
        if dam > 0:
            npc.health -= dam #subtracts health from player you are fighting and vice versa (NPC's are a bit glitchy right now and cannot be implemented just yet)
            if npc.health <= 0:
                npc.dead() #"kills" the npc or player
                return 'Killed'
            return 'Hit'
        else:
            return 'Missed'
    def dead(self):
        """
        die
        """
        self.death = True #updates death boolean
        rem = self.items
        for x, y in rem.items():
            self.location.items.update({x:self.items[x]}) #removes items and places them in the room
        self.items = {}
        if self.com:
            self.location.play.remove(self)

