
class Queue:
    
    def __init__(self, head_node= None, tail_node= None):
        self.head_node = head_node
        self.tail_node = tail_node
        
    def __str__(self):
        if self.head_node:
            return f"< {self.head_node} >" 
        else:
            return "<>"    
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node       #   head_node.next = TUEnode
            self.tail_node = new_node
#         print(f">>{self.head_node}, >>{self.head_node.next}, >>{self.tail_node}, >>{self.tail_node.next}")

        
    def dequeue(self):
        if not self.head_node:
            print("Queue is empty")
            return None
        value = self.head_node.value
        self.head_node = self.head_node.next
#         if not self.head_node:
#             self.tail_node = None
        return value

    def empty(self):
        if self.head_node:
            return False
        return True
    
    def postfix_eval(self,exp):
        for i in exp:
            if if i.isdigit():
                self.push(i)