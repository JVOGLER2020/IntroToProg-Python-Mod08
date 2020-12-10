# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <JVogler>,<Dec 7 2020>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
import os.path
# adjust filepath here
file_path = 'C:\\Users\\VoglerJ\\Documents\\U WASHINGTON PYTHON\\_PythonClass\\Assignment08'
# adjust .txt filename
name_of_file = 'products.txt'

strFileName = os.path.join(file_path, name_of_file)
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #
    product_name = ""
    product_price = 0

# Processing  ------------------------------------------------------------- #
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price

class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #
    @staticmethod
    def save_data_to_file():
        file = open(strFileName, 'w')
        for row in lstOfProductObjects:
            file.write(row.product_name + ',' + row.product_price + '\n')
        file.close()

    @staticmethod
    def read_data_from_file():
        file = open(strFileName, 'r')
        for row in file:
            name, price = row.split(",")
            product = Product(name.strip(), price.strip())
            lstOfProductObjects.append(product)
        file.close()


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass
    # TODO: Add code to show menu to user
    # TODO: Add code to get user's choice
    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user

# Presentation (Input/Output)  -------------------------------------------- #
    @staticmethod
    def display_menu():
        print("")
        print("Please choose number from the following options:")
        print("(1) Show current data.")
        print("(2) Add new product to list.")
        print("(3) Save file.")
        print("(4) Exit Program.")
        print("---------------------------------------------")

    @staticmethod
    def user_input():
        count = 0

        while (True):
            choice = input("Enter a number between 1 - 4: ")
            count = count + 1
            try:
                choice = int(choice)
                if ((choice > 0) & (choice < 5)):
                    return choice
                else:
                    print(str(choice) + " is not valid.  Select 1 - 4")
                    if count > 2:
                        IO.display_menu()
                        count = 0
            except:
                print(str(choice) + " is not valid.  Select 1 - 4")
                if count > 2:
                    IO.display_menu()
                    count = 0

    @staticmethod
    def display_data():
        for product in lstOfProductObjects:
            print(product.product_name + "," + product.product_price)

    @staticmethod
    def add_product():
        name = input("Enter name of product to add: ")
        price = input("Enter name of price for product: ")
        product = Product(name, price)

        lstOfProductObjects.append(product)

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

FileProcessor.read_data_from_file()
while (True):
    IO.display_menu()
    choice = IO.user_input()
    if choice == 1:
        IO.display_data()
    elif choice == 2:
        IO.add_product()
    elif choice == 3:
        FileProcessor.save_data_to_file()
    elif choice == 4:
        break

# Main Body of Script  ---------------------------------------------------- #

