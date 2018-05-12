import sys
import datetime
from model.item import Item
from model.event import Event
from model.store import Store


def parse_items_from_file(file_path):
    list = []
    file_data = open(file_path, 'r')

    value = []
    for each_line in file_data:
        each_line = each_line.replace("]", "")
        each_line = each_line.replace("[", "")
        each_line = each_line.replace("\"", "")

        value.append(each_line.strip().split(","))

    for each_data_Array in value:
        size = len(each_data_Array)

        price = float(each_data_Array[2].strip())
        if size == 3:
            new_item = Item(each_data_Array[0], each_data_Array[1], price)
            list.append(new_item)
        elif size == 4:
            date = datetime.datetime.strptime(each_data_Array[3].strip(), "%Y-%m-%d %H:%M:%S.%f").strftime(
                "%Y-%m-%d %H:%M:%S.%f")

            new_event = Event(each_data_Array[0], each_data_Array[1], price, date)
            list.append(new_event)
    file_data.close()
    return list


def print_items_in_store(store):
    for each_item in store.items:
        print(each_item)



def print_items_in_cart(store):
    for each_item in store.get_cart_items():
        print_items_in_store(each_item)


def store_menu(store):
    ready = False

    while not ready:
        menu_dict = {1: "View Items in Store", 2: "View Items in Cart", 3: "Add Item to Cart",
                     4: "Remove Item from Cart",
                     5: "Proceed to Checkout"}
        print("--------------------------------------")
        for key, value in menu_dict.items():
            print(str(key) + ".", end="", flush=True)
            print(value, end="", flush=True)
            print("")
        print("--------------------------------------")
        loop = False
        while not loop:
            try:
                user_input = int(input("\nPlease enter a numerical value corresponding to the menu selection: \n"))
                loop = True

                if user_input == 1:
                    print_items_in_store(store)
                    ready = False
                elif user_input == 2:
                    print_items_in_cart(store)
                    ready = False
                elif user_input == 3:
                    add_item_to_cart()
                    loop = False
                elif user_input == 4:
                    remove_item_from_cart()
                    ready = False
                elif user_input == 5:
                    checkout()
                    ready = True
                else:
                    sys.stderr.write(" Please select between 1 to 5...")
                    loop = False
            except ValueError:
                sys.stderr.write(" Invalid Input...")
                loop = False


def add_item_to_cart():
    print("Add items to cart")


def remove_item_from_cart():
    print("Remove item from cart")


def checkout():
    print("Check Out!")


def main(args=None):
    """The main routine."""

    if (args is None):
        args = sys.argv[1:]
        list = parse_items_from_file("C:/Users/Priya/pythonProjects/PycharmProjects/Shopping_Cart/sample_file.txt")
        store = Store(list)
        store_menu(store)
        print(" ")
        # print_items_in_store(store)


if __name__ == "__main__":
    main()
