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

    "sides": {
        "side_1" : {"item_name": "Garlic Bread", "price": 4.99},
        "side_2" : {"item_name": "Onion Rings", "price": 6.49},
        "side_3" : {"item_name": "Crinkle Cut Fries", "price": 5.49},
        "side_4" : {"item_name": "Chicken Wings", "flavors": ["Buffalo", "BBQ", "Peri Peri"],"price": {"5pc": 9.99, "8pc": 14.99, "16pc": 27.99}},
        "side_5" : {"item_name": "Chicken Tenders","flavors": ["Buffalo", "BBQ", "Peri Peri"], "price": {"5pc": 9.99, "8pc": 14.99, "16pc": 27.99}}
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

def pick_up_or_delivery():
    """Ask the user whether they are going to pick-up the order or have it delivered"""
    choice = 0
    while choice not in [1, 2]:
        choice = get_int("1. Pick up  2. Delivery" 
        "\n>")

    return choice

def get_details():
    """Get the user to enter their name, phone number, and address if they have chosen the deliver option"""
    details = {"name": "", "phone_number": ""}
    name = input("Enter name: ").lower()
    phone_number = get_int("Enter phone number: ")
    if pick_up_or_delivery() == 2:
        address = input("Enter Address: ")
        details["address"] = address
    details["name"] = name
    details["phone_number"] = phone_number

    return details

def display_details(details):
    """ """
    for detail in details:
        print(f"{detail}: {details[detail]} ")

display_details(get_details())