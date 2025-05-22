from decimal import Decimal

from pkg_resources import working_set

from data import MENU, resources
run = True
money = 0.0

def convert_letter_to_word(letter):
    if letter == "e":
        return "espresso"
    elif letter == "l":
        return "latte"
    elif letter == "c":
        return "cappuccino"
    elif letter == "r":
        return "report"
    else:
        return letter

def get_user_money():
    quarters = Decimal(input("Quarters: "))
    dimes = Decimal(input("Dimes: "))
    nickles = Decimal(input("Nickles: "))
    pennies = Decimal(input("Pennies: "))

    total = quarters * Decimal(".25") + dimes * Decimal(".10") + nickles * Decimal(".05") + pennies * Decimal(".01")
    return float(total)

def give_change(given_money, product_cost):
    working_money = round(given_money - product_cost, 2)
    print("Giving back $" + str(working_money))

    working_money = int(round(working_money * 100))

    quarters = working_money // 25
    working_money %= 25
    print("Quarters: ", int(quarters))

    dimes = working_money // 10
    working_money %= 10
    print("Dimes: ", int(dimes))

    nickles = working_money // 5
    working_money %= 5
    print("Nickles: ", int(nickles))

    pennies = working_money // 1
    working_money %= 1
    print("Pennies: ", int(pennies))

def check_resources(order):
    is_resources = True
    missing_ingredient = None
    ingredients = MENU[order]["ingredients"]

    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            return False, ingredient
    return True, None

def take_resources(order):
    ingredients = MENU[order]["ingredients"]

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

while run:
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        order = convert_letter_to_word(order)
        if order in ("espresso", "latte", "cappuccino", "off", "report"):
            break
    if order == "off":
        run = False
    elif order == "report":
        # print resources
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
        print(f"Money: ${money}")
    else:
        has_resources, missing_resources = check_resources(order)
        if not has_resources:
            print(f"Sorry there is not enough {missing_resources}")
        else:
            cost = MENU[order]["cost"]
            print("You need to pay up! it's $" + str(cost))
            payment = get_user_money()

            print("Money given:", payment)
            if payment < cost:
                print("Sorry but your broke!")
            else:
                # Add money
                money += cost
                give_change(payment, cost)
                take_resources(order)
                print(f"*Gives user their {order}*")
