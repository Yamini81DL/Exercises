class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key

def height(node):
    hLeft = 0
    hRight = 0
    if node.left!= None:
        hLeft = height(node.left)
    if node.right!= None:
        hRight = height(node.right)
    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1;        