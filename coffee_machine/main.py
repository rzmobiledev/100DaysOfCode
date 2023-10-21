from menu import MENU, resources


# process coins
def calculation(q: int, d: int, n: int, p: int) -> float:
    """To do a match calculation with amount of money the user inserted"""
    quarters: float = 0.25
    dimes: float = 0.10
    nickles: float = 0.05
    pennies: float = 0.01

    return (q * quarters) + (d * dimes) + (n * nickles) + (p * pennies)


# if resources are available
def resource_is_available(ingredient: str, amount: int) -> bool:
    """True or False if amount of resource is available"""
    if amount > resources[ingredient]:
        return False
    else:
        return True


SHUTDOWN = False
RESOURCE_IS_ENOUGH = True
# create variable money as global variable
money: float = 0

list_menus = ("espresso", "latte", "cappuccino", "off", "report")
espresso_ingredients = MENU["espresso"]["ingredients"]
latte_ingredients = MENU["latte"]["ingredients"]
cappuccino_ingredients = MENU["cappuccino"]["ingredients"]

# show report

while not SHUTDOWN:
    # Prompt user by asking "what would you like? (Espresso/latte/cappuccino)"
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # check if user give a correct input
    if user_prompt not in list_menus:
        # instruct to fill correct menu
        print("Choose 'espresso', 'latte', or 'cappuccino'")
        # break or repeat the programme
        continue

    elif user_prompt == "off":
        SHUTDOWN = True

    elif user_prompt == "report":
        print(f"Water: {resources['water']}")
        print(f"Water: {resources['milk']}")
        print(f"Water: {resources['coffee']}")
        print(f"Money: ${money}")
        continue

    else:
        # we need to loop through all MENU
        for val in MENU[user_prompt].values():
            # check if val has another dict
            if isinstance(val, dict):
                for k, v in val.items():
                    if not resource_is_available(ingredient=k, amount=v):
                        print(f"Sorry there is not enough {k}.")
                        # exit from the loop
                        RESOURCE_IS_ENOUGH = False
                        break
                    else:
                        RESOURCE_IS_ENOUGH = True

        if not RESOURCE_IS_ENOUGH:
            continue

        print("Please insert coins.")
        quarter = int(input("how many quarters?: "))
        dime = int(input("how many dimes?: "))
        nickle = int(input("how many nickles?: "))
        penny = int(input("how many pennies?: "))

        # calculate all user's coin and compare with the price
        user_coins = calculation(quarter, dime, nickle, penny)

        # check if user has enough money
        if user_coins < MENU[user_prompt]['cost']:
            print("Sorry that's not enough money. Money refunded")
            # please put break or cycle the program back
            continue
        else:
            money += MENU[user_prompt]['cost']

        # decrease resources volume
        for value in MENU[user_prompt].values():
            # check if value has another dict
            if isinstance(value, dict):
                for k, v in value.items():
                    # decrease resources
                    resources[k] -= v

        # small change if user has more money
        # the change should be rounded to 2 decimal places.
        dollar_in_change = round(user_coins - MENU[user_prompt]['cost'], 2)

        # show user the change
        print(f"Here is ${dollar_in_change} dollars in change.\n")
        print("Here is your latte. Enjoy!")
