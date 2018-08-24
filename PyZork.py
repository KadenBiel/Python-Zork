import player, room, time, random

try:
    startScreen = input("PyZork v1.3\nHit enter to start\n")
except:
    print("Your version of python is not compatible with this program, please use Python 3 or up")
    end = raw_input("Hit enter to quit")
    quit()

try:
    readSave = open('save.pzk', 'r')
    readSave.close()
except:
    createSave = open('save.pzk', 'w')
    createSave.close()

class Game:

    def __init__(self):    
        """
         constructor: create a Game object
        initialize your game in here
        """
 
        self.hw = room.Room('West of House', 'This is an open field west of a white house, with a boarded front door.', True, '001', False)
        self.hn = room.Room('North of House', 'You are facing the north side of a white house.  There is no door here, and all the windows are barred.', True, '010', False)
        self.he = room.Room('Behind House', 'You are behind the white house.', True, '100', False)
        self.hs = room.Room('South of House', 'You are facing the south side of a white house.  There is no door here, and all the windows are barred.', True, '002', False)
        self.k = room.Room('Kitchen', 'You are in the kitchen of the white house.  A table seems to have been used recently for the preparation of food.  A passage leads to the west and a dark staircase can be seen leading upward.', True, '020', False)
        self.a = room.Room('Attic', 'This is the attic. The only exit is stairs that lead down.', iden = '200', save = False)
        self.lr = room.Room('Living Room', 'You are in the living room.  There is a door to the east, a wooden door with strange gothic lettering to the west, which appears to be nailed shut, and a large oriental rug in the center of the room.', True, '003', False)
        self.f1 = room.Room('Forest', 'This is a forest, with trees in all directions around you.', True, '030', False)
        self.fp = room.Room('Forest', 'This is a dimly lit forest, with large trees all around.  One particularly large tree with some low branches stands here.', True, '300', False)
        self.t = room.Room('Up a Tree', 'You are about 10 feet above the ground nestled among some large branches.  The nearest branch above you is above your reach.', True, '004', False)
        self.f2 = room.Room('Forest', 'This is a dimly lit forest, with large trees all around.  To the east, there appears to be sunlight.', True, '040',False)
        self.c1 = room.Room('Clearing', 'You are in a clearing, there is a pile of leaves on the ground', True, '400', False)
        self.f3 = room.Room('Forest', 'This is a large forest, with trees obstructing all views except to the east, where a small clearing may be seen through the trees.', True, '005', False)
        self.f4 = room.Room('Forest', 'This is a dimly lit forest, with large trees all around.', True, '050', False)
        self.c2 = room.Room('Clearing', 'You are in a clearing, with a forest surrounding you on the south and west.', True, '500', False)
        self.cv = room.Room('Canyon View', 'You are at the top of the Great Canyon on its south wall. From here there is a marvelous view of the Canyon and parts of the Frigid River upstream. Across the canyon, the walls of the White Cliffs still appear to loom far above. Following the Canyon upstream (north and northwest), Aragian Falls may be seen, complete with rainbow. Fortunately, my vision is better than average and I can discern the top of the Flood Control Dam #3 far to the distant north. To the west and south can be seen an immense forest, stretching for miles around. It is possible to climb down the canyon from here.', True, '006', False)
        self.rl = room.Room('Rocky Ledge', 'You are on a ledge about halfway up to wall of the river canyon. You can see from here that the main flow from Aragian Falls twist along a passage which it is impossible to enter. Below you is the canyon bottom. Above you is more cliff, which still appears climbable.', True, '060', False)
        self.cb = room.Room('Canyon Bottom', 'You are beneath the walls of the river canyon which may be climbable here. There is a small stream here, which is the lesser part of the runoff of Aragain Falls. to the north is a narrow path', True, '600', False)
        self.er = room.Room('End of Rainbow', 'You are on a small, rocky beach on the continuation of the Frigid River past the Falls. The beach is narrow due to the presence of the White Cliffs. The river canyon opens here and sunlight shines in from above. A rainbow crosses over the falls to the west and a narrow path continues to the south.', True, '007', False)
        self.c = room.Room('Cellar', 'You are in a dark and damp cellar with a narrow passageway leading east, and a crawlway to the south.  On the west is the bottom of a steep metal ramp which is unclimbable. (The rest off the dungeon is still a work in progress, sorry for the inconvenice!)', False, '070', False)

        self.rooms = [self.hw, self.hn, self.he, self.hs, self.k, self.a, self.lr, self.f1, self.fp, self.t, self.f2, self.c1, self.f3, self.f4, self.c2, self.cv, self.rl, self.er]

        self.hw.add_items({'mailbox':{'leaflet':'# Welcome to the unofficial python version of Zork I! There are many commands you can use,\n-go : takes one direction, allows you to move around the map (or you can just type the dirction first and not use go)\n-take : takes one item name, allows you to take items from the room and put them in your inventory\n-look : can take the name of an item but if no items are in the arguments it will print the rooms descirption\n-read : takes name of an item, allows you to read papers\n-open : takes name of container or door in the room, allows you to open contianers and doors\n-close : takes name of a contianer, allows you to close containers (closing doors has not yet been implemented)\nHope that you find this guide useful! have fun!'}})
        self.k.add_items({'sack':{'lunch':'Nothing special here', 'garlic':'Nothing special here'}})
        self.t.add_items({'egg':'Looks pretty sealed to me, you cannot open the egg'})
        self.he.add_door('Window', 'w', 'e', self.k)
        self.lr.add_door('Trap-door', 'd', 'u', self.c)

        self.player = player.Player(self.hw, {'sword':'A sharp long elvish sword'}, False, input('Player Name: '))

        print("")
        
        self.npcs = []

        #Check for a save an open it if there is, this works in python:
        save = open('save.pzk', 'r')
        
        l = None
        obj = []
        for line in save:
            l = line
            obj.append(line)
            break
        if l != None:
            print('Open save file?')
            IN = 'null'
            while IN not in ['y', 'n']:
                IN = str(input('> '))
                print("")
                IN = IN.lower()
                if 'yes' in IN:
                    IN = 'y'
                if 'no' in IN:
                    IN = 'n'
            if IN == 'y':
                print('Loading file...')
                for line in save:
                    if line == "Template:\n":
                        break
                    obj.append(line)
                play = obj[0]
                playNRaw = play.replace(' $Player$ ', '')
                playN = playNRaw[:playNRaw.find(' *@* ')]
                ID = play[play.find(' *@* '):play.find(' ^* ')]
                ID = ID.replace(' *@* ', '')
                for r in self.rooms:
                    if r.id == ID:
                        loc = r
                        break
                itemsRaw = play[play.find(' ^* '):play.find(' *^ ')]
                itemsRaw = itemsRaw.replace(' ^* ', '')
                itemsRaw = itemsRaw.split(', ')
                if '' in itemsRaw:
                    itemsRaw.remove('')
                items = {}
                for x in itemsRaw:
                    if ' *&* ' in x:
                        key = x[:x.find(' *:* ')]
                        subItems = {}
                        item = x.replace(key + ' *:*  *&* ', '')
                        item = item.split('*,* ')
                        if '' in item:
                            item.remove('')
                        if ' *&* ' in item:
                            item.remove(' *&* ')
                        for i in item:
                            value = i.split(' *:* ')
                            subItems.update({value[0]:value[1]})
                        items.update({key:subItems})
                    else:
                        key = x.split(' *:* ')
                        items.update({key[0]:key[1]})
                health = play[play.find('*^ '):-1]
                health = health.replace('*^ ', '')
                health = int(health)
                self.player = player.Player(loc, items, False, playN)

                for i in range(1, len(obj)):
                    if ' $NPC$ ' in obj[i]:
                        nameRaw = obj[i].replace(' $NPC$ ', '')
                        name = nameRaw[:nameRaw.find(' *@* ')]
                        for x in self.npcs:
                            if x.name == name:
                                ob = x
                                break
                        self.openSave(ob, obj[i], name)
                    if ' $ROOM$ ' in obj[i]:
                        idRaw = obj[i].replace(' $ROOM$ ', '')
                        ID = idRaw[:idRaw.find(' *@* ')]
                        R = self.getById(ID)
                        play = obj[i]
                        itemsRaw = play[play.find(' ^* '):play.find(' *^ ')]
                        itemsRaw = itemsRaw.replace(' ^* ', '')
                        itemsRaw = itemsRaw.split(', ')
                        if '' in itemsRaw:
                            itemsRaw.remove('')
                        items = {}
                        for x in itemsRaw:
                            if ' *&* ' in x:
                                key = x[:x.find(' *:* ')]
                                subItems = {}
                                item = x.replace(key + ' *:*  *&* ', '')
                                item = item.split('*,* ')
                                if '' in item:
                                    item.remove('')
                                if ' *&* ' in item:
                                    item.remove(' *&* ')
                                for y in item:
                                    value = y.split(' *:* ')
                                    subItems.update({value[0]:value[1]})
                                items.update({key:subItems})
                            else:
                                key = x.split(' *:* ')
                                items.update({key[0]:key[1]})
                        n = R.name
                        d = R.desc1
                        l = R.lit
                        R.__init__(n, d, l, ID, False)
                        if items != {}:
                            R.add_items(items)
                        doorRaw = play[play.find(' %* '):play.find(' *% ')]
                        doorRaw = doorRaw.replace(' %* ', '')
                        doorRaw = doorRaw.split(', ')
                        if '' in doorRaw:
                            doorRaw.remove('')
                        door = {}
                        for x in doorRaw:
                            key = x.split(' : ')
                            door.update({key[0]:key[1]})
                        for k, direct in door.items():
                            other = self.getById(k)
                            R.connect_to(other, direct)                        
            else:
                save.close()
                save = open('save.pzk', 'w')
        save.close()
        

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

        print(self.player.location.name +':\n'+ self.player.location.desc)

    def print_rooms(self):
        """
        print function for debugging
        calls print for all rooms
        """
        for r in self.rooms:
            r.print_details()

    def getById(self, ID):
        for i in self.rooms:
            if i.id == ID:
                return i
            
    #Opens save file and starts the game with its information NOTE-This also works in Python
    def openSave(self, obj, play, playN):
        ID = play[play.find(' *@* '):play.find(' ^* ')]
        ID = ID.replace(' *@* ', '')
        for r in self.rooms:
            if r.id == ID:
                loc = r
                break
        itemsRaw = play[play.find(' ^* '):play.find(' *^ ')]
        itemsRaw = itemsRaw.replace(' ^* ', '')
        itemsRaw = itemsRaw.split(', ')
        if '' in itemsRaw:
            itemsRaw.remove('')
        items = {}
        for x in itemsRaw:
            if ' *&* ' in x:
                key = x[:x.find(' *:* ')]
                subItems = {}
                item = x.replace(key + ' *:*  *&* ', '')
                item = item.split('*,* ')
                if '' in item:
                    item.remove('')
                if ' *&* ' in item:
                    item.remove(' *&* ')
                for i in item:
                    value = i.split(' *:* ')
                    subItems.update({value[0]:value[1]})
                items.update({key:subItems})
            else:
                key = x.split(' *:* ')
                items.update({key[0]:key[1]})
        health = play[play.find('*^ '):-1]
        health = health.replace('*^ ', '')
        health = int(health)
        obj.__init__(loc, items, False, playN)

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

    def combat(self, npc):
        print('You have been attacked by ' + npc.name + ' type "kill ' + npc.name + '" to fight back.')
        while True:
            c = input('> ')
            if 'kill' in c and npc.name in c:
                if 'sword' in self.player.items:
                    print('You ' + self.player.kill(npc, random.choice([0,15,15,15,15,25,25,25,25,50,50,50,75,75,100,100])) + ' Him')
                else:
                    print('You ' + self.player.kill(npc, random.choice([0,15,15,15,15,15,15,15,15,25,25,25,50,50,75,100])) + ' Him')
                if npc.death:
                    return False
            x = "He " + npc.kill(self.player, random.choice([0,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,25,25,25,50,50,75,100])) + " You"
            if " Killed " in x:
                print(x)
                return True

    def saveGame(self):
        save = open('save.pzk', 'w')
        item = ' ^* '
        print("Saving...")
        for k, v in self.player.items.items():
            if type(v) == type(str()):
                item += k + ' *:* ' + v + ', '
            if type(v) == type(dict()):
                item += k + ' *:* '
                item += ' *&* '
                for w, x in v.items():
                    item += w + ' *:* ' + x + '*,* '
                item += ' *&* '
        item += ' *^ '
        save.write(' $Player$ ' + self.player.name + ' *@* ' + self.player.location.id + item + str(self.player.health) + '0')
        for i in self.npcs:
            item = ' ^* '
            for k, v in i.items.items():
                if type(v) == type(str()):
                    item += k + ' *:* ' + v + ', '
                if type(v) == type(dict()):
                    item += k + ' *:* '
                    item += ' *&* '
                    for w, x in v.items():
                        item += w + ' *:* ' + x + '*,* '
                    item += ' *&* '
            item += ' *^ '
            save.write('\n $NPC$ ' + i.name + ' *@* ' + i.location.id + item + str(i.health) + '0')
        for i in self.rooms:
            if i.save:
                item = ' ^* '
                for k, v in i.items.items():
                    if type(v) == type(str()):
                        item += k + ' *:* ' + v + ', '
                    if type(v) == type(dict()):
                        item += k + ' *:* '
                        item += ' *&* '
                        for w, x in v.items():
                            item += w + ' *:* ' + x + '*,* '
                        item += ' *&* '
                item += ' *^ '
                doors = ' %* '
                for x in i.openDoors:
                    for k, v in x.items():
                        doors += k.id + ' : ' + v + ', '
                doors += ' *% '
                save.write('\n $ROOM$ ' + i.id + ' *@* ' + item + doors)
        save.close()
        time.sleep(2)
        print("")
        return 'Saved'

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
            x = self.move(i)
            if len(self.player.location.play) > 0:
                for i in self.player.location.play:
                    if self.combat(i):
                        return 'dead'
                    else:
                        return self.player.location.name+'\n'+self.player.location.desc
            else:
                return x

        if c1 == 'read':
            w = self.player.location.items
            x = self.locItems
            y = self.playItems
            z = self.player.items
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
                elif i in w:
                    d = w[i]
                    if "# " in d:
                        d.replace('# ', '')
                        return d
                elif i in z:
                    d = z[i]
                    if "# " in d:
                        d.replace('# ', '')
                        return d
            return "Sorry, the item could not be found."
                    
        if c1 == 'go':
            for i in c:
                if i in direct:
                    x = self.move(i)
                    if len(self.player.location.play) > 0:
                        for x in self.player.location.play:
                            if self.combat(x):
                                return 'dead'
                            else:
                                return self.location.name+'\n'+self.location.desc
                    else:
                        return x
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
            y = self.locItems
            for i in c:
                if i in x:
                    if i == 'mailbox':
                        return 'Are you serious?'
                    if len(self.player.items) == 8:
                        return 'Your load is too heavy, you cannot pick this up'
                    else:
                        self.player.take(i)
                        return 'Taken'
                        self.player.location.save = True
                if i in y:
                    if len(self.player.items) == 8:
                        return 'Your load is too heavy, you cannot pick this up'
                    else:
                        self.player.take(i)
                        self.player.location.save = True
                        return 'Taken'
            return 'Could not find the item.'

        if c1 == 'open':
            self.locItems = {}
            self.playItems = {}
            doors = {}
            for k, v in self.player.location.items.items():
                self.locItems.update({k.lower():v})
                
            for k, v in self.player.items.items():
                self.playItems.update({k.lower():v})
                
            for k, v in self.player.location.door.items():
                doors.update({k.lower():v})
                
            for i in c:
                if i in self.locItems:
                    d = self.locItems[i]
                    if type(d) == type(dict()):
                        if len(d) < 1:
                            return 'There is nothing in here.'
                        r = 'You see: '
                        p = []
                        for k, v in d.items():
                            r += k+', '
                            self.locItems.update({k:v})
                        return r
                if i in self.playItems:
                    d = self.playItems[i]
                    if type(d) == type(dict()):
                        if len(d) < 1:
                            return 'There is nothing in here.'
                        r = 'You see: '
                        p = []
                        for k, v in d.items():
                            r += k+', '
                            self.playItems.update({k:v})
                        return r
                if i in doors:
                    self.player.location.connect_to(doors[i][1], doors[i][0])
                    doors[i][1].connect_to(self.player.location, doors[i][2])
                    self.player.location.save = True
                    doors[i][1].save = True
                    return 'Opened'

        if c1 == 'close':
            x = self.locItems
            y = self.playItems
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

        #Saves all game information to the file NOTE-This also works in the Python IDE:
        if c1 == 'save':
            return self.saveGame()

        if c1 in ['quit', 'q']:
            IN = input("Do you wish to save?\n> ")
            if IN.lower() in ['yes', 'y']:
                print(self.saveGame())
                input("Hit enter to quit\n")
                quit()
            if IN.lower() in ['no', 'n']:
                input("Hit enter to quit\n")
                quit()
                    
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
            IN = str(input('> '))
            IN = IN.lower()
            for x in rem:
                if x in IN:
                    IN.replace(x, '')
            c = IN.split(' ')
            print('')
            out = self.process_cmd(c)
            if out == 'dead':
                break
            else:
                print(out)
        str(input('Hit enter to exit\n> '))
        quit()
            
    def win(self):
        print("congrats, you have won the game!")
        input('Hit enter to exit\n> ')
        quit()

if __name__ == '__main__':
    g = Game()
    g.start()
