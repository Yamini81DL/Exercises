#Write your solutions here
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key

    def insert(self, key):
        if not self.root:                  # if the root node doesnt exist > #base_case
            self.root = Node(key)
        elif key <= self.root.key:
            if self.root.left:                              # if left exists  
                self.root.left.insert(key)      # recursive call
            else:
                self.root.left = Node(key)            # base_case
        else:
            if self.root.right:
                self.root.right.insert(key)     # recursive call
            else:
                self.root.right = Node(key)

