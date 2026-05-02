from services.item_service import add_item, get_all_items, update_item_status, mark_item_as_sold, update_item_field

def show_menu():
    while True:
        print("\n=== MultySell ===")
        print("1. Add new item")
        print("2. View inventory")
        print("3. Update listing status")
        print("4. Edit item")
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

                    if item[9] == "sold":
                        print(f"Sold price: £{item[10]}")
                        print(f"Sold platform: {item[11]}")

                    
        elif choice == "3":
            item_id = input("Enter item ID: ")

            print("\nChoose status:")
            print("0. Back")
            print("1. Not listed")
            print("2. Listed")
            print("4. Sold")

            status_choice = input("Select status: ")

            if status_choice == "0":
                continue

            elif status_choice == "1":
                update_item_field(item_id, "status", "not listed")
                update_item_field(item_id, "listed_platforms", None)
                print('Item set to "Not listed".')

            elif status_choice == "2":
                platforms = input("Enter platform(s) (e.g. Vinted, Depop): ")
                update_item_field(item_id, "status", "listed")
                update_item_field(item_id, "listed_platforms", platforms)
                print('Item set to "Listed".')

            elif status_choice == "3":
                sold_platform = float(input("Sold price: £"))
                sold_platform = input("Platform sold on: ")

                update_item_field(item_id, "status", "sold")
                update_item_field(item_id, "sold_price", sold_price)
                update_item_field(item_id, "sold_platform", sold_platform)

                print('Item set to "Sold".')

            else:
                print("Invalid option")
        

        elif choice == "4":
            item_id = input("Enter item ID to edit: ")

            while True:
                print("\nWhat do you want to edit?")
                print("1. Title")
                print("2. Brand")
                print("3. Category")
                print("4. Size")
                print("5. Condition")
                print("6. Colour")
                print("7. Price")
                print("8. Photo path")
                print("9. Status")

                field_choice = input("Select field: ")

                fields = {
                    "1": "title",
                    "2": "brand",
                    "3": "category",
                    "4": "size",
                    "5": "condition",
                    "6": "colour",
                    "7": "price",
                    "8": "photo_path",
                    "9": "status"
                }

                if field_choice not in fields:
                    print("Invalid field selected.")
                    continue
                
                field_name = fields[field_choice]

                if field_name == "status":
                    print("\nChoose a new status: ")
                    print("1. Not listed")
                    print("2. Listed on Vinted")
                    print("3. Listed on Depop")
                    print("4. Listed on Vinted and Depop")
                    print("5. Sold")

                    status_choice = input("Select status: ")

                    statuses = {
                        "1": "not listed",
                        "2": "listed on Vinted",
                        "3": "listed on Depop",
                        "4": "listed on Vinted and Depop",
                        "5": "sold",
                    }

                    if status_choice not in statuses:
                        print("Invalid status selected.")
                        continue
                    
                    new_value = statuses[status_choice]

                else:
                    new_value = input("Enter new Value: ")

                    if field_name == "price":
                        new_value = float(new_value)
                
                update_item_field(item_id, field_name, new_value)

                print("Item updated successfully!")

                again = input("Edit another field? (y/n): ").lower()
                if again != "y":
                    break

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again")