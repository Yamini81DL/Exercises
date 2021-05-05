from view_solution import capture_name, capture_age, display
from model_solution import Name_Age

name = capture_name()
age = capture_age()
info = Name_Age(name, age)
result = info.store()
display(result)