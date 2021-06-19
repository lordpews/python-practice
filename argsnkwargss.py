# The special syntax *args in function definitions in python is used to pass a variable number of arguments
# to a function
# in the following example we wanted to pass bunch of variables into the function so we used *args

def fa(a, *args, **kwargs):
    print(a)
    for i in args:
        print(i)

    for k, v in kwargs.items():
        print(k, "is", v)


ko = ["pews", "ewps", "sewp", "wesp", "gia"]
g = "number 1 khiladi"

# ༼ つ ◕_◕ ༽つ______I M P O R T A N T _____༼ つ ◕_◕ ༽つ
# In a function definition always pass normal variable first then *args and then **kwargs
kw = {"pews": "good", "sewp": "bad", "ewps": "neutral"}
fa(g, *ko, **kw)
print(f"{g} is bad")
#   **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
#   A keyword argument is where you provide a name to the variable as you pass it into the function.
#   One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
#   That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
