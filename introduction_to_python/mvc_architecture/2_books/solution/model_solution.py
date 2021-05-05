import json
book_list = {"The Firm" :"John Grisham", "The Apple" : "Devashish Sardana", "Shiv Trilogy" :"Amish Tripathi", 
    "Ponniyin Selvan" : "Kalki", "Pride and Prejudice" : "Jane Austin", "Gone With The Wind" : "Margaret Mitchell"}

#book_author_list = json.dumps(book_author_list, indent=4, sort_keys=True)    

def get_list():
    return book_list

class Book_Auth:
    
    def __init__(self,book):
        self.book = book
        #self.author = author        

    def retrive_book(self):
        return book_list.get(self.book)    