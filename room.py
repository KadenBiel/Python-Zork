class Room:

    def __init__(self, n, d="", l=False):
        """
        constructor: create a new Room object
        """
        self.name = n #room name
        self.desc = d #room description
        self.door = {} #dictionary contining the names of "connecting" rooms that require special action to get through
        self.doors = {} #ditionary with connecting rooms and their directions
        self.items = {} #dictionary with items in the room and thier descriptions
        self.play = [] #list of player objects in the room
        self.lit = l #boolean if the room is lit without lamp

    def name(self):
        return self.name

    def connect_to(self, other, direction):
        """
        connect this room to another
        """
        self.doors.update({direction:other})

    def add_items(self, item):
        """
        add items to the room
        param: item is a dictionary with
            name / description pairs
        """
        i = ' You see: '
        for k, v in item.items():
            i += k+', '
        self.desc += i
        self.items.update(item)

    def add_door(self, name, d, od, door):
        self.door.update({name:[d, door, od]})
        self.desc += ' '+name+' (can be opened), '

    def print_details(self):
        """
        verbose print for debugging
            prints the room's description
            prints connections & items
        """
        s = self.name
        s += '\n'
        s += self.desc
        s += '\n'
        for d, r in self.doors.items():
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
            s += 'To the '+di+' You see: '+r.name+', '
        if len(self.doors) > 0 and len(self.items) > 0:
            s += '\n'
        for i, d in self.items.items():
            s += str(i)+', '
        return s
