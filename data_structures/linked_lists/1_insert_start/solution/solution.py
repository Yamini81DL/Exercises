class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head =None):
        self.head = head

    def insert_at_start(self, data):
            n1 = Node(data)
            if self.head == None:
                self.head = n1   
                print('When Head is none -->', self.head.data)
            else:
                thisvalue = self.head
                print('Original Head --> ', self.head.data)        
                n1.next = self.head
                print('Hi', n1.next.data, self.head.data)
                self.head = n1
                print('Aftr insertion head is --> ', self.head.data)  
                print('After head  -->', self.head.next.data)#, 'after head-->' thisvalue.next)

items = linkedList()
items.head = Node(20)
items.insert_at_start(40)
items.insert_at_start(50)
assert items.head.data == 50
assert items.head.next.data == 40
assert items.head.next.next.data == 20
                   