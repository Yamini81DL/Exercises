def remove_ages(pdict,x,y):
    for k,v in list(pdict.items()):
        if v < x or v > y:
            item = pdict.popitem()
    return pdict