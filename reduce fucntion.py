from functools import reduce
# The reduce(function,sequence) function is used to apply a particular function passed in
# its argument to all of the list elements mentioned in the sequence passed along

list1 = [1, 2, 3, 4, 5, 6]
prod = reduce(lambda x, y: x + y, list1)
print(prod)
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and
# the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.
