import sys
from routes.routes import f1, f2
from exercices.conditionals import test as test1
from exercices.listAndRandom import test as test2
from exercices.loopsAndRange import test as test3
from exercices.hangman import test as test4
from exercices.encrypt import test as test5
from exercices.dictionaries import test as test6


def main():
    params = sys.argv[1:]
    if len(params) > 0:
        if params[0] == "1":
            print("is 1")
        elif params[0] == "2":
            print("is 2")
        else:
            f1()
            f2()
    else:
        test6()


main()
