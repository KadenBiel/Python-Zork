import os, Library

class saver:
    """
    Creates, stores and opens game saves
    Stores and opens maps
    """
    def __init__(self, p, r, i, n):
        self.player = p
        self.room = r
        self.item = i
        self.npc = n
        self.saves = os.listdir('Library/gameSaves')

    def save(self, n, id=None):
        if id == None:
            id = len(self.saves)
        nSave = open("Library/gameSaves/"+str(id)+".pzk", 'w')
        player = self.player.getAttributes()
        rooms = self.room.getSave()
        items = self.item.getSave()
        npcs = self.npc.getSave()
        map = self.libs.map
        print("Archiving Attributes")
        attributes = [n, player, rooms, items, npcs, map]
        print("Writing Save")
        for i in attributes:
            nSave.write(str(i)+'\n')
        nSave.close()
        if id == len(self.saves):
            self.saves.append(str(id)+'.pzk')
        return "Saved"
    
    def delSave(self, id):
       os.remove("Library/gameSaves/save"+id+".pzk")
       return "Deleted"
   
    def openSave(self, id):
        oSave = open("Library/gameSaves/save"+id+".pzk", 'r')
        attributes = []
        for line in oSave:
            attributes.append(line)
        oSave.close()
        return attributes
