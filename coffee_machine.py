water_stock = 400  # mL
milk_stock = 540  # mL
coffee_beans_stock = 120  # grams
disposable_cups = 9  # units
money = 550  # $

material_names = ["water", "milk", "coffee beans", "disposable cups", "money"]
material_units = ["ml", "ml", "grams", "", ""]
material_stock = [water_stock, milk_stock, coffee_beans_stock, disposable_cups, money]

# print("Starting to make a coffee\nGrinding coffee beans\n"
#       "Boiling water\nMixing boiled water with crushed coffee beans\n"
#       "Pouring coffee into the cup\nPouring some milk into the cup\n"
#       "Coffee is ready!")


def machine_status():
    global material_stock
    global material_names
    print("The coffee machine has:")
    for i in range(len(material_stock) - 1):
        print(f"{material_stock[i]} of {material_names[i]}")
    print(f"${material_stock[len(material_stock) - 1]} of {material_names[len(material_stock) - 1]}")
    print("")


def take_money():
    global material_stock
    if material_stock[len(material_stock) - 1] == 0:
        print("I have no money to give, sorry!\n")
    else:
        print(f"I gave you ${money}\n")
        material_stock[len(material_stock) - 1] = 0


def fill_machine():
    global material_stock
    global material_names
    global material_units
    for i in range(len(material_stock) - 1):
        material_stock[i] += abs(int(input(f"Write how many {material_units[i]} "
                                           f"of {material_names[i]} do you want to add:\n").strip()))
    print("")


def coffee_type(option):  # returns list with corresponding materials, if not available returns boolean False
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


def coffee_checker(water_per_cup, milk_per_cup, coffee_beans_per_cup, cost_per_cup, cups):
    # receives a list of materials, returns boolean True or False
    global material_stock
    material_requested = [water_per_cup, milk_per_cup, coffee_beans_per_cup]
    error = []
    error_message = "Sorry, not enough"

    for i in range(len(material_requested)):
        if (material_requested[i] * cups) <= material_stock[i]:
            error.append(True)
        else:
            error.append(False)

    if cups <= disposable_cups:
        error.append(True)
    else:
        error.append(False)

    if all(error):
        return True
    else:
        for i in range(len(error)):
            if not error[i]:
                error_message += " " + material_names[i]

        error_message += "!"
        print(error_message)
        return False


def coffee_maker(water_per_cup, milk_per_cup, coffee_beans_per_cup, cost_per_cup, cups):
    global material_stock
    material_requested = [water_per_cup, milk_per_cup, coffee_beans_per_cup, cups, cost_per_cup]
    print("I have enough resources, making you a coffee!\n")

    for i in range(len(material_stock) - 2):
        material_stock[i] -= material_requested[i]

    material_stock[len(material_stock) - 2] -= material_requested[len(material_stock) - 2]
    material_stock[len(material_stock) - 1] += material_requested[len(material_stock) - 1] * cups


while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n").strip().lower()

    if action == "buy":
        # coffee = int(input("What do you want to buy? 1 - espresso, 2- latte, 3 - cappuccino:\n").strip())
        # coffee_type(coffee)
        coffee = ""
        while coffee != "back":
            coffee = input("What do you want to buy? 1 - espresso, 2- latte, 3 - cappuccino "
                           "(back - to main menu):\n").strip().lower()
            if coffee == "back":
                continue

            mats_requested = coffee_type(coffee)
            if mats_requested is False:
                print("Please introduce a valid coffee type.")
                continue
            else:
                break
        else:
            continue

        have_materials = coffee_checker(*mats_requested)
        if have_materials is True:
            coffee_maker(*mats_requested)

    elif action == "fill":
        fill_machine()

    elif action == "take":
        take_money()

    elif action == "remaining":
        machine_status()

    elif action == "exit":
        break

    else:
        print("Please, introduce a valid action.")

# water_per_cup = 200
# milk_per_cup = 50
# coffee_beans_per_cup = 15


# cups_request = abs(int(input("Write how many cups of coffee you will need:\n")))

# water_request = water_per_cup * cups_request
# milk_request = milk_per_cup * cups_request
# coffee_beans_request = coffee_beans_per_cup * cups_request


# # Calculating cups in stock
# cups_stock = water_stock // water_per_cup
# if (milk_stock // milk_per_cup) < cups_stock:
#     cups_stock = milk_stock // milk_per_cup
# elif (coffe_beans_stock // coffee_beans_per_cup) < cups_stock:
#     cups_stock = coffe_beans_stock // coffee_beans_per_cup


# if cups_request == cups_stock:
#     print("Yes, I can make that amount of coffee")
# elif cups_request < cups_stock:
#     print(f"Yes, I can make that amount of coffee (and even {cups_stock - cups_request} more than that)")
# else:
#     print(f"No, I can make only {cups_stock} cups of coffee ")