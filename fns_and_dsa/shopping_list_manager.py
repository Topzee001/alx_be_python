def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            #prompt for and add an item
            item = input("Enter the name of your item: ")
            shopping_list.append(item)
            # pass
        elif choice == "2":
            # Prompt for and remove an item
            remove_item = input("Enter item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} removed")
            else: print("item not found!!!\n")
            # pass
        elif choice == '3':
            # Display the shopping list
            print("Menu Items", shopping_list)
            # pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": main()