"""

"""

menu = {
    "meals": {

    },

    "sides": {

    },

    "drinks": {

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

def display_details():
    """ """
    pass

def pick_up_or_delivery():
    """ """
    

def get_details():
    """ """
    name = input("Enter name: ").lower()
    phone_number = get_int("Enter phone number: ")
