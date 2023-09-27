from exercices.coffee_machine.menu import Menu, MenuItem
from exercices.coffee_machine.coffee_maker import CoffeeMaker
from exercices.coffee_machine.money_machine import MoneyMachine

# 1: Print Report
# 2: Check and see if resources are sufficient
# 3: Process money entered by the buyer
#    (quarters: 25c, dimes: 10c, nickels: 5c, pennies: 1c)
# 4: Check and see if transaction is successful
# 5: Make coffe


def coffee():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while True:
        # 1: print reports
        money_machine.report()
        coffee_maker.report()

        # 2: check and see if resources are sufficient
        user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        order = menu.find_drink(user_choice)
        if order and coffee_maker.is_resource_sufficient(order):
            
            # 3: process money entered by the buyer
            if money_machine.make_payment(order.cost):
                
                # 4: make coffee
                coffee_maker.make_coffee(order)
