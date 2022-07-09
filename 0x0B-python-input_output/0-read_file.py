#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    reads text file and prints to stdout
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print("{}".format(line))
