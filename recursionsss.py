def factorial_iterative(n):
    fac = 1
    for i in range(n): # range initiates a variable from 0 (default) and terminates it at n(in this case)
        fac = fac * (i+1)
    return fac

num = int(input("enter the no."))
print(factorial_iterative(num), "factorial using iterative method")

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
 # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # when n == 1 it'll straight up return 1 
    # 5 * 4 * 3 * 2 * 1 = 120
print(factorial_recursive(num), "factorial using recursive method")
