f1 = open("rgh3.py")
try:
    f = open("pews.txt")
except Exception as e:
    print(e)
else:
    print("itll run if except doesnt run")
finally:
    print("finally run this block")
    f.close()
    f1.close()

print("balle balle")