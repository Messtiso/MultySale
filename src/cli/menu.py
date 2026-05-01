from services.item_service import add_item, get_all_items

def show_menu():
    while True:
        print("\n=== MultySell ===")
        print("1. Add new item")
        print("2. View inventory")
        print("3. Update listing status")
        print("4. Mark item as sold")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Title: ")
            brand = input("Brand: ")
            category = input("Category: ")
            size = input("Size: ")
            condition = input("Condition: ")
            colour = input("Colour: ")
            price = float(input("Price: "))
            photo_path = input("Photo folder path: ")

            add_item(title, brand, category, size, condition, colour, price, photo_path)

            print("Item added successfully!")

        elif choice == "2":
            items = get_all_items()

            if len(items) == 0:
                print("No items were found.")
            else:
                for item in items:
                    print(f"\nID: {item[0]}")
                    print(f"Title: {item[1]}")
                    print(f"Brand: {item[2]}")
                    print(f"Category: {item[3]}")
                    print(f"Size: {item[4]}")
                    print(f"Condition: {item[5]}")
                    print(f"Colour: {item[6]}")
                    print(f"Price: {item[7]}")
                    print(f"Photo path: {item[8]}")
                    print(f"Status: {item[9]}")
                    
        elif choice == "3":
            print("Update listing status selected")
        elif choice == "4":
            print("Mark item as sold selected")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again")