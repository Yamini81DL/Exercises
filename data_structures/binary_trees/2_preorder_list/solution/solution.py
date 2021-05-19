class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key

def Preorder(root):
    lst = []
    if root:
        lst.append(root.key)
        print(lst)
        lst = lst + Preorder(root.left)
        print('lst after Left -->',  lst)
        lst = lst + Preorder(root.right) 
        print('lst after Right -->',  lst)
    return lst 
     
items = Node(5)
items.left = Node(6)
items.right = Node(7)
items.left.left = Node(8)
items.left.right = Node(9)
result_value_1 = Preorder(items)     
print(result_value_1)