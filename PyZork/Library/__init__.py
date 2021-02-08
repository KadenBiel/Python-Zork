from Library import game, Items, NPC, Player, Rooms, Saving, maps
import os

class lib:
    def __init__(self):
        self.player = Player.playLib()
        self.room = Rooms.roomLib()
        self.items = Items.itemLib()
        self.npc = NPC.npcLib()
        self.save = Saving.saver(self.player, self.room, self.items, self.npc)
        self.map = maps.map(self.player, self.room, self.items, self.npc)
        self.gameS = game.Game(self.player, self.room, self.items, self.npc, self.save)
        self.ver = "v1.3"
        self.maps = os.listdir("Library/maps/")

    def send(self, c):
        self.game.cmd(c)

class mapLib:
    def __init__(self):
        self.maps = os.listdir("Library/maps/")
        self.map = maps.map()
        print("Checking for map...\n")
        while True:
            if self.map.name == None:
                print("No maps open.\n")
                try:
                    for n, i in enumerate(self.maps):
                        print(str(n)+') '+i)
                except TypeError:
                    print("No map files found")
                usrIn = None
                print("\nSelect a map from the list (use the numbers to select) to add a map type 'addMap <path to your map file>'")
                while usrIn not in range(len(self.maps)):
                    try:
                        usrIn = input("> ")
                        usrIn = int(usrIn)
                        if usrIn in range(len(self.maps)):
                            break
                        else:
                            print("\nInvaild selection")
                    except:
                        if 'addMap' in usrIn:
                            cmd = usrIn.split(' ')
                            f = cmd[1]
                            name = f.split('/')
                            n = name[-1]
                            self.addMap(f, n)
                            usrIn = len(self.maps) - 1
                            break
                        print("\nInput must be an interger")
                print("\nOpening...\n")
                self.openMap(self.maps[usrIn])
                break
            else:
                print("Would you like to continue playing " + self.map.name + "?")
                usrIn = input("> ").lower()
                while usrIn not in ['y', 'n', 'yes', 'no']:
                    usrIn = input("y/n\n> ").lower()
                if 'y' in usrIn:
                    print("\nOkay.")
                    break
                else:
                    print("\nOkay.")
                    self.clearMap()
                    self.map.name = None
        return None

    def openMap(self, n):
        if n in self.maps:
            m = open("Library/maps/"+n, 'r')
            ma = open("Library/maps.py", 'w')

            for line in m:
                ma.write(line)
            ma.close()
            m.close()

            return True
        else:
            return False

    def clearMap(self):
        ma = open("Library/maps.py", 'w')
        l = ["class map:\n", "    def __init__(self, p=None, r=None, i=None, n=None):\n", "        self.name = None\n"]
        for line in l:
            ma.write(line)
        ma.close()

    def addMap(self, f, n):
        if n in self.maps:
            usrIn = input("You are about to overwrite" + n + ".py, do you wish to continue? (y/n)\n> ").lower()
            while usrIn not in ['y', 'n', 'yes', 'no']:
                usrIn = input("y/n\n> ").lower()
            if 'n' in usrIn:
                return "Okay."
        try:
            nMap = open(f, 'r')
            oMap = open("Library/maps/"+n, 'w')
            for line in nMap:
                oMap.write(line)
            nMap.close()
            oMap.close()
            self.maps.append(n)
            print("Map Added")
            return "Map Added"
        except FileNotFoundError:
            print("Error")
            return "Invalid Path"

    def delMap(self, n):
        if n+'.py' in self.maps:
            os.remove("Library/maps/"+n+'.py')
            self.maps.pop(n+'.py')
            return 'Removed'
        else:
            return "Could not find "+n+'.py'