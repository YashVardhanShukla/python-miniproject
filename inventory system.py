class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                print("Insufficient quantity to remove.")
        else:
            print("Item not found in inventory.")

    def update_item(self, item_name, new_quantity):
        if item_name in self.items:
            self.items[item_name] = new_quantity
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

def main():
    inventory = Inventory()

    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(item_name, quantity)
        elif choice == '3':
            item_name = input("Enter item name: ")
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_item(item_name, new_quantity)
        elif choice == '4':
            inventory.display_inventory()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
