import os
from time import sleep
# Coffee Ingredients
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine = True  # machine is on

coffee_process = True
# TODO 1. Report
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def report():
    print(f"Water: {water}\nMilk: {milk}\ncoffee: {coffee}\nmoney: {profit}")


# TODO 2. Check if the ingredients are sufficient
def check_ingredients(user_input):
    if user_input != "espresso":
        menu_milk = MENU[user_input]["ingredients"]["milk"]
    menu_water = MENU[user_input]["ingredients"]["water"]
    menu_coffee = MENU[user_input]["ingredients"]["coffee"]
    if water < menu_water:
        print("Sorry there is not enough water.")
        return False
    elif coffee < menu_coffee:
        print("Sorry there is not enough coffee.")
        return False
    elif user_input == "latte" or user_input == "cappuccino":
        if milk < menu_milk:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True
    else:
        return True


# TODO 3. Process Coins Asking the user to insert the coins
def process_coins(user_input):
    quarters_coins = float(input("How many quarters?: "))
    dimes_coins = float(input("How many dimes?: "))
    nickels_coins = float(input("How many nickels?: "))
    pennies_coins = float(input("How many pennies?: "))
    coffee_money = MENU[user_input]["cost"]
    total_coins = quarters_coins * 0.25 + nickels_coins * 0.05 + dimes_coins * 0.10 + pennies_coins * 0.01
    if coffee_money > total_coins:
        print(f"Sorry that's not enough money. Money Refunded")
        return False
    else:
        if total_coins > coffee_money:
            refunding_coins = "{:.2f}".format(total_coins - coffee_money)
            print(f"Here is the remaning change: ${refunding_coins}")
        print(f"Here is your {user_input} ☕. Enjoy!.")
        global profit
        profit += coffee_money
        return True


def user_choice():
    user_wants = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_wants == "report":
        report()
    elif user_wants == "off":
        print("Not available")
        global machine
        machine = False
    elif user_wants == "on":
        machine = True
    else:
        if check_ingredients(user_wants):
            print("Please insert coins.")
            if process_coins(user_wants):
                if user_wants != "espresso":
                    menu_milk = MENU[user_wants]["ingredients"]["milk"]
                    global milk
                    milk -= menu_milk
                menu_water = MENU[user_wants]["ingredients"]["water"]
                menu_coffee = MENU[user_wants]["ingredients"]["coffee"]
                global water, coffee
                water -= menu_water
                coffee -= menu_coffee




while machine:
    user_choice()
