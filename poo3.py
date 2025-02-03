class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f'El libro {self.title} ha sido prestado')
        else:
            print(f'El libro {self.title} no está disponible')
            
    def returnBook(self):
        self.available = True
        print(f'El libro {self.title} ha sido devuelto')   


class User:
    def __init__(self, name, userId):
        self.name = name
        self.userId = userId
        self.borrowedBooks = []
        
    def borrowBook(self, book):
        if book.available:
            book.borrow()
            self.borrowedBooks.append(book) 
        else: 
            print(f'El libro {self.title} no está disponible')
            
    def returnBook(self, book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
        else:
            print(f'El libro {book.title} no está en la lista de prestados')
            
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def addBook(self, book):
        self.books.append(book)
        print(f'El libro {book.title} ha sido agregado')
    
    
    def registerUser(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido registrado')
    
    
    def showAvailableBoooks(self):
        print('Libros disponibles')
        for book in self.books:
            if book.available:
                print(f'{book.title} por {book.author}')
      
# Crear libros          
book1 = Book('Cien años de soledad', 'Gabriel Garcia Márquez')
book2 = Book('1984', 'George Orwell')

# Crear usuario
user1 = User('Pablo', '1')

#Crear biblioteca
biblioteca = Library()
biblioteca.addBook(book1)
biblioteca.addBook(book2)
biblioteca.registerUser(user1)


#Mostrar libros
biblioteca.showAvailableBoooks()

#Realizar prestamo de libro
user1.borrowBook(book1)


#Mostrar libros
biblioteca.showAvailableBoooks()

#Devolver libro
user1.returnBook(book1)

#Mostrar libros
biblioteca.showAvailableBoooks()