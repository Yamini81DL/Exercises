# Code your solution here
from provided_code import grades

letter_grades= []
print(len(grades))
for i in range(0,len(grades)):
    if grades[i] >= 90 and grades[i] <=100:
        letter_grades.append("A")
    elif grades[i] >= 70 and grades[i] <=89:  
        letter_grades.append("B") 
    elif grades[i] >= 50 and grades[i] <=69:  
        letter_grades.append("C")
    elif grades[i] >= 35 and grades[i] <=49:  
        letter_grades.append("D")
    else:  
        letter_grades.append("F") 
   
print(letter_grades)


    
