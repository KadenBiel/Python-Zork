from Library import game, Items, NPC, Player, Rooms, Saving
import os

class lib:
    def __init__(self):
        self.gameS = game.Game()
        self.player = Player.playLib()
        self.room = Rooms.roomLib()
        self.items = Items.itemLib()
        self.npc = NPC.npcLib()
        self.save = Saving.saver()
        self.map = None
        self.ver = "v1.3"
        self.maps = os.listdir("Library/maps/")

    def initData(self):
        print("Checking for map...\n")
        if self.room.listed() == []:
            print("No maps open.\n")
            try:
                for n, i in enumerate(self.maps):
                    print(str(n)+') '+i)
            except TypeError:
                print("No map files found")
                return
            usrIn = None
            print("\nSelect a map from the list (use the numbers to select)")
            while usrIn not in range(len(self.maps)):
                try:
                    usrIn = int(input("> "))
                    if usrIn in range(len(self.maps)):
                        break
                    else:
                        print("\nInvaild selection")
                except:
                    print("\nInput must be an interger")
            print("\nOpening...")
            self.openMap(self.maps[usrIn])
        print("\nGame State: Ready")

    def openMap(self, n):
        if n in self.maps:
            os.system("python Library/maps/"+n)
            return True
        else:
            return False

    def addMap(self, f, n):
        if n+'.py' in self.maps:
            usrIn = input("You are about to overwrite" + n + ".py, do you wish to continue? (y/n)\n> ").lower()
            while usrIn not in ['y', 'n', 'yes', 'no']:
                usrIn = input("y/n\n> ").lower()
            if 'n' in usrIn:
                return "Okay."
        try:
            nMap = open(f, 'r')
            oMap = open("Library/maps/"+n+".py", 'w')
            for line in nMap:
                oMap.write(nMap)
            nMap.close()
            oMap.close()
            self.maps.append(n+".py")
            return "Map Added"
        except:
            return "Invalid Path"

    def delMap(self, n):
        if n+'.py' in self.maps:
            os.remove("Library/maps/"+n+'.py')
            self.maps.pop(n+'.py')
            return 'Removed'
        else:
            return "Could not find "+n+'.py'

    def send(self, c):
        self.game.cmd(c)