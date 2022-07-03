# creating a calculator

banner = """
|===========================
|Please select an operation|
|Addition-1                |
|Subtraction-2             |
|Multiply-3                | 
|Divison-4                 |
============================


"""

print(banner)

num1 = float(input("Enter a number:-"))
num2 = float(input("Enter another number:-"))

operation = float(input("Choose an operation:-"))

# operations
add = num1 + num2
sub = num1 - num2
multiply = num1 * num2
divison = num1 / num2

# using while and if else


while True:

    if operation == 1:
        print("The sum is" + " " + str(add))
    elif operation == 2:
        print("Difference is" + " " + str(sub))
    elif operation == 3:
        print("Product is" + " " + str(multiply))
    elif operation == 4:
        print("The divison is" + " " + str(divison))

    again = input("Do you want to do it again(yes/no)")

    if again == "no":
        break
    else:
        # creating a calculator

        banner = """
        |===========================
        |Please select an operation|
        |Addition-1                |
        |Subtraction-2             |
        |Multiply-3                | 
        |Divison-4                 |
        ============================


        """

        print(banner)

        num1 = float(input("Enter a number:-"))
        num2 = float(input("Enter another number:-"))

        operation = float(input("Choose an operation:-"))

        # operations
        add = num1 + num2
        sub = num1 - num2
        multiply = num1 * num2
        divison = num1 / num2

        # using while and if else

        while True:

            if operation == 1:
                print("The sum is" + " " + str(add))
            elif operation == 2:
                print("Difference is" + " " + str(sub))
            elif operation == 3:
                print("Product is" + " " + str(multiply))
            elif operation == 4:
                print("The divison is" + " " + str(divison))

            again = input("Do you want to do it again(yes/no)")

            if again == no:
                break

        else:
                print("Invalid")
