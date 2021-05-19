def median_of_medians(lst):
    lst.sort()
    mid = len(lst) // 2
    res = (lst[mid] + lst[~mid]) / 2
    return res