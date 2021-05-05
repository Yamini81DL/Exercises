from model_solution import get_list, Prog
from view_solution import show_list, update_key, enter_value, display

program_list = get_list()
show_list(program_list)
key = update_key()
value = enter_value()
new_list = Prog(key,value)
result = new_list.update_list_key()
display(result)
