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

# Main program starts here
print("------------------------ Welcome to SuperMarket --------------------------------")

# Prompt the user for their name
name = input("Enter Your name: ")

# List of items along with their prices in euros per unit or per kilogram/liter
lists = '''
1. Apples - 1.50 €/- per kg
2. Rice - 4.00 €/- per kg
3. Milk - 2.00 €/- per liter
4. Oil - 2.39 €/- per liter
5. Meat - 14.00 €/- per kg
6. Cola - 1.90 €/- per liter
7. Wine - 2.50 €/- 500ml
8. Curd - 1.40 €/- 500ml
9. Atta - 5.00 €/- per kg
10. Bread - 3.00 €/- per loaf
'''

# Dictionary to store item names and their respective prices in euros
items = {
    'Apple': 1.50,
    'Rice': 4.00,
    'Milk': 2.00,
    'Oil': 2.39,
    'Meat': 14.00,
    'Cola': 1.90,
    'Wine': 2.50,
    'Curd': 1.40,
    'Atta': 5.00,
    'Bread': 3.00
}

total_price = 0
pricelist = []
itemList = []
quanList = []
priceList = []

option = int(input("To view the list of items, press 1: "))

# Check if the user selected option 1 to view the list of items
if option == 1:
    display_item_list()  # Call the function to display the item list

# Initialize 'buying' to False
buying = False

while True:
    print("Select an option:")
    print("1. Buy items")
    print("2. Exit")
    input1 = int(input())
    # Check if the user selected option 2 to exit the loop
    if input1 == 2:
        break  # Exit the loop and terminate the program
    # if the user selected option 1 that is to buy items.
    elif input1 == 1:
        buying = True
        item = get_user_item_choice() 

        quantity = get_user_item_quantity() 
        price = quantity * items[item]  
        pricelist.append((item, quantity, items[item], price)) 
        total_price += price  
        itemList.append(item)  
        quanList.append(quantity)  
        priceList.append(price)

