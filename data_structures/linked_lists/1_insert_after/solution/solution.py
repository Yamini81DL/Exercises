class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def insert_after_item(self,x,data):
        insert_after_item(self,x,data)        

class linkedList:
    def __init__(self, head=None):
        self.head = head
        #val = head.data

    def insert_after_item(self,x,data):
        n1 = Node(data)
        if self.head == None:
            return None
        elif self.head.data == x:
            n1.next = self.head.next  
            self.head.next = n1
        else:
            thisvalue = self.head
            while thisvalue.next != None:
                if thisvalue.next.data == x:
                    n1.next = thisvalue.next.next.next
                    thisvalue.next.next = n1
                thisvalue = thisvalue.next    


items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(50)
print(items.insert_after_item(30, 0))
print(items.head.data)
#print(items.head.next.data)
#print(items.head.next.next.data)