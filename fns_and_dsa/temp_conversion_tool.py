# shopping_list_manager.py

def display_menu():
    """Displays the main menu options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Manages the shopping_list, displays the menu, and handles user choices.
    """
    shopping_list = []  # Initialize an empty list named shopping_list

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: ")) # Convert input to int
        except ValueError:
            print("Invalid choice. Please enter a number from the menu.")
            continue # Skip to the next loop iteration

        if choice == 1: # Compare with integer
            # Prompt for and add an item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:  # Ensure item is not empty
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == 2: # Compare with integer
            # Prompt for and remove an item
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")
        elif choice == 3: # Compare with integer
            # Display the shopping list
            if not shopping_list:
                print("The shopping list is currently empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == 4: # Compare with integer
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
