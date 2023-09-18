from datetime import datetime

# Function to display the available items
def display_item_list():
    print("Available Items:")
    print(lists)  

# Function to get the user's item choice
def get_user_item_choice():
    while True:
        item = input("Enter the item you want to buy: ")
        if item in items: 
            return item
        else:
            print("Invalid item! Please enter a valid item.")
# Function to get the user's desired quantity for the item
def get_user_item_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity you want to buy: "))  
            if quantity > 0:  
                return quantity
            else:
                print("Invalid quantity! Please enter a valid quantity.")  
        except ValueError:
            print("Invalid input! Please enter a valid numeric quantity.")  




