class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author_instance):
        if isinstance(author_instance, Author):
            self._author = author_instance
        else:
            raise Exception

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book_instance):
        if isinstance(book_instance, Book):
            self._book = book_instance
        else:
            raise Exception

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date_instance):
        if type(date_instance) == str:
            self._date = date_instance
        else:
            raise Exception

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties_instance):
        if type(royalties_instance) == int:
            self._royalties = royalties_instance
        else:
            raise Exception

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)