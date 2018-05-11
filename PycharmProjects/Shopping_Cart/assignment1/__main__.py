import sys
import datetime
from model.item import Item
from model.event import Event


def parse_items_from_file(file_path):
    list= []
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
            date = datetime.datetime.strptime(each_data_Array[3].strip(), "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d %H:%M:%S.%f")

            new_event = Event(each_data_Array[0], each_data_Array[1], price, date)
            list.append(new_event)
    file_data.close()
    return list


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

def main(args = None):
    """The main routine."""

    if(args is None):
        args = sys.argv[1:]
        list = parse_items_from_file("C:/Users/Priya/pythonProjects/PycharmProjects/Shopping_Cart/sample_file.txt")
        for each_item in list:
            print(each_item)
if __name__== "__main__":
    main()

