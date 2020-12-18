class Room:

    
    def __init__(self, n="", d="", l=False, iden = 000, save = False):
        """
        constructor: create a new Room object
        """
        self.name = n #room name
        self.desc1 = d #room description(not changeable)
        self.desc = d #room description (changeable)
        self.door = {} #dictionary contining the names of "connecting" rooms that require special action to get through
        self.doors = {} #ditionary with connecting rooms and their directions
        self.openDoors = [] #A list of all the connections with other rooms
        self.items = {} #dictionary with items in the room and thier descriptions
        self.play = [] #list of player objects in the room
        self.lit = l #boolean if the room is lit without lamp
        self.save = save
        self.id = iden

    def name(self):
        return self.name #returns room name

    def connect_to(self, other, direction):
        """
        connect this room to another
        """
        if other.id in self.openDoors:
            return
        self.doors.update({direction:other}) #Adds room to dictionary or surrounding rooms
        connect = {other:direction} #Creates a dictionary contianing the connecting room and the direction
        self.openDoors.append(connect) #Adds the connection dictionary to the list or connections

    def add_items(self, item):
        """
        add items to the room
        param: item is a dictionary with
            name / description pairs
        """
        i = ' You see: ' #defines string for list of items in the room
        for k, v in item.items():
            i += k+', ' #adds each item name to the string 
        self.desc += i #adds string to room description
        self.items.update(item) #adds item name and description to the room dictionary

    def add_door(self, name, d, od, door):
        self.door.update({name:[d, door, od]}) #adds doors to the room
        self.desc += ' '+name+' (can be opened), ' #adds door name to room description

    def print_details(self):
        """
        verbose print for debugging
            prints the room's description
            prints connections & items
        """
        s = self.name #defines string with room name
        s += '\n' #adds a break to string
        s += self.desc #adds description
        s += '\n' #adds a break
        for d, r in self.doors.items():
            #Defines directions:
            if d == 'n':
                di = 'North' 
            if d == 's':
                di = 'South'
            if d == 'e':
                di = 'East'
            if d == 'w':
                di = 'West'
            if d == 'u':
                di = 'Above'
            if d == 'd':
                di = 'Below'
            s += 'To the '+di+' You see: '+r.name+', ' #adds room name and direction
        if len(self.doors) > 0 and len(self.items) > 0:
            s += '\n' #adds a break
        for i, d in self.items.items():
            s += str(i)+', '#adds item names
        return s
