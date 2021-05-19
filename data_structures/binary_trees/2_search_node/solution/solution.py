class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key

def search(root, key):
    if root:
        if key == root.key:  
            print('Root key is ', root.key)             # base case >>> 
            return True
        elif key < root.key and root.left:  
            print('Left key is ', root.left.key)           # recursive case
            return root.left.search(key)
        elif key > root.key and root.right:  
            print('Right key is ', root.right.key)          # recursive case
            return root.right.search(key)
        else:
            return False    
    else:
        return False

items = Node(6)
items.left = Node(4)
items.right = Node(9)
items.left.left = Node(3)
items.left.right = Node(5)
items.right.left = Node(7)
items.right.right = Node(11)

print(search(items,11)) # == True
#
#print(search(items,8)) # == False