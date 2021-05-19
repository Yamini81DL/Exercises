
class Node:
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        if self.next:
            return f"{self.value}, {self.next}"
        else:
            return str(self.value)

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

    def __len__(self):
        count = 1
        #print('Head --> ', self.head_node.value)
        if self.head_node == None:
            return 0
        else:
            thisqueue = self.head_node
            #print('thisqueue -->', thisqueue.value)
            while thisqueue.next != None:
                count+= 1
                #print("Iam here")
                thisqueue = thisqueue.next
                print(count)
               # print('thisq.next --> ', thisqueue.next.value)
            return count  

queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
print(len(queue1))# == 3

#queue2 = Queue()
#print(len(queue2))# == 0                 
