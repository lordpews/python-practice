# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(list of books, library_name)

# dictionary (books-name of person)

# create a main function and run an infinite while loop asking
# users for their input

class Library:
    def __init__(self, book_list, name):
        self.booklist = book_list
        self.name = name

    def displaybooks(self):
        return print(f"{self.booklist}")

    def lendbook(self):
        for items in self.booklist:
            print(items)
        i = str(input("which book do you want \n"))
        i = i.lower()
        lender = str(input("enter the name of the lender"))
        print(f"{lender} has {i}")
        bookl[i] = lender
        print("list of books and lender:  \n", bookl)

        self.booklist.remove(i)
        print(f"books left in the library : \n")
        for items in self.booklist:
            print(items)

    def addbook(self):
        nb = str(input("enter the name of the new book"))
        self.booklist.append(nb)

    def returnbook(self):
        print("list of books and lender:\n", bookl)
        retbook = input("enter the book you want to return")
        retbook = retbook.lower()
        bookl.pop(retbook)
        print("list of books and lender:\n", bookl)

bookl = {}

library1 = Library(["maths book", "physics book", "biology book", "note book"], "school library")


if __name__ == '__main__':
    while True:
        choice = int(input("enter the input:\n"
                           "1: Display books \n"
                           "2: lend book \n"
                           "3: add book \n"
                           "4: return book \n"))
        if choice == 1:
            library1.displaybooks()
        elif choice == 2:
            library1.lendbook()
        elif choice == 3:
            library1.addbook()
        elif choice == 4:
            library1.returnbook()
