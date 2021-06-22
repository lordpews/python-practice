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
        print("which book do you want \n"
              "1: Maths \n"
              "2:Physics \n"
              "3:Biology \n"
              "4:note book lmao")
        i = int(input("enter the input"))
        if i == 1:
            le = input("enter the name of the lender")
            print(f"{le} has {self.booklist[0]}")
            del self.booklist[0]
        if i == 2:
            le = input("enter the name of the lender")
            print(f"{le} has {self.booklist[1]}")
            del self.booklist[1]
        if i == 3:
            le = input("enter the name of the lender")
            print(f"{le} has {self.booklist[2]}")
            del self.booklist[2]
        if i == 4:
            le = input("enter the name of the lender")
            print(f"{le} has {self.booklist[3]}")
            del self.booklist[3]
        print("list of books: \n")
        for items in self.booklist:
            print(items)

    def addbook(self):
        nb = str(input("enter the name of the new book"))
        self.booklist.append(nb)

    def returnbook(self):
        return 0


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
        if choice == 2:
            library1.lendbook()
        if choice == 3:
            library1.addbook()
        if choice == 4:
            library1.returnbook()
