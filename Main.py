### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if ingredient not in self.machine_resources or self.machine_resources[ingredient] < quantity:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 0
        coins = {
            "large dollars": 1,
            "half dollars": 0.5,
            "quarters": 0.25,
            "nickels": 0.05
        }
        for coin, value in coins.items():
            num_coins = int(input(f"How many {coin}?: "))
            total += num_coins * value
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        else:
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


# Make an instance of SandwichMachine class
sandwich_machine = SandwichMachine(resources)

# Main loop for interaction
while True:
    choice = input("What would you like? (small/medium/large/off/report): ").lower()

    if choice == "off":
        print("Turning off the machine.")
        break
    elif choice == "report":
        print("Current resources:")
        for item, quantity in sandwich_machine.machine_resources.items():
            print(f"{item.capitalize()}: {quantity}")
    elif choice in recipes.keys():
        size = choice
        if sandwich_machine.check_resources(recipes[size]["ingredients"]):
            print("Please insert coins.")
            cost = recipes[size]["cost"]
            coins_inserted = sandwich_machine.process_coins()
            if coins_inserted:
                transaction_success = sandwich_machine.transaction_result(coins_inserted, cost)
                if transaction_success:
                    sandwich_machine.make_sandwich(size, recipes[size]["ingredients"])
    else:
        print("Invalid choice. Please choose again.")