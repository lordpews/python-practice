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
