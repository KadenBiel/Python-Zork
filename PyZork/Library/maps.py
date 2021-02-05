import Library
import os

class map():
    def __init__(self):
        self.maps = []
        self.id = 7
        tree = Library.lib.mod
        self.rooms = tree[2]
        self.items = tree[3]
        self.npc = tree[4]
        self.save = tree[5]
        self.ver = Library.lib.ver

        files = os.listdir("./")
        self.files = files.sort()

    def openMap(self, n):
        if n+'.py' in self.files:
            os.system("exec ./"+n+".py")
            return True
        else:
            return False

    def addMap(self, f, n):
        if n+'.py' in self.files:
            usrIn = input("You are about to overwrite" + n + ".py, do you wish to continue? (y/n)\n> ").lower()
            while usrIn not in ['y', 'n', 'yes', 'no']:
                usrIn = input("y/n\n> ").lower()
            if 'n' in usrIn:
                return "Okay."
        try:
            nMap = open(f, 'r')
            oMap = open("./"+n+".py", 'w')
            for line in nMap:
                oMap.write(nMap)
            nMap.close()
            oMap.close()
            return "Map Added"
        except:
            return "Invalid Path"

    def delMap(self, n):
        if n+'.py' in self.files:
            os.remove("./"+n+'.py')
            return 'Removed'
        else:
            return "Could not find "+n+'.py'