def inventory_price(idict):
    tot_price = 0
    for key, (valX, valY) in idict.items():
        tot_price += valX * valY
    return int(tot_price)