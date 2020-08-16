class CoffeeType:
    cups = 1
    coffee_types = []

    def __init__(self, name, cost, water, coffee, milk=0):
        self.water_per_cup = water
        self.milk_per_cup = milk
        self.coffee_beans_per_cup = coffee
        self.cost_per_cup = cost
        CoffeeType.coffee_types.append(name)

    def materials_request(self, number_of_cups=1):
        water_req = self.water_per_cup * number_of_cups
        milk_req = self.milk_per_cup * number_of_cups
        coffee_beans_req = self.coffee_beans_per_cup * number_of_cups
        cups_req = number_of_cups
        cost_total = self.cost_per_cup * number_of_cups
        return [water_req, coffee_beans_req, milk_req, cups_req, cost_total]


# class CoffeeMaterial:
#     name = ""
#     amount = 0
#     unit = ""
#
#     def __init__(self, material, initial_amount, unit_label):
#         self.name = material
#         self.required_amount = initial_amount
#         self.unit = unit_label
#
#     def __str__(self):
#         return f'{self.name}: {self.amount} {self.unit}'
#
#     def calc_total_materials(self, qty):
#         return qty * self.required_amount
#
#     def can_make_coffee(self, required, qty):
#         return (self.amount // (required * qty)) > 0
#

class CoffeeMachine:
    state = "idle"
    action = None

    def __init__(self, water, coffee_beans, milk, disposable_cups, money):
        self.stock = [water, coffee_beans, milk, disposable_cups, money]
        self.names = ["water", "coffee beans", "milk", "disposable cups", "money"]
        self.units = ["ml", "grams", "ml", "units", "U$D"]

    def main(self):
        print("Hello there!\n")

        while self.state == "idle":
            print("What would you like to do? \n"
                  "1 - Buy coffee \n"
                  "2 - Fill the machine \n"
                  "3 - Take the machine money \n"
                  "4 - See machine stock \n"
                  "5 - Turn off the machine\n")
            self.user_input()

            if self.state == "buy":
                self.buy_interface()

                self.state = "idle"

            elif self.state == "fill":

                print("Filling the machine...")
                self.fill_machine()
                self.remaining_stock()

                self.state = "idle"

            elif self.state == "take":
                print("Taking money from stock...")
                self.take_money()

                self.state = "idle"

            elif self.state == "remaining":
                print("Showing machine stock...")
                self.remaining_stock()

                self.state = "idle"

            elif self.state == "exit":
                print("Bye bye!")
                continue

    def buy_interface(self):
        while self.state == "buy":
            print("Choose a type of coffee:")
            counter = 0
            for coffee in CoffeeType.coffee_types:
                counter += 1
                print(f"{counter} - {coffee}")
            print("")
            self.user_input()
            if self.action is False:
                continue

            if self.check_materials() is False:
                continue

            self.make_coffee()
            print("\n> Back")
            self.user_input(True)

    def user_input(self, stop=False):
        """This process the user input. The input is a numeric keyboard."""
        while True:
            input_str = input().strip()
            if input_str.isnumeric():
                self.action = abs(int(input_str))
                break
        if stop is True:
            return
        if self.state == "idle":
            if self.action == 1:
                self.state = "buy"
            elif self.action == 2:
                self.state = "fill"
            elif self.action == 3:
                self.state = "take"
            elif self.action == 4:
                self.state = "remaining"
            elif self.action == 5:
                self.state = "exit"
            else:
                print("Introduce a valid input.")

        elif self.state == "buy":
            if self.action == 753:
                self.state = "idle"
                self.action = False
            elif self.action == 1:
                self.action = CoffeeType.coffee_types[0]
            elif self.action == 2:
                self.action = CoffeeType.coffee_types[1]
            elif self.action == 3:
                self.action = CoffeeType.coffee_types[2]
            else:
                print("Introduce a valid input.")
                self.action = False

    # def add_material(self, name, amount, unit):
    #     material = CoffeeMaterial(name, amount, unit)
    #     if exists
    #         material.amount += stock.get(name).amount
    #     stock.add(name)

    # def show_stock(self):
    #     stock = {
    #         "water": CoffeeMaterial("water", 200, "ml")
    #     }
    #     for item in stock.values():
    #         print(item)

    def fill_machine(self):
        length = len(self.stock)

        for i in range(length - 1):
            print(f"How much/many {self.units[i]} of {self.names[i]} would you want to add?")
            self.user_input()
            self.stock[i] += self.action
        print("")

    def remaining_stock(self):
        length = len(self.stock)

        for i in range(length):
            print(f"{self.names[i].capitalize()} in machine stock: {self.stock[i]} {self.units[i]}")
        print("\n> Back")
        self.user_input(True)

    def take_money(self):
        money = self.stock[-1]
        if money == 0:
            print("I have no money to give!")
        else:
            print(f"I gave you {self.units[-1]} {money}.")
            self.stock[-1] = 0
        print("\n> Back")
        self.user_input(True)

    def choose_coffee(self):
        if self.action == CoffeeType.coffee_types[0]:
            return espresso.materials_request()
        elif self.action == CoffeeType.coffee_types[1]:
            return latte.materials_request()
        elif self.action == CoffeeType.coffee_types[2]:
            return cappuccino.materials_request()

    def check_materials(self):
        mats_req = self.choose_coffee()
        length = len(mats_req) - 1  # without counting the money
        error = []
        error_message = "Sorry, not enough:"

        for i in range(length - 1):
            if mats_req[i] <= self.stock[i]:
                error.append(True)
            else:
                error.append(False)

        if all(error):
            return True
        else:
            print(error_message)
            for i in range(len(error)):
                if not error[i]:
                    print("-" + self.names[i])
            return False

    def make_coffee(self):
        print("Making coffee...")
        mats_req = self.choose_coffee()
        length = len(mats_req) - 1  # without counting the money
        for i in range(length - 1):
            self.stock[i] -= mats_req[i]
        self.stock[-1] += mats_req[-1]  # adding the money obtained
        print("Done. Enjoy!")


espresso = CoffeeType("Espresso", 4, 250, 16)
latte = CoffeeType("Latte", 7, 350, 20, 75)
cappuccino = CoffeeType("Cappuccino", 6, 200, 12, 200)

coffee_machine = CoffeeMachine(400, 120, 540, 9, 550)
coffee_machine.main()
