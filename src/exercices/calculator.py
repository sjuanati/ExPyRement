import sys
from typing import Union

def test():
    # create calculator that receives 2 inputs & an operation, and calculates the result
    # user can use the result for another calculation or do a new calculation (clear func)
    # separate functions per operation
    more_calcs = True
    res = first_calc()
    while more_calcs:
        calcs = input('Do you want to do another calc with the result (y/n): ').lower()
        more_calcs = True if calcs == 'y' else False
        if more_calcs:
            res = second_calc(res)
        else:
            break

def operation(num1: float, num2: float, op: str) -> float:
    if num2 == 0 and op == '/':
        print('You bastard! division by zero is undefined')
        return 0
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        print(f'Unknown operatior {op}')
        sys.exit()
    
def first_calc() -> Union[float, bool]:
    num1 = float(input('Insert first number: '))
    num2 = float(input('Insert second number: '))
    op = input('Insert operation: (+,-,*,/): ')
    res = operation(num1, num2, op)
    print(f'Result: {res}')
    return res

def second_calc(num1: float) -> float:
    num2 = float(input('Insert new number: '))
    op = input('Insert operation: (+,-,*,/): ')
    res = operation(num1, num2, op)
    print(f'Result: {res}')
    return res

def is_number(num) -> bool:
    if isinstance(num, (int, float, complex)):
        return True
    else:
        return False
