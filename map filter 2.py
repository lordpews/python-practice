list1 = [1, 2, 3, 4, 5, 6]


def get(num):
    return num > 2


lsit2 = list(filter(get, list1))
print(lsit2)
# The filter() method filters the given sequence with the help of a function
# that tests each element in the sequence to be true or not.
