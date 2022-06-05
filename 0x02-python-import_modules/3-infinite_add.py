#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv)
    sum = 0

    if num_args > 1:
        for i in range(1, num_args):
            sum += int(argv[i])

    print(sum)
