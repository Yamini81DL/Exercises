def adjacency_list(adjacency_matrix):
    start = 0
    res = []
    lst = []
    n = len(adjacency_matrix)

    for i in range(n):
        res.append(lst*n)
    while start < n:
        y = adjacency_matrix[start]
        for i in range(len(y)):
            if y[i] == 1:
                res[start].append(i)
        start += 1
    return res


    