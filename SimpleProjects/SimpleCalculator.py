operations = {1: "Add", 2: "Subtract", 3: "Multiply", 4: "Divide"}

loop = True
user_selection = ""
while loop == True:
    try:
        for key, values in operations.items():
            print(str(key) + ". " + values)
        user_input = input("Please enter one of the operation types from above: ")

        size = len(operations)

        if int(user_input) > size:
            loop = True
        else:
            user_selection = operations[int(user_input)]
            print("User's Selection: " + user_selection)
            loop = False

    except ValueError:
        print("\nInvalid Input!")


loop2 = True
a_Value = 0
b_Value = 0
while loop2 == True:

    try:
        a = input("Please enter the first number: ")
        b = input("Please enter the second number: ")

        a_Value = int(a)
        b_Value = int(b)

        c = ""
        loop2 = False
    except ValueError:
        print("\nInvalid Input Error!")
        loop2 = True

if user_selection == "Add":
    c = a_Value + b_Value
    loop2 = False
elif user_selection == "Subtract":
    c = a_Value - b_Value
    loop2 = False
elif user_selection == "Multiply":
    c = a_Value * b_Value
    loop2 = False
elif user_selection == "Divide":
    c = a_Value / b_Value
    loop2 = False
result = float(c)
print("\tResult: " + str(result))
