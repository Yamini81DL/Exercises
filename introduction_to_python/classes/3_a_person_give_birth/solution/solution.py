class Person:
    def __init__(self,name, age,spouse = None,children =[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children
        
    def give_birth(self,name):
        child = Child(name, 0, parents=[self])  # creating a object of the Child class
        self.children.append(child)
        if self.spouse:
            self.spouse.children.append(child)
            child.parents.append(self.spouse)
        
        
class Child(Person):
    def __init__(self, name, age, spouse=None , children=[], parents=None):
        super().__init__(name, age,spouse,children)
        self.parents = parents