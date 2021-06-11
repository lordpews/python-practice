import math
import time
a = float(6.6)
print("this is %f" % a)
# %s - String (or any object with a string representation, like numbers)
#
# %d - Integers
#
# %f - Floating point numbers
#
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#
# %x/%X - Integers in hex representation (lowercase/uppercase)
x = "tit"
print("weight of my left %s is %f" % (x, a))
# for positional formatting we can use this % method where you can put %s for strings %d for int and %s for floats
# followed by the % and variable name for multiple variables create a tuple just as in above example
g = "whis is {} {}"
f = g.format(a, x)
print(f)
# this is new style string formatting where formatted data in inserted in {} just like in above example
g = "whis is {1} {0}"
f = g.format(a, x)
print(f)
# you can also change the positions by adding index numbers in {}
# The format() method allows you to format selected parts of a string.
a = f"{a} this is weight of my left {x} and 4 x 4 is {4 * 4}"
print(a)
# this how you make an f string you can straight up putyour variable name in {} and can even use functions like
# following example
a = f"{a} this is weight of my left {x} and sin60 is {math.sin(60)}"
print(a)
print(time.asctime())
l = f"this is {time.process_time()}"
print(l)