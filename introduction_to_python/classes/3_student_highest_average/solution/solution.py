class Student:
    
    stud_lst = []
    
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        Student.stud_lst.append(self)
        self.avg = sum(self.grades)/len(self.grades)
        
      
def highest_avg(stud_lst):
   # stud_avg = []
    sorted(stud_lst, key=lambda x: getattr(x, 'avg'), reverse=True)    
    #stud_lst.sort(key=lambda x: stud_avg, reverse=True)
    return stud_lst[0].name
           
           
        