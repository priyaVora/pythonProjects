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
        print(each_item)


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


def add_item_to_cart(store):
    count = 1
    item_dict = {}
    for each_item in store.items:
        print(str(count) + ".", end= "", flush=True)
        print(str(each_item)+ ".", end="", flush=True)
        item_dict[count] = each_item
        print("")
        count = count + 1
    loop = False
    while not loop:
        try:
            user_input = int(input("\nPlease enter a numerical value corresponding to the menu selection: \n"))

            size = len(store.items)

            if user_input <= size:
                adding_item = item_dict[user_input]

                loop = True

                second_loop = False
                while not second_loop:
                    try:
                        second_input = int(input("\nPlease enter quantity of item: " + str(user_input)))
                        store.add_cart(adding_item, second_input)
                        second_loop = True
                       # print_items_in_cart(store)
                       # store.add_cart(adding_item, 5)
                        #print_items_in_cart(store)

                        #print(store.get_cart_item_quantity(adding_item))
                    except ValueError:
                        second_loop = False
            else:
                loop = False

        except ValueError:
            sys.stderr.write(" Invalid Input...")
            loop = False


def remove_item_from_cart(store):
    count = 1
    item_dict = {}
    for each_item in store.items:
        print(str(count) + ".", end="", flush=True)
        print(str(each_item) + ".", end="", flush=True)
        item_dict[count] = each_item
        print("")
        count = count + 1
    loop = False
    while not loop:
        try:
            user_input = int(input("\nPlease enter a numerical value corresponding to the menu selection: \n"))
            loop = True
            size = len(store.items)

            if user_input <= size:
                removing_item = item_dict[user_input]
                print("Item is : ")
                print(removing_item)
                loop = True

                second_loop = False
                while not second_loop:
                    try:
                        second_input = int(input("\n Enter a quantity (or to type 0 for “all”) to remove " + str(user_input)))
                        store.remove_from_cart(removing_item, int(user_input))
                        second_loop = True
                    except ValueError:
                        second_loop = False
            else:
                print("")
                loop = False

        except ValueError:
            sys.stderr.write(" Invalid Input...")
            loop = False


def checkout(store):
    count = 1
    print("Items for checkout: \n")
    for each_item_in_cart in store.get_cart_items():
        print(str(count) + ".", end="", flush="")
        print(each_item_in_cart)
        print("")


def main(args=None):
    """The main routine."""

    if (args is None):
        args = sys.argv[1:]
        list = parse_items_from_file("C:/Users/Priya/pythonProjects/PycharmProjects/Shopping_Cart/sample_file.txt")
        store = Store(list)

        print_items_in_store(store)




if __name__ == "__main__":
    main()
