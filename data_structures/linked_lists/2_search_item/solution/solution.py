# Search if a node exists or not

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head = None):
        self.head = head
        
    def search(self,x):
        thisvalue = self.head
        if self.head == None:
            return None
        elif self.head.data == x:
            return True
        else:
            while thisvalue.next != None:
                if thisvalue.next.data == x:
                    return True
                else:
                    return False
                thisvalue = thisvalue.next    
        #else:
         #   return False
        
items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)

print(items.search(30)) # == True
print(items.search(10))# == False
                   
            