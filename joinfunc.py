lis = ["john", "cena", "hone", "dena", "dasdas", "cursor"]
for i in lis:
    print(f"{i} and", end=" ")
# Syntax
# string.join(iterable) iterable = list or dictionary or tuple
# When using a dictionary as an iterable, the returned values are the keys, not the values.
a = " and ".join(lis)
print("\n", a)
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
