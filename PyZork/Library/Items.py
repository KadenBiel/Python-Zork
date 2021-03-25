class itemLib(object):
    """Items indentifier"""
    def __init__(self):
        self.iList = []
        
    def listed(self):
        return self.iList
    
    def create(self, n, desc, atk=15, litSrc=False):
        iden = len(self.iList)
        newItem = item(n, desc, atk, litSrc)
        self.iList.append()


class item(object):
    def __init__(self, n, desc, atk, litSrc):
        self.name = n
        self.attack = atk
        self.desc = desc
        self.litSrc = litSrc
        if self.litSrc:
            self.lit = False