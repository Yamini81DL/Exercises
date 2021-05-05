from view_solution import show_list, retrive_book, display
from model_solution import get_list, Book_Auth

book_list = get_list()
show_list(book_list)
book = retrive_book()
author = Book_Auth(book)
data = author.retrive_book()
display(data)    
