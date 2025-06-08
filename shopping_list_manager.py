shopping_list = []

def display_menu():
    print("1. Add item\n2. Remove item\n3. View list\n4. Exit")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-4): "))
        # Implement logic based on choice

if _name_ == "_main_":
    main()
