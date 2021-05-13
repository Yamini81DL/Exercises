# Insert data at the given index. Index starts from 1
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insert_at_index(self, index, data):
        ind = 1
        n1 = Node(data)
        if self.head == None:
            return None
        else:
            thisvalue = self.head
            print('Head --> ', thisvalue.data)
            while thisvalue.next != None:
                ind += 1
                if ind == index:
                    n1.next = thisvalue.next
                    thisvalue.next = n1                    
                thisvalue = thisvalue.next

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)
items.insert_at_index(2, 2)

print(items.head.data)# == 20
print(items.head.next.data)# == 2        