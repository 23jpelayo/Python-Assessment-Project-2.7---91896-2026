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
        "drink_1" : {"item_name": "Coca Cola", "price": {"1.5L": 4.99, "330ml Can": 2.99}},
        "drink_2" : {"item_name": "Coca Cola Zero Sugar", "price": {"1.5L": 4.99, "330ml Can": 2.99}},
        "drink_3" : {"item_name": "Sprite", "price": {"1.5L": 4.99, "330ml Can": 2.99}},
        "drink_4" : {"item_name": "Sprite Zero Sugar", "price": {"1.5L": 4.99, "330ml Can": 2.99}},
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
    print(f"{" PIZZA MENU ":=^100}")
    print(f"{"Pizza":<25} | {"Large":>15} | {"Extra Large":>15} | {"Dietary":>15}")
    print("-"*50)
    for item in menu['pizzas'].values():
        if item['vegan'] == True:
            vegan_tag = "Vegan"
        else:
            vegan_tag = "Non-vegan"
        print(f"{item['item_name']:<25} | ${item['price']['large']:>15.2f} | ${item['price']['extra_large']:>15.2f} | {vegan_tag:>15}")

def display_drinks():
    """Display the drinks"""
    print(f"{" DRINKS ":=^100}")
    for items in menu['drinks'].values():
        print(items['item_name'])
        for size, price in items['price'].items():
            print(f"  {size:<5}  ${price:>5.2f}")

def order_pizza():
    """Take the user's pizza orders"""
    while True:
        display_pizza()
        print("Type the name of the pizza you want or type 'B' to go back")
        user_input = input("> ").strip().lower().replace(" ", "")

        if user_input == 'b':
            return

        pizza_found = False
        pizza_details = {}

        # compare the user's input to the pizzas in the dictionary
        for item in menu['pizzas'].values():
            if user_input == item['item_name'].strip().lower().replace(" ", ""):
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
        
        else:
            print("Invalid name. Please check your spelling")


def order_drinks():
    """Take the user's drink orders"""
    while True:
        display_drinks()
        print("Type the name of the drink you want or type 'b' to go back")
        user_input = input("> ").strip().lower().replace(" ", "")

        if user_input == 'b':
            return

        drink_found = False
        drink_details = {}
        size = []

        # compare the user's input to the drinks in the dictionary
        for item in menu["drinks"].values():
            if user_input == item['item_name'].strip().lower().replace(" ", ""):
                drink_found = True
                drink_name = item['item_name']
                drink_details = item
                price = item['price'].items()
                for num in price:
                    size.append(num[0])

        if drink_found == True:
            print(f"You have selected {drink_name}")
            while True:
                print(f"Choose size: 1. {size[0]} 2. {size[1]}")
                chosen_size = get_int("> ")
                match chosen_size:
                    case 1:
                        print(f"You have ordered a {size[0]} {drink_name}")
                        drink_size = size[0]
                        price = drink_details['price'][size[0]]
                        break
                    case 2:
                        print(f"You have ordered a {size[1]} {drink_name}")
                        drink_size = size[1]
                        price = drink_details['price'][size[1]]
                        break
                    case _:
                        print("Choose a valid size")

            drink_order = [drink_details['item_name'], drink_size, price]
            return drink_order
        else:
            print("Invalid name. Please check your spelling")



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
    details = {"Name": "", "Phone Number": "", "Service": ""}
    choice = pick_up_or_delivery()
    name = input("Enter name: ")
    phone_number = get_int("Enter phone number: ")
    if choice == 2:
        address = input("Enter Address: ")
        details['address'] = address
        details['Service'] = "Delivery"
    else:
        details['Service'] = "Pick-up"
    details['Name'] = name
    details['Phone Number'] = phone_number

    return details

def checkout(items):
    """Display the items the user has ordered and show the individual prices and the total price"""
    while True:
        if len(items) > 0:

            total = 0
            print(f"{" CART ":=^65}")
            print(f"{"Item":<25} | {"Size":>15} | {"Price":>15}")
            for item in items:
                print(f"{item[0]:<25} | {item[1]:>15} | ${item[2]:>15.2f}")
                total += item[2]

            print(f"{"Total":<25} | {"":>15} | {total:>15.2f}")

            print("What would you like to do?"\
            "\n1. Confirm and Checkout" \
            "\n2. Remove item" \
            "\n3. Cancel order"
            "\n4. Go back")

            while True:
                choice = get_int("> ")
                match choice:
                    case 1:
                        customer_details = get_details()
                        if customer_details['Service'] == "Delivery":
                            print(f"\nDelivery Charge: ${DELIVERY_CHARGE}")
                            total += DELIVERY_CHARGE

                        print(f"Total Cost: ${total:.2f}")
                        print("Order Confirmed. Thank you for shopping")
                        print("\nWould you like to make another order?" \
                        "\nType '1' to order again or type '2' to exit")
                        while True:
                            user_choice = get_int("> ")
                            match user_choice:
                                case 1:
                                    items.clear()
                                    return
                                case 2:
                                    exit()
                                case _:
                                    print('Choose a valid option')

                    case 2:
                        print("Enter the name of the item you want to remove or type 'b' to cancel")
                        remove_item_name = input("> ").strip().lower().replace(" ", "")
                        if remove_item_name == 'b':
                            return
                        
                        item_to_remove = ""
                        
                        for item in items:
                            if item[0].strip().lower().replace(" ", "") == remove_item_name:
                                item_to_remove = item
                                break

                            
                        if item_to_remove != "":
                            items.remove(item_to_remove)
                            print(f"Successfully removed {item_to_remove[0]}")
                        else:
                            print("Item not found. Please check your spelling")

                        break

                    case 3:
                        print("Type 'c' to confirm cancellation or 'b' to go back")
                        confirmation = input("> ").strip().lower()
                        if confirmation == 'c':
                            items.clear()
                            print("Order cancelled")
                            exit()
                        elif confirmation == 'b':
                            return

                    case 4:
                        print("Returning to menu")
                        return

                    case _:
                        print("Choose one of the options")
                        


        else:
            print("You have not ordered anything yet")
            return

def display_details(details):
    """Display the user details"""
    for detail in details:
        print(f"{detail}: {details[detail]} ")

def main():
    order = []
    while True:
        display_choices()

        choice = get_int("Enter action:"
        "\n> ")
        match choice:
            case 1:
                result = order_pizza()
                if result is not None:
                    order.append(result)
            case 2:
                result = order_drinks()
                if result is not None:
                    order.append(result)
            case 3:
                checkout(order)
            case 4:
                print("Exit successful")
                return #end the program
            case _:
                print("Choose one of the options")

main()