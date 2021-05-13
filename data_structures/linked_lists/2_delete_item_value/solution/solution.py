class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
        
    def delete_item_by_value(self,x):
        if self.head == None:
            return None
        elif self.head.data == x:
            self.head = None
        else:
            thisvalue = self.head
            while thisvalue.next != None:
                if thisvalue.next.data == x:
                    thisvalue.next = thisvalue.next.next
                thisvalue = thisvalue.next     
                    
items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)
items.head.next.next.next = Node(50)
items.delete_item_by_value(40)

print(items.head.data)# == 20)
print(items.head.next.data)# == 30)
print(items.head.next.next.data)# == 50)
                
        