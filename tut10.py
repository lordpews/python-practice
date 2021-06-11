bhojan = {"piyush": "bhindi", "pews": "headshot", "lordpews": "ace",
          "sewp": {"b": "soup", "l": "tomato soup", "d": "rice"}}
print(type(bhojan))
print(bhojan)
d3 = bhojan
del d3["lordpews"]
print(bhojan)
d4 = bhojan.copy()
d4["lordpews"] = "ace"
print(d4)
print(bhojan)
print(d3)
print(bhojan["sewp"])
print(bhojan.get("piyush"))
d4.update({"papo": "tapo"})
print(d4)
print(d4.keys())
print(d4.items())
