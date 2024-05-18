#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
	args = len(argv) - 1
    for i in range(args):
		sum = sum + int(argv[i])
	print("{}".format(sum))
