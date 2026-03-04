class Author:
    all = []  # Stores all author instances

    def __init__(self, name: str):
        #Initialize a new Author with a name.
        self.name = name
        Author.all.append(self)

    def contracts(self):
        #Return a list of Contract objects related to this author.
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        #Return a list of Book objects related to this author via contracts.
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date: str, royalties: int):
        #Create a new contract between this author and a book.
        #param book: Book instance
        #param date: string representing contract date
        #param royalties: integer representing royalties
        #return: Contract instance
        return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self):
        #Return the total royalties from all contracts.
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []  # Stores all book instances

    def __init__(self, title: str):
        #Initialize a new Book with a title.
        self.title = title
        Book.all.append(self)

    def contracts(self):
        #Return a list of Contract objects related to this book.
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        #Return a list of Author objects related to this book via contracts.
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []  # Stores all contract instances

    def __init__(self, author, book, date: str, royalties: int):

        #Initialize a new Contract.
        #Validates all inputs to ensure correct types.

        # Validation
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)  # Add to the global list of contracts

    @classmethod
    def contracts_by_date(cls, date: str):
        #Return all contracts that match a given date.
        return [contract for contract in cls.all if contract.date == date]
    
    # Create Authors
a1 = Author("Alice")
a2 = Author("Bob")

# Create Books
b1 = Book("Python 101")
b2 = Book("SD for Beginners")

# Authors sign contracts
c1 = a1.sign_contract(b1, "2026-03-04", 5000)
c2 = a2.sign_contract(b1, "2026-03-05", 3000)
c3 = a1.sign_contract(b2, "2026-03-04", 7000)


# Books for an author
print("Alice's Books:", [book.title for book in a1.books()])  
# Output: ["Python 101", "AI for Beginners"]

# Authors for a book
print("Authors for 'Python 101':", [author.name for author in b1.authors()])  
# Output: ["Alice", "Bob"]

# Total royalties for an author
print("Alice's Total Royalties:", a1.total_royalties())  
# Output: 12000

# Contracts by date
contracts_today = Contract.contracts_by_date("2026-03-04")
print("Contracts on 2026-03-04:", [(c.author.name, c.book.title) for c in contracts_today])  
# Output: [("Alice", "Python 101"), ("Alice", "AI for Beginners")]