def sum_first_n(n):
    sum = 0
    if n == 1:
        return 1
    else:
        sum += sum + n +sum_first_n(n-1)
        return sum   