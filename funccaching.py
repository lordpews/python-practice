import time
from functools import lru_cache

nox = int(input("how much data you want cache: \n"))


@lru_cache(maxsize=nox)
def funcs(n):
    # some random stuff
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("running funcs")
    funcs(3)
    print("Done...  Calling again")
    funcs(3)
    print("pheewww...  Ho gya")
