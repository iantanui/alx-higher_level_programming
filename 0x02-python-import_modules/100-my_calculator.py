#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argv = argv[1:]

    if len(argv) < 3 or len(argv) > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[1] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[0])
        b = int(argv[2])
        if argv[1] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        if argv[1] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        if argv[1] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        if argv[1] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
