import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map
kokokokoooo
Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass'''

# findall, search, split, finditer,sub
# pattern1 = re.compile(r'Moore')
# matches = pattern1.finditer(mystr)
# for match in matches:
#  print(match)
#
# print(mystr[249:254])

# pattern1 = re.compile(r'.')  # . = any character
# pattern1 = re.compile(r'^Tata')  # ^ = starts with the following character
# pattern1 = re.compile(r'fass$')  # $ = ends with the preceding character
# pattern1 = re.compile(r'as*')  # * =  Zero or more occurrences
# in this case the returning string must have one 'a' and 0 or more occurrences of 'i'
# pattern1 = re.compile(r'as+')  # + =  one or more occurrences
# in this case the returning string must have one 'a' and 1 or more occurrences of 'i'
# pattern1 = re.compile(r'ko{3}') # {x} = exactly the no of specified occurrences
# in this case we are looking for 'k' followed by 3 'o's
# pattern1 = re.compile(r'(ko){3}') # () is used to group
# in this case we are looking for 'ko' with 3 occurrences
# pattern1 = re.compile(r'(ko){3}|ass') # x|y = Either x or y
# in this case we are looking for 'ko' with 3 occurrences OR ass

"""SPECIAL SEQUENCES"""
# pattern1 = re.compile(r'\ATata') # returns a match if the specified characters
# are at the beginning of the string
# pattern1 = re.compile(r'\bFax')
# pattern1 = re.compile(r'ass\b')
# Returns a match where the specified characters
# are at the beginning or at the end of a word r'ain'\b
pattern1 = re.compile(r'\d{5}-\d{4}')
# \d Returns a match where the string contains digits (numbers from 0-9)
# \d searches digit with exactly {5} occurrences followed by a - and then \d digit with
# exactly {4} occurrences

matches = pattern1.finditer(mystr)
print(type(matches))
for match in matches:
    print(match)
