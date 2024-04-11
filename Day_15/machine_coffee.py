from Menu import *
def caculator_resouces(drink):
    """"calculate the resources"""
    for i in drink['ingredients']:
        resources[i] -= drink['ingredients'][i]
    return drink['cost']

def change_custommer(coin,price):
    """"return change to customer"""
    return coin-price


def caculator_coin():
    """"return total of coin"""
    print('insert your coin please.')
    Total=int(input('pennies : '))*0.01
    Total+=int(input('nickles : '))*0.05
    Total+=int(input('dimes : '))*0.10
    Total+=int(input('quarters : '))*0.25
    return Total

def check_resources_coffee(drink):

    for item in drink['ingredients']:
        if drink['ingredients'][item]>resources[item]:
            print(f'Sorry our {item} is not enough ')
            return False
    return True

def coffee_machine():
    price = 0

    continue_machine=True

    while continue_machine:
        choice = input('What would you like? (espresso/latte,cappuccino) : ').lower()

        drink={}
        coin=0

        if choice=='off':
            continue_machine=False

        elif choice=="report":
            print(f"water : {resources['water']}ml")
            print(f"milk : {resources['milk']}ml")
            print(f"coffee : {resources['coffee']}g")
            print(f"price: {price}$")

        else:
            drink = MENU[choice]
            if check_resources_coffee(drink):
                coin=caculator_coin()
                if coin>=drink['cost'] :

                    change = round(change_custommer(coin,drink['cost']),2)
                    price+=caculator_resouces(drink)

                    print(f'Here is your change {change}$ ')
                    print(f'Here your coffee ☕ {choice} enjoy!')


                else:
                    
                    print('Sorry that not enough money')
                    
coffee_machine()
            