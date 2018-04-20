import player, room, time, random

class Game:

    def __init__(self):    
        """
         constructor: create a Game object
        initialize your game in here
        """
        self.hw = room.Room('West of House', 'This is an open field west of a white house, with a boarded front door.', True)
        self.hn = room.Room('North of House', 'You are facing the north side of a white house.  There is no door here, and all the windows are barred.', True)
        self.he = room.Room('Behind House', 'You are behind the white house.')
        self.hs = room.Room('South of House', 'You are facing the south side of a white house.  There is no door here, and all the windows are barred.', True)
        self.k = room.Room('Kitchen', 'You are in the kitchen of the white house.  A table seems to have been used recently for the preparation of food.  A passage leads to the west and a dark staircase can be seen leading upward.', True)
        self.a = room.Room('Attic', 'This is the attic. The only exit is stairs that lead down.')
        self.lr = room.Room('Living Room', 'You are in the living room.  There is a door to the east, a wooden door with strange gothic lettering to the west, which appears to be nailed shut, and a large oriental rug in the center of the room.', True)
        self.f1 = room.Room('Forest', 'This is a forest, with trees in all directions around you.', True)
        self.fp = room.Room('Forest', 'This is a dimly lit forest, with large trees all around.  One particularly large tree with some low branches stands here.', True)
        self.t = room.Room('Up a Tree', 'You are about 10 feet above the ground nestled among some large branches.  The nearest branch above you is above your reach.', True)
        self.f2 = room.Room('Forest', 'This is a dimly lit forest, with large trees all around.  To the east, there appears to be sunlight.')
        self.c1 = room.Room('Clearing', 'You are in a clearing, there is a pile of leaves on the ground', True)
        self.f3 = room.Room('Forest', 'This is a large forest, with trees obstructing all views except to the east, where a small clearing may be seen through the trees.', True)
        self.f4 = room.Room('Forest', 'This is a dimly lit forest, with large trees all around.', True)
        self.c2 = room.Room('Clearing', 'You are in a clearing, with a forest surrounding you on the south and west.', True)
        self.cv = room.Room('Canyon View', 'You are at the top of the Great Canyon on its south wall. From here there is a marvelous view of the Canyon and parts of the Frigid River upstream. Across the canyon, the walls of the White Cliffs still appear to loom far above. Following the Canyon upstream (north and northwest), Aragian Falls may be seen, complete with rainbow. Fortunately, my vision is better than average and I can discern the top of the Flood Control Dam #3 far to the distant north. To the west and south can be seen an immense forest, stretching for miles around. It is possible to climb down the canyon from here.', True)
        self.rl = room.Room('Rocky Ledge', 'You are on a ledge about halfway up to wall of the river canyon. You can see from here that the main flow from Aragian Falls twist along a passage which it is impossible to enter. Below you is the canyon bottom. Above you is more cliff, which still appears climbable.', True)
        self.cb = room.Room('Canyon Bottom', 'You are beneath the walls of the river canyon which may be climbable here. There is a small stream here, which is the lesser part of the runoff of Aragain Falls. to the north is a narrow path', True)
        self.er = room.Room('End of Rainbow', 'You are on a small, rocky beach on the continuation of the Frigid River past the Falls. The beach is narrow due to the presence of the White Cliffs. The river canyon opens here and sunlight shines in from above. A rainbow crosses over the falls to the west and a narrow path continues to the south.', True)

        self.rooms = [self.hw, self.hn, self.he, self.hs, self.k, self.a, self.lr, self.f1, self.fp, self.t, self.f2, self.c1, self.f3, self.f4, self.c2, self.cv, self.rl, self.er]
        self.player = player.Player(self.hw)

        self.hw.connect_to(self.hn, 'n')
        self.hn.connect_to(self.hw, 'w')

        self.hw.connect_to(self.hs, 's')
        self.hs.connect_to(self.hw, 'w')

        self.hn.connect_to(self.he, 'e')
        self.he.connect_to(self.hn, 'n')

        self.hs.connect_to(self.he, 'e')
        self.he.connect_to(self.hs, 's')

        self.hw.connect_to(self.f1, 'w')

        self.f4.connect_to(self.f1, 'w')
        self.f1.connect_to(self.f4, 's')

        self.f1.connect_to(self.fp, 'e')
        self.fp.connect_to(self.f1, 'w')

        self.fp.connect_to(self.t, 'u')
        self.t.connect_to(self.fp, 'd')

        self.f1.connect_to(self.c1, 'n')
        self.c1.connect_to(self.fp, 'w')

        self.c1.connect_to(self.f2, 'e')
        self.f2.connect_to(self.c1, 'n')

        self.fp.connect_to(self.f2, 'e')
        self.f2.connect_to(self.fp, 'w')

        self.f2.connect_to(self.f3, 'e')
        self.f3.connect_to(self.f2, 'w')
        self.f3.connect_to(self.f2, 'n')
        self.f3.connect_to(self.f2, 's')

        self.f2.connect_to(self.c2, 's')
        self.c2.connect_to(self.f2, 'n')

        self.c2.connect_to(self.he, 'w')
        self.he.connect_to(self.c2, 'e')

        self.c2.connect_to(self.cv, 'e')
        self.cv.connect_to(self.c2, 'n')

        self.cv.connect_to(self.rl, 'd')
        self.rl.connect_to(self.cv, 'u')

        self.rl.connect_to(self.cb, 'd')
        self.cb.connect_to(self.rl, 'u')

        self.cb.connect_to(self.er, 'n')
        self.er.connect_to(self.cb, 's')

        self.cv.connect_to(self.f4, 'w')
        self.f4.connect_to(self.cv, 'e')

        self.f4.connect_to(self.hs, 'nw')
        self.hs.connect_to(self.f4, 's')

        self.k.connect_to(self.a, 'u')
        self.a.connect_to(self.k, 'd')

        self.k.connect_to(self.lr, 'w')
        self.lr.connect_to(self.k, 'e')
        
        self.hw.add_items({'mailbox':{'leaflet':'# Welcome to the unofficial python version of Zork I! There are many commands you can use,\n-go : takes one direction, allows you to move around the map (or you can just type the dirction first and not use go)\n-take : takes one item name, allows you to take items from the room and put them in your inventory\n-look : can take the name of an item but if no items are in the arguments it will print the rooms descirption\n-read : takes name of an item, allows you to read papers\n-open : takes name of container or door in the room, allows you to open contianers and doors\n-close : takes name of a contianer, allows you to close containers (closing doors has not yet been implemented)\nHope that you find this guide useful! have fun!'}})
        self.k.add_items({'sack':{'lunch':'Nothing special here', 'garlic':'Nothing special here'}})
        self.t.add_items({'egg':'Looks pretty sealed to me, you cannot open the egg'})
        self.he.add_door('window', 'w', 'e', self.k)

        print(self.player.location.name +':\n'+ self.player.location.desc)

    def print_rooms(self):
        """
        print function for debugging
        calls print for all rooms
        """
        for r in self.rooms:
            r.print_details()

    def move(self, c):
        if 'north' in c or 'n' in c:
            self.player.go('n')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'south' in c or 's' in c:
            self.player.go('s')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'east' in c or 'e' in c:
            self.player.go('e')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'west' in c or 'w' in c:
            self.player.go('w')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'northeast' in c or 'ne' in c:
            self.player.go('ne')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'northwest' in c or 'nw' in c:
            self.player.go('n')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'southwest' in c or 'sw' in c:
            self.player.go('sw')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'southeast' in c or 'se' in c:
            self.player.go('se')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'up' in c or 'u' in c:
            self.player.go('u')
            return self.player.location.name +':\n'+ self.player.location.desc
        elif 'down' in c or 'd' in c:
            self.player.go('d')
            return self.player.location.name +':\n'+ self.player.location.desc
        else:
            return 'Invalid Direction'

    def process_cmd(self, c):
        """
        process given command
        params is a list of arguments
        """
        for n, i in enumerate(c):
            c[n] = i.lower()
        c1 = c[0]

        direct = ['north', 'n', 'south', 's', 'east', 'e', 'west', 'w', 'northeast', 'ne', 'northwest', 'nw', 'southeast', 'se', 'southwest', 'sw', 'up', 'u', 'down', 'd']

        if c1 in direct:
            return self.move(c1) 

        if c1 == 'read':
            x = self.player.location.items
            y = self.player.items
            for i in c:
                if i in x:
                    d = x[i]
                    if "# " in d:
                        d.replace('# ', '')
                        return d
                elif i in y:
                    d = y[i]
                    if "# " in d:
                        d.replace('# ', '')
                        return d
            return "Sorry, the item could not be found."
                    
        if c1 == 'go':
            for i in c:
                if i in direct:
                    return self.move(i)
            return "Invalid direction"

        if c1 == 'look':
            if len(c) > 0:
                x = self.player.location.items
                y = self.player.items
                for i in c:
                    if i in x:
                        d = x[i]
                        if '# ' in d or type(d) == type(dict()):
                            return "There is nothing special about this "+i+'.'
                        else:
                            return d
                    elif i in y:
                        d = y[i]
                        if "# " in d or type(d) == type(dict()):
                            return "There is nothing special about this "+i+'.'
                        else:
                            return d
            return self.player.location.name +':\n'+ self.player.location.desc
        
        if c1 == 'take':
            x = self.player.location.items
            for i in c:
                if i in x:
                    if i == 'mailbox':
                        return 'Are you serious?'
                    self.player.take(i)
                    return 'Taken'
            return 'Could not find the item.'

        if c1 == 'open':
            x = self.player.location.items
            y = self.player.items
            z = self.player.location.door
            for i in c:
                if i in x:
                    d = x[i]
                    if type(d) == type(dict()):
                        if len(d) < 1:
                            return 'There is nothing in here.'
                        r = 'You see: '
                        p = []
                        for k, v in d.items():
                            r += k+', '
                            x.update({k:v})
                        return r
                if i in y:
                    d = y[i]
                    if type(d) == type(dict()):
                        if len(d) < 1:
                            return 'There is nothing in here.'
                        r = 'You see: '
                        p = []
                        for k, v in d.items():
                            r += k+', '
                            y.update({k:v})
                        return r
                if i in z:
                    self.player.location.connect_to(z[i][1], z[i][0])
                    z[i][1].connect_to(self.player.location, z[i][2])
                    return 'Opened'

        if c1 == 'close':
            x = self.player.location.items
            y = self.player.items
            for i in c:
                if i in x:
                    d = x[i]
                    if type(d) == type(dict()):
                        for k, v in d.items():
                            x.pop(k)
                        return 'Closed'
                if i in y:
                    d = y[i]
                    if type(d) == type(dict()):
                        for k, v in d.items():
                            y.pop(k)
                        return 'Closed'
            return 'Could not find any open contianers in this room.'
        return 'I beg your pardon?'

    def start(self):
        """
        start the input loop:
            1. get user input (command)
            2. split into tokens
            3. process the command
        """
        while True:
            rem = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '`', '~', "'", '"', '{', '}', '[', ']', '|', '/', '<', '>', '?', '.', ',', 'the', 'at', 'and', 'with', 'inside']
            IN = input('> ')
            IN = IN.lower()
            for x in rem:
                if x in IN:
                    IN.replace(x, '')
            c = IN.split(' ')
            print('')
            print(self.process_cmd(c))
            
    def win(self):
        print("congrats, you have won the game!")
        time.sleep(5)
        quit

if __name__ == '__main__':
    g = Game()
    g.start()
