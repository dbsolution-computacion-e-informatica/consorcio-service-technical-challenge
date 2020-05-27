import sys
from utils import checker


def main():
    """This main function allow us to test the "is_mutant" funciton faster using command line
    An example of use is: python3 src/main.py ABCDEF FEDCBA ABCDEF FEDCBA ABCDEF AAAAAA
    """
    print('Result: ', checker.is_mutant(sys.argv[1:]))


if __name__ == "__main__":
    main()
