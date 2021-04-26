def binomial_coefficient(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    else:
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)