def factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * factorial(n-1)        