def hofstaderA(n):
    if n < 0:
        return
    if n == 0:
        return 1
    return n - hofstaderB(hofstaderA(n-1))
    
def hofstaderB(n):   
    if n < 0:
        return
    if n == 0:
        return 0
    return n - hofstaderA(hofstaderB(n-1))