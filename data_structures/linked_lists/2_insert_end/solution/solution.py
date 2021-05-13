#Insert node at the end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head = None):
        self.head = head
        
    def insert_at_end(self,data):
        n1 = Node(data)
        if self.head == None:
            self.head = n1
        else:
            thisvalue = self.head
            while thisvalue.next != None:
                thisvalue = thisvalue.next
            thisvalue.next = n1    
        
        
        
        
        
        