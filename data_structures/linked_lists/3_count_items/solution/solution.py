# Count Items

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head = None):
        self.head = head
        
    def get_count(self):
        count = 1
        if self.head == None:
            return 0
        else:
            thisvalue = self.head
            print('Head --> ', thisvalue.data)
            while thisvalue.next != None:
                count += 1
                thisvalue = thisvalue.next
            return count    

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)

print(items.get_count()) #== 3