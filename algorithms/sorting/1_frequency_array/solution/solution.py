def frequency_array(lst):
    new_lst = list()
    if lst:
        lst_size = max(lst)        
        for item in range(0,lst_size+1):
            new_lst.append(lst.count(item))        
        return new_lst
    return lst


lst = [1, 1, 3, 4, 4, 5, 6, 8, 8, 8, 9]
print(frequency_array(lst)) #== [0, 2, 0, 1, 2, 1, 1, 0, 3, 1]    