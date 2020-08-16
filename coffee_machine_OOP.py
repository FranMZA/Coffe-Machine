class CoffeeMachine:
    state = "idle"
    action = None

    def __init__(self, material_names, material_units, material_stock):
        self.material_names = material_names
        self.material_units = material_units
        self.material_stock = material_stock

    def main_interface(self):
        """The main interface of the machine."""
        while self.state == "idle":
            print("Write action (buy, fill, take, remaining, exit):")
            self.user_input("string")
            self.state = self.action

            if self.state == "buy":
                self.action = ""
                while self.action != "back":
                    print("What do you want to buy? 1 - espresso, 2- latte, 3 - cappuccino (back - to main menu):")
                    self.user_input("string")
                    if self.action == "back":
                        continue

                    mats_requested = self.coffee_type()
                    if mats_requested is False:
                        print("Please introduce a valid coffee type.")
                        continue
                    else:
                        break
                else:
                    self.state = "idle"
                    continue

                have_materials = self.coffee_checker(*mats_requested)
                if have_materials is True:
                    self.coffee_maker(*mats_requested)
                self.state = "idle"

            elif self.state == "fill":
                self.fill_machine()
                self.state = "idle"

            elif self.state == "take":
                self.take_money()
                self.state = "idle"

            elif self.state == "remaining":
                self.machine_status()
                self.state = "idle"

            elif self.state == "exit":
                break

            else:
                print("Please, introduce a valid action.")
                self.state = "idle"

    def user_input(self, req_type):
        """Request an user input. Receives only one argument, the type of input desired."""
        if req_type == "number":
            while True:
                input_str = input().strip().lower()
                if input_str.isnumeric():
                    self.action = abs(int(input_str))
                    break
                else:
                    print("Please, introduce a valid number.")
        elif req_type == "string":
            self.action = input().strip().lower()

    def machine_status(self):
        """Prints the stock of every material the machine has.
        Requires no parameter."""
        print("The coffee machine has:")
        length = len(self.material_stock)
        for i in range(length - 1):
            print(f"{self.material_stock[i]} of {self.material_names[i]}")
        print(f"${self.material_stock[length - 1]} of {self.material_names[length - 1]}")
        print("")

    def take_money(self):
        """Allows to retrieve the money from the machine, if there is no money returns an error message."""
        length = len(self.material_stock)
        if self.material_stock[length - 1] == 0:
            print("I have no money to give, sorry!\n")
        else:
            print(f"I gave you ${self.material_stock[length - 1]}\n")
            self.material_stock[length - 1] = 0

    def fill_machine(self):
        """Adds the desired amount of materials to the machine's stock."""
        length = len(self.material_stock)
        for i in range(length - 1):
            print(f"Write how many {self.material_units[i]} of {self.material_names[i]} do you want to add:")
            self.user_input("number")
            self.material_stock[i] += self.action
        print("")

    def coffee_type(self):
        """Returns list with corresponding materials for the requested coffee,
        if not available in stock returns boolean False"""
        option = self.action
        cups = 1
        if option == "1":  # espresso
            water_per_cup = 250
            milk_per_cup = 0
            coffee_beans_per_cup = 16
            cost_per_cup = 4
        elif option == "2":  # latte
            water_per_cup = 350
            milk_per_cup = 75
            coffee_beans_per_cup = 20
            cost_per_cup = 7
        elif option == "3":  # cappuccino
            water_per_cup = 200
            milk_per_cup = 100
            coffee_beans_per_cup = 12
            cost_per_cup = 6
        else:
            return False

        return [water_per_cup, milk_per_cup, coffee_beans_per_cup, cost_per_cup, cups]

    def coffee_checker(self, water_per_cup, milk_per_cup, coffee_beans_per_cup, cost_per_cup, cups):
        """Receives a list of materials requested,
        returns boolean True if there are enough materials or False if there aren't
        enough materials in stock."""
        material_requested = [water_per_cup, milk_per_cup, coffee_beans_per_cup]
        error = []
        error_message = "Sorry, not enough"

        for i in range(len(material_requested)):
            if (material_requested[i] * cups) <= self.material_stock[i]:
                error.append(True)
            else:
                error.append(False)

        if cups <= self.material_stock[len(self.material_stock) - 2]:
            error.append(True)
        else:
            error.append(False)

        if all(error):
            return True
        else:
            for i in range(len(error)):
                if not error[i]:
                    error_message += " " + self.material_names[i]

            error_message += "!"
            print(error_message)
            return False

    def coffee_maker(self, water_per_cup, milk_per_cup, coffee_beans_per_cup, cost_per_cup, cups):
        """\"Makes\" the coffee. Receives a list of materials requested and it takes them
         from stock and adds the money obtained"""
        material_requested = [water_per_cup, milk_per_cup, coffee_beans_per_cup, cups, cost_per_cup]
        print("I have enough resources, making you a coffee!\n")
        length = len(self.material_stock)

        for i in range(length - 2):
            self.material_stock[i] -= material_requested[i]

        self.material_stock[length - 2] -= material_requested[length - 2]
        self.material_stock[length - 1] += material_requested[length - 1] * cups


water_stock = 400  # mL
milk_stock = 540  # mL
coffee_beans_stock = 120  # grams
disposable_cups = 9  # units
money = 550  # $

initial_material_names = ["water", "milk", "coffee beans", "disposable cups", "money"]
initial_material_units = ["ml", "ml", "grams", "", ""]
initial_material_stock = [water_stock, milk_stock, coffee_beans_stock, disposable_cups, money]

coffee_machine = CoffeeMachine(initial_material_names, initial_material_units, initial_material_stock)
coffee_machine.main_interface()
