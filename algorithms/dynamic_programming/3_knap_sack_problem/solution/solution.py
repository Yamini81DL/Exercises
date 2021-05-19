def knap_sack(x, items):
    for k, (v1,v2) in items.items():
        sum = 0
        if v2 < x:
            if sum < x:
                sum += v2

    print(sum)


print(knap_sack(5, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}))# == 8)        