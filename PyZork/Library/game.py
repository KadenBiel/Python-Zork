class Game:

    def __init__(self, p, r, i, n, s):    
        """
        Initializes game state
        """
        self.validMoves = ['north', 'n', 'south', 's', 'east', 'e', 'west', 'w', 'northeast', 'ne', 'northwest', 'nw', 'southeast', 'se', 'southwest', 'sw', 'up', 'u', 'down', 'd']
        self.player = p
        self.room = r
        self.items = i
        self.npc = n
        self.save = s
        self.sID = None

    def combat(self, npc):
        print('You have been attacked by ' + npc.name + ' type "kill ' + npc.name + ' with <object>" to fight back.')
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

    def cmd(self, c):
        c1 = c[0]

        if c1 in self.validMoves or c1 == "go":
            try:
                x = self.move(c1)
            except:
                if c[1] in self.validMoves:
                    x = self.move(c[1])
                else:
                    print("'"+c[1]+"' is not a valid direction")
            if len(self.player.location.hostile) > 0:
                for i in self.player.location.hostile:
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

        if c1 == 'save':
            n = input("Please enter a name for your save\n> ")
            return self.save.save(n, self.sID)

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


    def move(self, c):
        """
        Moves the player, needs a direction
        """
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
            raise TypeError("'"+c+"' is not a direction")