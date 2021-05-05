import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
 
    def __lt__(self,other):
        #x_vector = self.x
        #y_vector = self.y
        #vector = (x_vector, y_vector)
        #magnitude = math.sqrt(sum(v**2 for v in vector))
        self.mag = math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))
        other.mag = math.sqrt((other.x ** 2) + (other.y ** 2) + (other.z ** 2))
        if (self.mag < other.mag):
            return True
        else:
            return False
        
    def __gt__(self,other):
        self.mag = math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))
        other.mag = math.sqrt((other.x ** 2) + (other.y ** 2) + (other.z ** 2))
        if (self.mag > other.mag):
            return True
        else:
            return False     
          