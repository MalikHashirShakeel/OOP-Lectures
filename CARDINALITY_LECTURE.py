#--------------------------------------ASSOCIATION-------------------------------------------------------
# class Car:

#     def __init__(self,m,e,ID):
#         self.model = m
#         self.engine = e
#         self.id = ID

# class Engine:

#     def __init__(self,en):
#         self.number = en

# class PetrolPump:

#     def __init__(self,id):
#         self.id = id

# pp = PetrolPump("Shell-KHI-02")
# en = Engine("0114")
# my_car = Car("2024",en,pp.id)


#--------------------------------------------ONE TO ONE(BIDIRECTIONAL : AGGREGATION)--------------------------------------
# class Book:

#     def __init__(self,name,i):
#         self.name = name
#         self.isbn = i
#         self.isbn.add_book(self.name)
        
# class ISBN:
    
#     def __init__(self,i_n):
#         self.number = i_n
    
#     def add_book(self,b):
#         self.book = b

# i1 = ISBN("112-9675")
# b1 = Book("Programming",i1)
# print(i1.book)

#----------------------------------------------EXAMPLE2(COMPOSITION)--------------------------------------------------
# class Book:

#     def __init__(self,n,i):
#         self.name = n
#         self.isbn = ISBN(i)
#         self.isbn.add_book(self.name)

# class ISBN:

#     def __init__(self,no):
#         self.number = no

#     def add_book(self,b):
#         self.book = b


# b1 = Book("Programming","213-963")

#--------------------------------------------ONE TO MANY----------------------------------------------------

# class Library:

#     def __init__(self):
#         self.books = []

#     def add_book(self,b):
#         self.books.append(b)

#     def list_books(self):
#         for i in self.books:
#             print(i.name)
        

# class Book:
#     def __init__(self,n):
#         self.name = n

# b1 = Book("Mardana Kamzoori ka ilaaj.")
# b2 = Book("Bawaseer k khaatma.")
# l = Library()
# l.add_book(b1)
# l.add_book(b2)
# l.list_books()

#-----------------------------------------MANY TO MANY----------------------------------------------------
# class Book:

#     def __init__(self,n):
#         self.name = n
#         self.authors = []

#     def add_authors(self,name):
#         self.authors.append(name)

# class Author:

#     def __init__(self,a):
#         self.author_name = a
#         self.books = []

#     def add_book(self,name):
#         self.books.append(name)





























