
class Name_Age:

    data = []
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def store(self):
        Name_Age.data.append(self.name) 
        Name_Age.data.append(self.age)  
        return Name_Age.data