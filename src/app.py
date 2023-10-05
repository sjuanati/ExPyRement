import sys
from routes.routes import f1, f2
from exercices.conditionals import test as test1
from exercices.listAndRandom import test as test2
from exercices.loopsAndRange import test as test3
from exercices.hangman import test as test4
from exercices.encrypt import test as test5
from exercices.dictionaries import test as test6
from exercices.calculator import test as test7
from exercices.blackjack import test as test8
from exercices.guess import test as test9
from exercices.coffee_machine.main import coffee as test10
from exercices.quiz.main import quiz as test11
from exercices.gui import test as test12
from exercices.hirst.main import test as test13
from exercices.listener import test as test14
from exercices.race import test as test15



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
        test15()
        print('eps')


main()
