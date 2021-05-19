def fibonacci(n):
    if n < 0:
        return -1
    elif n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def paths_nth_stair(n):
    if n <= 1:
        return n
    return fibonacci(n+1) 