# snake water gun
import random

choice = ["snake", "water", "gun"]
i = 0
m = 0
c = 0
while i < 10:
    i = i + 1
    comp = random.choice(choice)
    inp = input("enter your choice \ns = snake\nw = water\ng = gun\n")
    if inp == "s" and comp == "snake":
        print("comp:",comp,"you",inp)
        print("draw")
    if inp == "w" and comp == "water":
        print("comp:", comp, "you", inp)
        print("draw")
    if inp == "g" and comp == "gun":
        print("comp:", comp, "you", inp)
        print("draw")
    if inp == "w" and comp == "snake":
        print("comp:", comp, "you", inp)
        print("you lost")
        c = c + 1
    if inp == "w" and comp == "gun":
        print("comp:", comp, "you", inp)
        print("you won")
        m = m + 1
    if inp == "g" and comp == "water":
        print("comp:", comp, "you", inp)
        print("you lost")
        c = c + 1
    if inp == "g" and comp == "snake":
        print("comp:", comp, "you", inp)
        print("you won")
        m = m + 1
    if inp == "s" and comp == "water":
        print("comp:", comp, "you", inp)
        print("you won")
        m = m + 1
    if inp == "s" and comp == "gun":
        print("comp:", comp, "you", inp)
        print("you lost")
        c = c + 1
    if i == 10:
        break
a = f"score is you: {m} and computer {c}"
print(a)

if m < c:
    print("youve won the game")
elif m == c:
    print("game draw")
else:
    print("you lost to the computer noob ahahahjajaja")
