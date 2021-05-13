# Reverse the Linked List, this has been done in the Linked List Jupyter Notebook datastructures  

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
        
    def reverse(self):
        previous = None
        current = self.head
        while current:                        
            next = current.next             
            current.next = previous         
            previous = current              
            current = next 
        self.head = previous 
        return self
                