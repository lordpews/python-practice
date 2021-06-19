import sys
print(sys.path)
import jila2
print(jila2.a)
# these 2 basically does the same thing
# but the second one 'from jila2 import a'
# is a bad practice
#
from jila2 import a
print(a)
print(jila2.jkse1("jifajida"))