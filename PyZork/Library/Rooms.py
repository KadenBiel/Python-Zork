class roomLib:
    def __init__(self):
        """
        this class is called to create, manage, connect and save room objects
        """
        self.rList = []

    def create(self, name, desc, lit=True):
        """
        create a new room, returns the created room object
        param:
            name: string, name of the room
            desc: string, description of the room,
            lit: boolean, defines if the room is already lit or needs a light source to be seen
        """
        iden = len(self.rList)
        newRoom = room(n=name, id=iden, d=desc, l=lit)
        self.rList.append(newRoom)
        return newRoom

    def connect(self, r1, r2, d, od):
        """
        connect two rooms, note: don't use connect() if you want to add an interactive door. Use room.add_door() instead
        params:
            r1: object, first room object
            r2: object, second room object
            d: string, direction of r1 to r2 ('n', 'e', 's', 'w', 'u' or 'd')
            od: string, direction of r2 to r1 ('n', 'e', 's', 'w', 'u' or 'd')
        """
        r1.connect_to(r2, d)
        r2.connect_to(r1, od)

    def getSave(self):
        """
        reutrns a string of information to be saved in the save file
        """
        cList = []
        for room in self.rList:
            if room.change:
                cList.append(room)
        try:
            rStr = ''
            for room in cList:
                rStr += '$ROOM$ '
                rStr += str(room.id)
                if len(room.items) > 0:
                    rStr += ' ^* '
                    for item in room.items:
                        rStr += str(item.id) + ' '
                    rStr += '*^ '
                if len(room.doors) > 0:
                    rStr += '%* '
                    for door in room.doors:
                        rStr += door.name +' '+ door.connector +' '+ door.direct1 +' '+ door.direct2
                        if door.hidden:
                            rStr += ' ' + 't'
                        else:
                            rStr += ' ' + 'f'
                        if door.opened:
                            rStr += ' ' + 't'
                        else:
                            rStr += ' ' + 'f'
                    rStr += ' *%'
                if room != cList[-1]:
                    rStr += '\n'
            return rStr
        except TypeError:
            return 'None'

class room(object):
    def __init__(self, n='', id=None, d='', l=False, i=[]):
        """
        create new room object
        param:
            n: string, name of the new room (i.e. West of House)
            id: interger, unique id for each room (defined by the position in the list of rooms)
            d: string, description for the room
            l: boolean, defines if the room is pre-lit or needs an external light (like a lamp the player is holding)
            i: list, list of item objects contained in the room
        """
        self.name = n
        self.id = id
        self.desc = d
        self.lit = l
        self.door = []
        self.connection = {}
        self.openDoors = []
        self.items = i
        self.change = False

    def name(self):
        return self.name

    def connect_to(self, other, direction):
        """
        connect this room to another
        param:
            other: object, the other room
            direction: string, the direction of the other room ('n', 'e', 's', 'w', 'u' or 'd')
        """
        if other.id in self.openDoors:
            return None
        self.doors.update({direction:other}) #Adds room to dictionary or surrounding rooms
        connect = {other:direction} #Creates a dictionary contianing the connecting room and the direction
        self.openDoors.append(connect) #Adds the connection dictionary to the list or connections

    def add_items(self, item):
        """
        add items to the room
        param: item is a dictionary with
            name / description pairs
        """
        self.items.append(item)

    def add_door(self, name, d, od, room, op=False, h=False):
        """
        add interactive doors to the room
        param:
            name: string, name of your door (i.e. 'Window')
            d: string, direction from the room of origin ('n', 'e', 's', 'w', 'u' or 'd')
            od: string, direction back to the room of origin ('n', 'e', 's', 'w', 'u' or 'd')
            room: object, the other room connected to the door
            op: boolean, defines if the door is already opened (defaults to false)
            h: boolean, defines is the door is hidden or not (defaults to false)
        """
        newDoor = door(name, d, od, self, room, op, h)
        self.door.append(newDoor)
        room.door.append(newDoor)

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

class door:
    def __init__(self, n, d, od, r1, r2, op, h):
        """
        creates new door object
        param:
            see room.add_door for more details
        """
        self.name = n
        self.origin = r1
        self.connector = r2
        self.direct1 = d
        self.direct2 = od
        self.opened = op
        self.hidden = h

    def open(self):
        """
        opens and closes the door
        """
        self.opened = not self.opened
        self.origin.change = True