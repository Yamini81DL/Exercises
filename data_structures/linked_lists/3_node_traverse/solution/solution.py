class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        if self.head == None:
            return None
        else:
            thisvalue = self.head
            while thisvalue != None:
                print(thisvalue.data)
                thisvalue = thisvalue.next