def product_sequence_n(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * product_sequence_n(n-2)      