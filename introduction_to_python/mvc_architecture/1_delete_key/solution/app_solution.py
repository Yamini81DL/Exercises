from model_solution import get_list, del_list_key #, movie_lst, m_lst
from view_solution import delete_key, display

movie_list = get_list()
display(movie_list)
del_key = delete_key()
final_list = del_list_key(del_key)
display(final_list)