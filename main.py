"""

"""

menu = {
    "pizzas": {
        "pizza_1": {"item_name": "Pepperoni", "vegan": False, "price": {"large": 7.49, "extra_large": 11.48}},
        "pizza_2": {"item_name": "Classic Cheese", "vegan": False, "price": {"large": 6.99, "extra_large": 10.98}},
        "pizza_3": {"item_name": "Ham and Cheese ", "vegan": False, "price": {"large": 6.49, "extra_large": 10.48}},
        "pizza_4": {"item_name": "Meat Lovers", "vegan": False, "price": {"large": 12.99, "extra_large": 17.48}},
        "pizza_5": {"item_name": "Mega Meat Lovers", "vegan": False, "price": {"large": 18.49, "extra_large": 23.48}},
        "pizza_6": {"item_name": "Peri Peri Chicken", "vegan": False, "price": {"large": 17.99, "extra_large": 22.98}},
        "pizza_7": {"item_name": "Buffalo Chicken", "vegan": False, "price": {"large": 15.99, "extra_large": 20.98}},
        "pizza_8": {"item_name": "Classic Veggie", "vegan": True, "price": {"large": 7.99, "extra_large": 11.98}},
        "pizza_9": {"item_name": "Veggie Lovers", "vegan": True, "price": {"large": 12.49, "extra_large": 17.48}},
        "pizza_10": {"item_name": "Hot and Spicy Veggie", "vegan": True, "price": {"large": 10.99, "extra_large": 15.48}}
    },

    "drinks": {
        "drink_1" : {"item_name": "Coca Cola", "price": {"1.5L": 4.99, "600ml": 3.99, "330ml Can": 2.99}},
        "drink_2" : {"item_name": "Coca Cola Zero Sugar", "price": {"1.5L": 4.99, "600ml": 3.99, "330ml Can": 2.99}},
        "drink_3" : {"item_name": "Sprite", "price": {"1.5L": 4.99, "600ml": 3.99, "330ml Can": 2.99}},
        "drink_4" : {"item_name": "Sprite Zero Sugar", "price": {"1.5L": 4.99, "600ml": 3.99, "330ml Can": 2.99}},
        "drink_5" : {"item_name": "Water", "price": {"1.5L": 4.99, "750ml": 3.99}},
        "drink_6" : {"item_name": "Apple Juice", "price": {"750ml": 6.49, "350ml": 4.99}}
    }
}

DELIVERY_CHARGE = 10

def get_int(prompt):
    """Validates user input. Negative numbers are unnecessary for this program so it also checks fro positive integers."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Must be a positive integer")
            else:
                return value
        except:
            print("Must be an integer")

def display_choices():
    """Display the actions the user can do"""
    print("\n1. Pizzas" \
    "\n2. Drinks" \
    "\n3. Checkout" \
    "\n4. Exit")

def display_pizza():
    """Display the pizzas"""
    print(f"{" PIZZA MENU ":=^50}")
    print(f"{"Pizza":<25} | {"Large":>15} | {"Extra Large":>15} | {"Dietary":>15}")
    print("-"*50)
    for item in menu['pizzas'].values():
        vegan_tag = "Vegan" if item['vegan'] else "Non-vegan"
        print(f"{item['item_name']:<25} | ${item['price']['large']:>15} | ${item['price']['extra_large']:>15} | {vegan_tag:>15}")

def display_drinks():
    """Display the drinks"""
    print(f"{"Drinks":=^50}")
    for items in menu['drinks'].values():
        print(items['item_name'])
        for size, price in items['price'].items():
            print(f"  {size:<5}  ${price:>5}")

def order_pizza():
    """Take the user's pizza orders"""
    while True:
        display_pizza()
        print("Type the name of the pizza you want or type 'B' to go back")
        user_input = input("> ").strip().lower()

        if user_input == 'b':
            break

        pizza_found = False
        pizza_details = {}

        # compared the user's input to the pizzas in the dictionary
        for item in menu['pizzas'].values():
            if user_input == item['item_name'].lower():
                pizza_found = True
                price = item['price'].items()
                pizza_name = item['item_name']
                pizza_details = item


        if pizza_found == True:
            print(f"You have selected: {pizza_name}")
            while True:
                print("Choose size: (1. Large or 2. Extra Large)")
                size = get_int("> ")
                match size:
                    case 1:
                        print(f"You have ordered a large {pizza_name}")
                        size = "Large"
                        price = pizza_details['price']['large']
                        break
                    case 2:
                        print(f"You have ordered an extra large {pizza_name}")
                        size = "Extra Large"
                        price = pizza_details['price']['extra_large']
                        break
                    case _:
                        print("Choose a valid option")

    pizza_order = [pizza_details['item_name'], size, price]
    return pizza_order


def pick_up_or_delivery():
    """Ask the user whether they are going to pick-up the order or have it delivered"""
    choice = 0
    while choice not in [1, 2]:
        choice = get_int("1. Pick up  2. Delivery" 
        "\n> ")

        if choice not in [1, 2]:
            print("Choose a valid option")

    return choice

def get_details():
    """Get the user to enter their name, phone number, and address if they have chosen the deliver option"""
    details = {"Name": "", "Phone Number": ""}
    name = input("Enter name: ")
    phone_number = get_int("Enter phone number: ")
    if pick_up_or_delivery() == 2:
        address = input("Enter Address: ")
        details["address"] = address
    details["Name"] = name
    details["Phone Number"] = phone_number

    return details

def checkout():
    """ """
    pass

def display_details(details):
    """Display the user details"""
    for detail in details:
        print(f"{detail}: {details[detail]} ")

def main():
    while True:
        display_choices()

        choice = get_int("Enter action:"
        "\n> ")
        match choice:
            case 1:
                print(order_pizza())
            case 2:
                display_drinks()
            case 3:
                checkout()
            case 4:
                return
            case _:
                print("Choose one of the options")

main()