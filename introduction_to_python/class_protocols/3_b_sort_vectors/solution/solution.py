import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
           
    def sort_vectors(vect_lst):
        vect_mag = []
        for vect in vect_lst:
            mag =  math.sqrt((vect.x**2) + (vect.y**2) + (vect.z**2))
            vect_mag.append(mag)
        vect_lst.sort(key=lambda x : vect_mag)    
        #sort_vect = sorted(vect_lst, key=lambda x: getattr(x, vect_mag), reverse=True)
        #(math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2)))
        print(vect_lst)
        
        