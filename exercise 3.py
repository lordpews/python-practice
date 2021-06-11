# rules
# number of guesses = 9
# no. of guesses left
# no. of guesses one took
# gameover
x = 32
nog = 0
print("you have 9  guesses left")
while True:
    g = int(input("guess the number \n"))
    nog += 1
    if nog<9:
        if g > 32:
            print("your guess is bigger \n")
            print("guesses left", 9 - nog)

        elif g < 32:
            print("your guess is smaller \n")
            print("guesses left", 9 - nog)

        else:
            print("right answer \n")
            print("guesses took = ", nog)
            break
    else:
        print("game over noob hahaha")

