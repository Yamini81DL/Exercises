# Code your solution here

shape = {3:"Triangle" , 4:"Quadrilateral" , 5:"Pentagon" , 6:"Hexagon", 7:"Heptagon", 8:"Octagon", 9:"Nonagon"}
g_lst = []
while True:
    g_int = int(input())
    if g_int not in shape:
            #print("Out of loop!!!")
            break
    else:
        g_lst.append(shape[g_int]) 
print(g_lst)     