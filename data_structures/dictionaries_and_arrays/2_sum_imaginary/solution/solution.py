def sum_imaginary(ilst):
    sum1 = 0
    sum2 = 0
    for i in ilst:
        #print(i[1])
        sum1 += i[0]
        sum2 += i[1]
    return (sum1, sum2) 