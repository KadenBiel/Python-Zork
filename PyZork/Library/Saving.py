import os, Library

class saver:
    """
    Creates, stores and opens game saves
    Stores and opens maps
    """
    def __init__(self):
        self.libs = Library.lib()
        self.Game = self.libs.gameS
        self.Player = self.libs.player
        self.Room = self.libs.room
        self.Items = self.libs.items
        self.NPC = self.libs.npc
        self.Save = self.libs.save

        dat = open("Library/gameSaves/saveData.pzk", 'r')
        for line in dat:
            sLen = int(line)
            break
        if sLen > 0:
            for i in range(len(self.saves)):
                nS = open("Library/gameSaves/save"+str(i)+".pzk", 'r')
                for line in nS:
                    items.append(line)
                    break

    def save(self, n, id=None):
        if id == none:
            id = len(self.saves)
        nSave = open("Library/gameSaves/save"+id+".pzk", 'w')
        player = self.player.getAttributes()
        rooms = self.room.getSave()
        items = self.item.getSave()
        npcs = self.npc.getSave()
        map = self.libs.map
        print("Archiving Attributes")
        attributes = [n, player, rooms, items, npcs, map]
        print("Writing Save")
        for i in attributes:
            nSave.write(i)
        nSave.close()
        if id == len(self.saves):
            self.saves.append(n)
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
