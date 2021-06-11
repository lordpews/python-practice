def fibo(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:

        return (n) + fibo(n-1)
    pass
x= int(input("no."))
print(fibo(x))


# 0 1 1 2 3 5 8 13