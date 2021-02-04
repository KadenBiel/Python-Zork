from Library import lib
import os

class Saver(object):
    """
    Creates, stores and opens game saves
    Stores and opens maps
    """
    def __init__(self):
        tree = lib.mod
        self.saves = []
        self.player = tree[1]
        self.room = tree[2]
        self.item = tree[3]
        self.npc = tree[4]
        self.ver = lib.ver

        dat = open("/gameSaves/saveData.pzk", 'r')
        for line in dat:
            sLen = int(line)
            break
        if sLen > 0:
            for i in range(self.saves.len()):
                nS = open("/gameSaves/save"+str(i)+".pzk", 'r')
                for line in nS:
                    items.append(line)
                    break

    def save(self, n, id=self.saves.len()):
        id = id
        nSave = open("/gameSaves/save"+id+".pzk", 'w')
        player = self.player.getAttributes()
        rooms = self.room.getSave()
        items = self.item.getSave()
        npcs = self.npc.getSave()
        map = lib.currentMap
        print("Archiving Attributes")
        attributes = [n, player, rooms, items, npcs, map]
        print("Writing Save")
        for i in attributes:
            nSave.write(i)
        nSave.close()
        if id == self.saves.len():
            saves.append(n)
        return "Saved"
    
    def delSave(self, id):
       os.remove("/gameSaves/save"+id+".pzk")
       return "Deleted"
   
    def openSave(self, id):
        oSave = open("/gameSaves/save"+id+".pzk", 'r')
        attributes = []
        for line in oSave:
            attributes.append(line)
        oSave.close()
        return attributes