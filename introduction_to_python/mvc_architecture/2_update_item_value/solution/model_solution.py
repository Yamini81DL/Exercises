program_list = {1:"Python", 2:"Java", 3:"Javascript", 4:"C#" , 5:"R", 6:"SQL"}

def get_list():
    return program_list

class Prog:    

    def __init__(self,key,value):
        self.key = key
        self.value = value

    def update_list_key(self):
        program_list[self.key] = self.value
        return program_list