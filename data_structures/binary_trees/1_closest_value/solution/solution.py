class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key

def closest_value(node, target):
        r = node.key
        child = node.left if target < r else node.right
        if not child:
            return r
        n = closest_value(child, target)
        return min((r,n), key=lambda x: abs(target-x))  
         