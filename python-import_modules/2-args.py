#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = len(argv) - 1
    print("{} arguments:".format(args))
    pos = 0
    while (args > pos):
        print("{}: {}".format(pos, argv[pos]))
        pos = pos + 1
