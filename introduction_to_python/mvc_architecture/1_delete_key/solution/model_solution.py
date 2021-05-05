
movie_list = {1:"Twilight", 2:"Mulan", 3:"The Shawshank Redemption", 4:"Ocean's Eight", 5:"Harry Potter", 6:"The Intern"}

def get_list():
    return movie_list

def del_list_key(del_key):
    # If key exist in dictionary then delete it using del.
    key_to_be_deleted = del_key
    if key_to_be_deleted in movie_list:
        #print(f'Deleting {movie_list[1]} from the list')
        print(f"Deleting {movie_list[del_key]} from the list")
        del movie_list[del_key]
    else:
        print(f'Key {key_to_be_deleted} is not in the dictionary')
        print(type(del_key))
    #m_lst = list(movie_list.items())    
    return movie_list
    
    