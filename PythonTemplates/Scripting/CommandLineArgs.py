"""
A template to make use of command line arguments as program input
"""

import sys
# Alternatively: " from sys import argv "


def main():
    # Error when command line args are malformed
    if len(sys.argv) == 1:
        print("You must specify an argument!")

    # Index argv like a list
    print(sys.argv[0])  # arg 0 is the ran command (e.g. CommandLineArgs.py)
    print(sys.argv[1])  # arg 1 is the first command specified by the user


if __name__ == "__main__":
    main()
