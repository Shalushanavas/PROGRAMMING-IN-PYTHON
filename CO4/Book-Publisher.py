class Publisher:
    title = ""
    author = ""
    def __init__(self):
        self.title = "New Publisher"
        self.author = "Publisher Name"

class Book(Publisher):
    def __init__(self):
        super().__init__()
        self.title = "Book Name"
        self.author = "Author Name"
    def getDetails(self):
        print("Name :" + self.title)
        print("Author :" + self.author)


class Python(Book):
    price = 450
    no_of_pages = 500
    def __init__(self):
        super().__init__()
        self.title = "Python for beginners"
        self.author = "Jack Vanderplas"

    def getDetails(self):
        print("Name :"+self.title)
        print("Author :" +self.author)
        print("Price : "+str(self.price))
        print("No of Pages : "+str(self.no_of_pages))

pyBook = Python()
pyBook.getDetails()

book = Book()
book.getDetails()


