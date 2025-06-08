def display_menu():
    """Display the shopping list manager menu options"""
    print("\n=== Shopping List Manager ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("============================")

def main():
    """Main function to manage the shopping list operations"""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        # Add Item
        if choice == '1':
            item = input("Enter the name of the item to add: ").strip()
            if item:
                if item.lower() in [i.lower() for i in shopping_list]:
                    print(f"'{item}' is already in your shopping list.")
                else:
                    shopping_list.append(item)
                    print(f"'{item}' has been added to your shopping list.")
            else:
                print("Error: Item name cannot be empty.")
        
        # Remove Item
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is currently empty.")
                continue
                
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' was not found in your shopping list.")
        
        # View List
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is currently empty.")
            else:
                print("\n=== Your Shopping List ===")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("=========================")
                print(f"Total items: {len(shopping_list)}")
        
        # Exit Program
        elif choice == '4':
            print("\nThank you for using the Shopping List Manager!")
            print("Goodbye!")
            break
        
        # Invalid Choice
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if _name_ == "_main_":
    main()
