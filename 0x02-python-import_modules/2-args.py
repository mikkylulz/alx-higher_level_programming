#!/usr/bin/python3
import sys

def print_args(argv):
    num_args = len(argv)
    if num_args == 0:
        print("Number of argument(s): 0")
    else:
        print("Number of argument(s):", num_args, "argument(s)")
        for i in range(num_args):
            print(i + 1, ":", argv[i])
            if __name__ == "__main__":
                print_args(sys.argv)
