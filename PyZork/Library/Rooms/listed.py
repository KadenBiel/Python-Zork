class listed():
    """Object for managing the library of rooms"""
    def __init__(self):
        """Init function, gives object a name"""
        self.name = "Rooms List Manager"

    def getList(self):
        """Get list function opens list file and extracts the data"""
        li = open('Rooms.list', 'r') #opens list file
        lis = [] #var for storing list
        for line in self.li:
            """each new line is 1 object in the list"""
            if line != 'null':
                lis.append(line)
            else:
                li.close()
                return "No Rooms Found"
        li.close()
        return lis

    def clearList(self):
        """Function for clearing the list"""
        li = open('list.dat', 'w')
        li.write('null')
        li.close()
        return "Cleared"

    def addItem(self, item):
        """Function for adding items to the list (called whenever a new room is created)"""
        oli = open('list.dat', 'r')
        lis = []
        for line in oli:
            lis.append(line)
        oli.close()
        nli = open('list.dat', 'w')
        lis.append(item)
        for i in lis:
            nli.write(i)
        nli.close()
        return "added"