# ls = [i for i in range(100) if i%3==0]
# """
# listname = [-item you want to print -for loop -condition]
# """
# print(ls)

# dic = { i:f"bablu{i}" for i in range(100) }
# print(dic)
# n3 = \n

#
# dict1 = {i:f"chuty{i}" for i in range(5)}
# print(dict1)
# dict2 = {v:k for k,v in dict1.items()}
# print(dict2)

dre = {dress for dress in ["dress1", "dress2", "dress1", "dress1", "dress2"]}
print(dre)
"""
SET COMPREHENSION
doesnt print redundant elements
VS
LIST COMPREHENSION
prints all elements
"""
dre = [dress for dress in ["dress1", "dress2", "dress1", "dress1", "dress2"]]
print(dre)
"""
USE '('  & ')' to make a    G E N E R A T O R
"""
evens = (i for i in range(100) if i%2 == 0)
# print(evens.__next__())
for item in evens:
    print(item)
