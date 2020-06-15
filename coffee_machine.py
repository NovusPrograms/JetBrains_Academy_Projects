class CoffeeMachine(object):
    coffee_draw = "\n ((" \
                  "\n  ))" \
                  "\n |~~|" \
                  "\nc|__| Hot coffee for you!"

    display_action = "\nWrite action (buy, fill, take, remaining, exit):"
    ingredients = ("water", "milk", "coffee beans", "cups", "money")
    units = ("ml of", "ml of", "grams of", "disposable")
    espresso = (-250, 0, -16, -1, +4)
    latte = (-350, -75, -20, -1, +7)
    cappuccino = (-200, -100, -12, -1, +6)
    coffee_dict = {
        "1": espresso,
        "2": latte,
        "3": cappuccino}

    def __init__(self):
        self.supplies = [400, 540, 120, 9, 550]

    def __str__(self):
        message = "The coffee machine has:"
        for ingredient_number in range(4):
            message += "\n\t{} {} {}"\
                .format(self.supplies[ingredient_number],
                        self.units[ingredient_number],
                        self.ingredients[ingredient_number])
        message += "\n\t${} of money".format(self.supplies[4])
        return message

    def handle(self, command=None):
        if command.lower() == "remaining":
            print(self)
        elif command.lower() == "take":
            self.take()
        elif command.lower() == "fill":
            self.fill()
        elif command.lower() == "buy":
            self.buy()
        else:
            print("I don't understand, repeat your action.")
        print(self.display_action)

    def take(self):
        print(f"I gave you ${self.supplies[4]}")
        self.supplies[4] = 0

    def fill(self):
        for ingredient_number in range(4):
            print("Write how many {} {} do you want to add:"
                  .format(self.units[ingredient_number],
                          self.ingredients[ingredient_number]))
            self.supplies[ingredient_number] += int(input(prompt))

    def buy(self):
        print("What do you want to buy? 1 -espresso, 2 - latte, 3 cappuccino, back - to main menu:")
        type_of_coffee = input(prompt)
        if type_of_coffee == "1" or type_of_coffee == "2" or type_of_coffee == "3":  # Select your Coffee
            if self.check_supply(self.coffee_dict[type_of_coffee]):  # Check if there is enough supplies
                for ingredient_number in range(5):  # Change value of available supplies
                    self.supplies[ingredient_number] += self.coffee_dict[type_of_coffee][ingredient_number]
                print("I have enough resources, making you a coffee!\n", self.coffee_draw)
            return
        elif type_of_coffee.lower() == "back":
            return
        else:
            print("Wrong choice.\n")
            self.buy()

    def check_supply(self, coffee_name):
        coffee_possible = True
        # For every ingredient check if there is enough supplies,
        # If not, respond proper answer and set there is no way to do a coffee (coffee_possible = False).
        for ingredient_number in range(4):
            if self.supplies[ingredient_number] + coffee_name[ingredient_number] < 0:
                coffee_possible = False
                print(f"Sorry, not enough {self.ingredients[ingredient_number]}!")
            return coffee_possible
        return coffee_possible

prompt = "> "
my_machine = CoffeeMachine()
user_input = ""

while user_input.lower() != "exit":
    my_machine.handle(user_input)
    user_input = input(prompt)
