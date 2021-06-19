
import random, playsound


def winning_music():
    """
    Plays the winning music.
    """
    win_music = ["anime wow.mp3", "bruhh.mp3"]
    try:
        playsound.playsound(random.choice(win_music))
    except Exception as e:
        print(e)


def losing_music():
    """
    Plays the losing music.
    """
    lose_music = ["Nope.mp3", "Fart.mp3"]
    try:
        playsound.playsound(random.choice(lose_music))
    except Exception as e:
        print(e)


def tie_music():
    """
    Plays the tie music.
    """
    try:
        playsound.playsound(random.choice("Awkward Cricket.mp3"))
        playsound.playsound("Awkward Cricket.mp3")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("Welcome to the Snake Water Gun game!\n\n")
    print("\nWelcome to the Snake Water Gun game!\n\n")

    attempts = 1
    your_point = 0


@-40

, 39 + 40, 53 @ @
if __name__ == "__main__":

    while (attempts <= 10):

        lst = ["snake", "water", "gun"]
        lst = ["s", "w", "g"]
        ran = random.choice(lst)

        inp = input("Enter your choice (snake/water/gun): ")
        inp = input("Enter your choice (Snake(s), Water(w), Gun(g)): ")
        inp = inp.lower()

        if inp == ran:
            if inp == 's' and ran == 's':
                print("Tie")
                print(f"You chose {inp} and computer guess is {ran}")
                print(f"\nYou chose snake and Computer also chose snake! ")
                print("No body gets point\n")
                tie_music()


            elif inp == "snake" and ran == "water":
            elif inp == 'w' and ran == 'w':
                print("Tie")
                print(f"\nYou chose water and Computer also chose water! ")
                print("No body gets point\n")
                tie_music()


            elif inp == 'g' and ran == 'g':
                print("Tie")
                print(f"\nYou chose gun and Computer also chose gun! ")
                print("No body gets point\n")
                tie_music()


            elif inp == "s" and ran == "w":
                your_point = your_point + 1
                print(f"You choosed {inp} and computer guess is {ran}")
                print(f"\nYou choosed snake and Computer chose water! ")
                print("The snake drank water\n")
                print("You won this round")
                print("You got 1 point\n")
                winning_music()


            elif inp == "water" and ran == "snake":
            elif inp == "w" and ran == "s":
                computer_point = computer_point + 1
                print(f"You choosed {inp} and computer guess is {ran}")
                print(f"\nYou choosed water and Computer chose snake! ")
                print("The snake drank water\n")
                print("You lost this round")
                print("Computer gets 1 point\n")
                losing_music()


            elif inp == "water" and ran == "gun":
                print(f"You chose {inp} and computer guess is {ran}")
            elif inp == "w" and ran == "g":
                print(f"\nYou chose water and Computer chose gun! ")
                your_point = your_point + 1
                print("The gun sank in water\n")
                print("You won this round")


@-80

, 8 + 94, 8 @ @
if __name__ == "__main__":
    winning_music()


elif inp == "gun" and ran == "water":
    print(f"you choosed {inp} and computer guess is {ran}")
elif inp == "g" and ran == "w":
    print(f"\nYou choosed gun and Computer chose water! ")
    computer_point = computer_point + 1
    print("The gun sank in water\n")
    print("You Lost this round")


@-89

, 59 + 103, 59 @ @
if __name__ == "__main__":
    losing_music()


elif inp == "gun" and ran == "snake":
    print(f"You choosed {inp} and computer guess is {ran}")
elif inp == "g" and ran == "s":
    print(f"\nYou choosed gun and Computer chose snake! ")
    your_point = your_point + 1
    print("The snake was shot and it died\n")
    print("You won this round")
    print("You get 1 point\n")
    winning_music()

elif inp == "snake" and ran == "gun":
    print(f"you choosed {inp} and computer guess is {ran}")
elif inp == "s" and ran == "g":
    print(f"\nYou choosed snake and Computer chose gun! ")
    computer_point = computer_point + 1
    print("The snake was shoot and he died\n")
    print("You lost this round")
    print("computer gets 1 point\n")
    print("The snake was shot and he died\n")
    print("You lost this round!")
    print("Computer gets 1 point\n")

else:
    print("Invalid input!\n")
    continue

print("No. of guesses left: {}".format(10 - attempts))
print("\nNo. of guesses left: {}".format(10 - attempts))
attempts = attempts + 1

if attempts > 10:
    print("Game over!")
    print("\nGame over!\n")

print(f"Your score: {your_point} \nComputer's score: {computer_point}")

if computer_point > your_point:
    print("Computer won and you lost!")
    print("\nComputer won and you lost!\n")

elif computer_point < your_point:
    print("You won and computer lost!")
    print("\nYou won and computer lost!\n")

else:

    print("It was a tie!")
    print("invalid")
    print("Invalid")

print(10 - attempts, "no. of guesses left")
print(11 - attempts, "no. of guesses left")
attempts = attempts + 1

if attempts > 10:
    print("game over")
    print("\nGame over! ")

if computer_point > your_point:
    print("Computer wins and you loose")
    print("\nComputer wins and you lose!")

if computer_point < your_point:
    print("you win and the computer looses")
    print("\nYou win and the computer loses!")

print(f"your point is {your_point} and computer point is {computer_point}")
print(f"\nYour points are {your_point} and Computer's points are {computer_point}!\n")


