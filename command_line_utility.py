import argparse
import sys


def calc(args):  # the arguments parsed to this function will be taken from __main__
    if args.o == "add":
        return args.x + args.y

    elif args.o == "sub":
        return args.x - args.y

    elif args.o == "mul":
        return args.x * args.y

    elif args.o == "div":
        return args.x / args.y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float,
                        default=1.0,
                        help="Enter a no. contact pews")
    parser.add_argument('--y', type=float,
                        default=3.0,
                        help="Enter a no. contact pews")
    parser.add_argument('--o', type=str,
                        default=3.0,
                        help="for calculation. Enter a no. contact pews")
    args = parser.parse_args()
    # parser the added argument to the function
    sys.stdout.write(str(calc(args)))
    # sys.stdout.write is used to display stuff on windows powershell
    # line 32 will display the result of calc function with args as parsed above in the windows powershell

# power shell
# PS C:\Users\piyush thakur> cd .\PycharmProjects\
# PS C:\Users\piyush thakur\PycharmProjects> python .\command_line_utility.py
# None
# PS C:\Users\piyush thakur\PycharmProjects> python .\command_line_utility.py --x 10 --y 2 --o div
# 5.0
# PS C:\Users\piyush thakur\PycharmProjects>
