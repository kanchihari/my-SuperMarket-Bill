from datetime import datetime

# Function to display the available items
def display_item_list():
    print("Available Items:")
    print(lists)  # It seems like `lists` should be defined somewhere; it's not in the provided code

# Function to get the user's item choice
def get_user_item_choice():
    while True:
        item = input("Enter the item you want to buy: ")
        if item in items:  # `items` is not defined; this will cause an error
            return item
        else:
            print("Invalid item! Please enter a valid item.")

# It would be beneficial to define and initialize 'lists' and 'items' somewhere in the code

