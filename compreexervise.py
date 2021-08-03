noi = int(input("no of items you want to enter \n"))
list1 = input("enter the elements of list separated by ',' \n")
list0 = list1.split(",")
list0 = list0[:noi]
cpre = int(input("Which Comprehension do you want : \n"
                 "1 : List \n"
                 "2 : Dictionary \n"
                 "3 : Set \n"))
if cpre == 1:
    lss = [items for items in list0]
    print(lss)
elif cpre == 2:
    res = dict(zip(range(1, noi+1), list0))
    print(res)
elif cpre == 3:
    lss = {items for items in list0}
    print(lss)
