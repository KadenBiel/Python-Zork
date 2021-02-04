from Library import lib
class Game():

    def __init__(self):    
        """
        Initializes game state
        """
        tree = lib.mod
        self.validMoves = ['north', 'n', 'south', 's', 'east', 'e', 'west', 'w', 'northeast', 'ne', 'northwest', 'nw', 'southeast', 'se', 'southwest', 'sw', 'up', 'u', 'down', 'd']
        self.id = 0
        self.player = tree[1]
        self.rooms = tree[2]
        self.items = tree[3]
        self.npc = tree[4]
        self.save = tree[5]
        self.ver = lib.ver

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

if __name__ == '__main__':
    g = Game()
    g.start()