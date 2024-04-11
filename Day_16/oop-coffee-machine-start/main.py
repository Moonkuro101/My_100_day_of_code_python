from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

Machine_on = True
while Machine_on:
    option = menu.get_items()
    User_drink = input(f"What would you like? {option} ").lower()
    if User_drink == 'report':
        machine.report()
        money.report()
    elif User_drink =='off':
        Machine_on = False
    else:
        drink = menu.find_drink(User_drink)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)

