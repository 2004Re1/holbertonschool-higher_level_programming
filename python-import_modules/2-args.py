#!/usr/bin/python3
from sys import argv
args = len(argv) - 1
print("{} arguments:".format(args))
pos = 1
while (args > pos):
    print("{}: {}".format(pos, argv[pos]))
    pos = pos + 1
