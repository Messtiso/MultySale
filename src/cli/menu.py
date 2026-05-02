from services.item_service import add_item, get_all_items, update_item_status, mark_item_as_sold, update_item_field, get_item_by_id, delete_item

def get_input(prompt):
    value = input(prompt)

    if value == "0":
        return None

    return value

def show_menu():
    while True:
        print("\n=== MultySell ===")
        print("1. Add new item")
        print("2. View inventory")
        print("3. Update listing status")
        print("4. Edit item")
        print("5. Remove item")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            title = get_input("Title (0 to go back): ")
            if title is None:
                continue
        
            brand = get_input("Brand (0 to go back): ")
            if brand is None:
                continue
            
            category = get_input("Category (0 to go back): ")
            if category is None:
                continue
            
            
            size = get_input("Size (0 to go back): ")
            if size is None:
                continue
            
            condition = get_input("Condition (0 to go back): ")
            if condition is None:
                continue
            
            colour = get_input("Colour (0 to go back): ")
            if colour is None:
                continue
            
            price = get_input("Price (0 to go back): ")
            if price is None:
                continue
            price = float(price)
            
            photo_path = get_input("Photo folder path (0 to go back): ")
            if photo_path is None:
                continue
            

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

            item_id = input("Enter item ID (0 to go back): ")

            if item_id == "0":
                continue

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

            item_id = input("Enter item ID to edit (0 to go back): ")

            if item_id == "0":
                continue

            while True:
                print("\nWhat do you want to edit?")
                print("0. Back")
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

                if field_choice == "0":
                    break

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
            item_id = input("Enter item ID to remove (0 to go back): ")

            if item_id == "0":
                continue

            item = get_item_by_id(item_id)

            if item is None:
                print("Item not found.")
                continue

            if item[9] == "sold":
                print("Sold items cannot be removed. Change the status first if needed.")
                continue

            confirm = input(f'Are you sure you want to remove "{item[1]}"? (y/n): ').lower()

            if confirm == "y":
                delete_item(item_id)
                print("Item removed successfully.")
            else:
                print("Remove cancelled.")


        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again")