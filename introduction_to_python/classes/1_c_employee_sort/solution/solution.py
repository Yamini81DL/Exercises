class Employee:
    def __init__(self,name,employee_id,salary,years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company


def sort_employees(employee_lst):
    name_lst =[]
    for i in employee_lst:
        name_lst.append(i.name)
    name_lst.sort()
    return name_lst