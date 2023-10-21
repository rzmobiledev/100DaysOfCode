from coffee_machine.menu import MENU, resources

profit: float = 0


class MenuItem:

    def __init__(self, name: str):
        self.name = name
        self.cost = MENU[name]['cost']
        self.ingredients = MENU[name]['ingredients']


class Menu:

    @staticmethod
    def get_items():
        return f"latte/espresso/cappuccino/"

    @staticmethod
    def find_drink(order_name):
        return MenuItem(order_name)


class CoffeeMaker:

    def __init__(self):
        self.resources = resources

    def report(self):
        print(f"Water: {self.resources['water']}")
        print(f"Milk: {self.resources['milk']}")
        print(f"Coffee: {self.resources['coffee']}")
        print(f"Money: ${profit}")

    def is_resource_sufficient(self, drink):
        """ The MenuItem object to make.
Returns True when the drink order can be made, False if ingredients are insufficient."""
        for k, v in MENU[drink]['ingredients'].items():
            if v > self.resources[k]:
                return False
            else:
                return True

    def make_coffee(self, order: MenuItem):
        """Deducts the required ingredients from the resources"""
        for k, v in order.ingredients.items():
            self.resources[k] -= v


class MoneyMachine(MenuItem):

    def __init__(self, name: str):
        super().__init__(name)

    def make_payment(self, cost: float):
        """Returns True when payment is accepted, or False if insufficient."""
        if cost < self.cost:
            return False

        dollar_in_change = round(cost - self.cost, 2)
        # save self.cost as a profit
        global profit
        profit += self.cost
        print(f"Here is ${dollar_in_change} dollars in change.\n")
        print("Here is your latte. Enjoy!")
        return True


is_on = True
while is_on:
    choice = input(f"What would you like? ({Menu().get_items()}): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        CoffeeMaker().report()

    elif choice not in ("espresso", "latte", "cappuccino",):
        print(f"Please choose {Menu().get_items()}")

    else:
        menu_item = MoneyMachine(choice)
        print(menu_item.name)
        # check resource is sufficient
        is_resource_sufficient = CoffeeMaker().is_resource_sufficient(menu_item.name)
        if is_resource_sufficient:
            print("Please insert your coin:")
            coin = int(input("how many quarters?: ")) * 0.25
            coin += int(input("how many dimes?: ")) * 0.10
            coin += int(input("how many nickles?: ")) * 0.05
            coin += int(input("how many pennies?: ")) * 0.01

            # time to make a coffee
            CoffeeMaker().make_coffee(menu_item)
            # process the coin
            payment_is_ok = menu_item.make_payment(coin)
            if not payment_is_ok:
                print("Sorry that's not enough money. Money refunded")

        else:
            print("Sorry there is not enough water.")

