def pes(stri):
    return f"wow wow balle balle {stri}"


def befd(x, y):
    return x + y + 3

 print(__name__)
if __name__ == '__main__':
    print(pes("sasur"))
    print(befd(2, 2))

# __name__ is a variable that has different name based on its location
# if __name__ is of the file its value will be __main__
#  If this file is being imported from another module, __name__ will be set to the module’s name
# check tutmain2.py for more info
# ༼ つ ◕_◕ ༽つ I M P O R T A N T ༼ つ ◕_◕ ༽つ
# if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
