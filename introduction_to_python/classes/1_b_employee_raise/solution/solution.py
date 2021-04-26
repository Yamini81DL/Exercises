class Employee:
    def __init__(self,name,employee_id,salary,years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

def give_raises(employee_lst):
    for i in employee_lst:
        #print("hi")
        if i.years_at_company <= 5:
            i.salary+= 5000
        elif i.years_at_company > 5 and i.years_at_company < 10:
            i.salary+= 8000
        else:
            i.salary+= 10000

