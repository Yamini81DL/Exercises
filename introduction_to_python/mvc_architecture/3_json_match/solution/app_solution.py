from view_solution import show_list, retrive_sport, retrive_country, display
from model_solution import get_list, Sports

data_list = get_list()
show_list(data_list)
sport = retrive_sport()
country = retrive_country()
data_a = Sports(sport,country)
data_b= Sports(sport, country)
result = data_a.retrive_match()
result = data_b.retrive_match()
display(result)