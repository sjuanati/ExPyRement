import sys
from routes.routes import f1, f2

# v1
from v1.conditionals import test as test1
from v1.listAndRandom import test as test2
from v1.loopsAndRange import test as test3
from v1.hangman import test as test4
from v1.encrypt import test as test5
from v1.dictionaries import test as test6
from v1.calculator import test as test7
from v1.blackjack import test as test8
from v1.guess import test as test9
from v1.coffee_machine.main import coffee as test10
from v1.quiz.main import quiz as test11
from v1.gui import test as test12
from v1.hirst.main import test as test13
from v1.listener import test as test14
from v1.race import test as test15

# v2
from v2.lottery import test as test16
from v2.movies import test as test17
from v2.oop import test as test18
from v2.filez.main import test as test19
from v2.books.app import test as test20
from v2.generators import test as test21
from v2.unpacking import test as test22
from v2.collections import test as test23
from v2.datetime import test as test24
from v2.regex import test as test25
from v2.logs import test as test26
from v2.scrap.main import test as test27
from v2.scrapping_quotes.app import test as test28
from v2.scrapping_books.app import test as test29
from v2.concurrency.threads import test as test30
from v2.concurrency.processes import test as test31


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
        test31()


if __name__ == "__main__":
    main()
