def display_menu():
    """Display the main menu options"""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list"""
    shopping_list = []  # Initialize empty shopping list
    
    while True:
        display_menu()  # Display menu options
        choice = input("\nEnter your choice (1-4): ")  # Get user input
        
        # Add Item
        if choice == '1':
            item = input("Enter item to add: ").strip()
            if item:  # Only add if not empty string
                shopping_list.append(item)
                print(f"'{item}' added to your shopping list.")
            else:
                print("Item cannot be empty!")
        
        # Remove Item
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is empty!")
                continue
                
            print("Current items:", ', '.join(shopping_list))
            item = input("Enter item to remove: ").strip()
            
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")
        
        # View List
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty!")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        
        # Exit Program
        elif choice == '4':
            print("Goodbye!")
            break
        
        # Invalid Choice
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if _name_ == "_main_":
    main()
