from coffee_menu import MENU
from coffee_menu import resources
import time


def process_order(drink):
    global drinkprocess
    if drinkprocess:
        price = MENU[drink]['cost']
        print(f'the price of drink is ${price} proceed to payment ')
        payment(price)

    if drinkprocess:

        print(f'your {drink} is served \n Thanks for your patronage')
        print("next customer Please")
        time.sleep(2)
    else:
        print(f'{drink} cannot be served ')
        print("next customer Please")
        time.sleep(2)

def off_coffe():
    global serving
    serving = False
    print("... Turning off ...")
    time.sleep(2)
    print("OFF")


def report():
    print("The Report of resource is as follows ")
    global updated_resources
    for i, resource in enumerate(updated_resources):
        if i==3:
            print(f"{i + 1}. {resource} --- ${updated_resources[resource]} ")

        else:
            print(f"{i +1}. {resource} --- {updated_resources[resource]} ml ")
    time.sleep(2)




def check(drink):
    global drinkprocess
    global updated_resources
    drinkprocess = True
    for i,drink_item in enumerate(MENU[drink]['ingredients']):
        available_resource = updated_resources[drink_item]
        needed_resource = MENU[drink]['ingredients'][drink_item]
        if available_resource < needed_resource:
            drinkprocess = False
            print(f'{drink_item} is not enough')
    updateresource(drink)
def payment(cost):
    global updated_resources
    dime = 0.10 * int(input("how many dimes: "))
    quaters = 0.25 * int(input("how many quaters: "))
    nickel = 0.05* int(input("how many nickels: "))
    penny = 0.01 * int(input("how many pennies: "))
    total = float(penny + nickel + dime + quaters )

    if total >= cost:
        change = total - cost
        updated_resources['money'] += cost
        print(f"Here's your change ${float(change)} \n payment confirmed")

    elif total < cost:
        global drinkprocess
        drinkprocess = False
        print('not enough money, Money refunded')


def updateresource(selected_drink):
    global drinkprocess
    global updated_resources
    if drinkprocess:
        for i, drink_item in enumerate(MENU[selected_drink]['ingredients']):
            needed_resource = MENU[selected_drink]['ingredients'][drink_item]
            updated_resources[drink_item] -= needed_resource



# def updatemoney(money):
#     global updated_resources
#     updated_resources['money'] += money

drinkprocess = ''

updated_resources = {
  "water": resources['water'],
  "milk": resources['milk'],
  "coffee": resources['coffee'],
  "money":resources['money']}


