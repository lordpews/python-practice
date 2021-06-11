"""operators in python"""
# arithmetic operators
# assignment operator
# logical operator
# comparison operator
# bitwise operator
# identity operator
# membership operator
"""arithmetic operator"""
# print("use of + ", 5 + 5)
# print("use of - ", 5 - 2)
# print("use of * ", 2 * 3)
# print("use of / ", 10 / 8)
# print("use of // divide but gives int value not float", 10 // 8)
# print("use of % modulus remainder", 10 % 8)
# print("use of ** exponential power", 5 ** 3)

"""assignment operator"""
"""x = 5
print(x)
x += 5  # add the number written next to += operator SIMPLY x=x+5
print(x)
x -= 5  # subtracts the number written next to += operator SIMPLY x=x-5
print(x)
x *= 5  # multiplies the number written next to += operator with x SIMPLY x=x*5
print(x)
x /= 5  # div the number written next to += operator  with x SIMPLY x=x/5
print(x)
x //= 5  # div the number written next to += operator  with x and gives the int value SIMPLY x=x%5
print(x)
x **= 5  # raises the power the number written next to += operator SIMPLY x=x**5
print(x)
x %= 2  # div the number written next to += operator  with x and gives remainder SIMPLY x=x%5
print(x)"""
# NOTE DUE TO SIMULTANEOUS OPERATION OF X ITS VALUE KEEPS CHANGING SO DON'T CALCULATE EACH OPERATION TAKING X=5

"""Comparison operators"""
# i = 5
# print(i == 8)
# print(i < 10)
# print(i > 10)
# print(i >= 10)
# print(i <= 10)

"""logical operators"""
"""# and
a = True
b = False
print(a and b)
print(a and a)
print(b and b)
print(b and a)
print("_________________")
# or
a = True
b = False
print(a or b)
print(a or a)
print(b or b)
print(b or a)"""

# identity operator
# is
# is not
"""print( 5 is 5)
print(5 is 6)

print(5 is not 0)
print(5 is not 5)"""

"""Membership operator"""
list1 = [2, 222, 33, 4, 42, 6565, 65, 6, 88]
# 'in' and 'not in'
print(32 in list1)
print(32 not in list1)

"""Bitwise Operators"""
# and = &
# or = |
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
print(0 | 2)
# in this case itll perform or operation on  2 bit form of 0 and 2
#   00
#  +10
#  =10 which is is equal to 2
print(0 & 3)
# in this case itll perform and operation on  2 bit form of 0 and 3
#   00
#   11
#  =00 which is is equal to 0

