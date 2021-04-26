# Write your code here
def divisible_by_3(*args):
    L = []
    for i in args:
        if i % 3 == 0:
            L.append(i)
    return(L) 