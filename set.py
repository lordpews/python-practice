"""s=set([1,2,3,4])
print(type(s))
print(s)
r=(3,3,3,32,4)
print(type(r))
print(r)
l=["chiga", "migga", 1 ,2 ,3]
print(type(l))
print(l)
g=set(l)
print(g)
print(type(g))"""
s=set()
s.add(1)
s.add(2)
s.add(5)
print(s)
s1=s.intersection(
    {1,2,2,3,4,4,})
print(s,s1)
print(len(s))

