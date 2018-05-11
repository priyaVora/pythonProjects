import sys

def main(args = None):
    """The main routine."""

    if(args is None):
        args = sys.argv[1:]
if __name__== "__main__":
    main()

def parse_items_from_file():
    print("parse items from file")

def print_items_in_store():
    print("Prints items in store")

def print_items_in_cart():
    print("Print items in cart")

def store_menu():
    print("Display store menu options")

def add_item_to_cart():
    print("Add items to cart")

def remove_item_from_cart():
    print("Remove item from cart")

def checkout():
    print("Check Out!")