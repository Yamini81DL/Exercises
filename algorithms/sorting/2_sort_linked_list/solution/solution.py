class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def sort_ll(self):
        return

    class sort_ll(self):

        def insert_element(self, data):
            if self.head is None:
                self.head = Node(data, self.head)
            else:
                current = self.head
                previous = current
                while current.data < data:
                    if current.next is None:
                        current.next = Node(data, current.next)
                        return True
                    previous = current
                    current = current.next
                if previous == current:
                    self.head = Node(data, self.head)
                else:
                    previous.next = Node(data, previous.next)
            self.size += 1



  
