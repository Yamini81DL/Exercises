def intersect_lists(lst1,lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    inter = set1.intersection(set2)
    intersect = list(inter)
    return intersect

