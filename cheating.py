

print("Welcome to Calculator")
print("Enter a operator \n + for addition \n - for subtraction \n * for multiplication \n / for division")
operator = input()
List_of_operators = ["+", "-", "*", "/"]

if operator not in List_of_operators:
    print("Please enter a valid operator")
else:
    print("Enter two values")
    num1 = int(input())
    num2 = int(input())

    if operator == '+':
        if num1 == 56 and num2 == 9:
            print(77)
        elif num1 == 9 and num2 == 56:
            print(77)
        else:
            print(num1 + num2)

    elif operator == '-':
        print(num1 - num2)

    elif operator == '*':
        if num1 == 45 and num2 == 3:
            print(555)
        elif num1 == 3 and num2 == 45:
            print(555)
        else:
            print(num1 * num2)

    else:
        if num1 == 56 and num2 == 6:
            print(4)
        else:
            print(num1 / num2)