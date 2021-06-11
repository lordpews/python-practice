#!/bin/python3


#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

"""def solve(meal_cost, tip_percent, tax_percent):
    tc = meal_cost + (meal_cost * (tip_percent / 100)) + (meal_cost * (tax_percent / 100))
    return solve()


# Write your code here


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

print(solve())"""
print("astrologer's stars")
s = input("enter the holy integer")
p = input("enter true or false")


def bool(p):
    if p.lower() == "true":
        p = True
        print(p)
    elif p.lower() == "false":
        p = False
        print(p)


