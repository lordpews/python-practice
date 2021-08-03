import json

data = '{"var1" : "pews", "var2" : "lmao" }'  # this is a string

"""

To parse JSON from URL or file, use json.load().

For parse string with JSON content, use json.loads().

"""

parsed = json.loads(data)  # # this is a json dictionary

print(parsed)

print(data)

print(parsed["var1"])
# print(data["var1"])

f = open("koko.json")

parsed2 = json.load(f)

dara2 = {
    "v1": "chut", "v2": ["eq", "ew", "chew"],
    "v3": ["bread", "mal"],
    "fridege": ('poti', 420),
    "isgood ": False
}

"""
dumps() json. dumps() function converts a Python object into a json string.

"""

jscomp = json.dumps(dara2)

print(jscomp)

# JSON dump sort keys
# sort_keys =  False by default
# Dumping JSON serializes a JSON object to string format for printing.
# Sorting the keys when dumping saves the key-value pairs in alphabetical order by keys.
# numerical keys will be sorted to initial indexes

json_object = {'name': 'John', 'age': 30, 'car': 'None', '1' : 'kihhs'}

a_json = json.dumps(json_object)  # without sort keys = True

print(a_json)

a_json = json.dumps(json_object, sort_keys=True)  # with sort keys = True

print(a_json)
