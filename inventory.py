import json
from items import item_from_dict, SupplyItem, CPU, RAM, Monitor, Storage, Peripheral

class Inventory:
    def __init__(self, data_file="inventory_data.json"):
        self.items: dict[str, SupplyItem] = {} 
        self.data_file = data_file
        self.load_data() 
    
    def add_item(self, item: SupplyItem):
        """Adds a SupplyItem object to the inventory."""
        if item.item_id in self.items:
            raise ValueError(f"Item with ID '{item.item_id}' already exists.")
        self.items[item.item_id] = item
        print(f"Added item: {item.name} (ID: {item.item_id})")
        self.save_data()

    def remove_item(self, item_id: str):
        """Removes an item from the inventory by its ID."""
        if item_id not in self.items:
            raise ValueError(f"Item with ID '{item_id}' not found.")
        del self.items[item_id]
        print(f"Removed item with ID: {item_id}")
        self.save_data()

    def find_item(self, item_id: str) -> SupplyItem | None:
        """Finds and returns an item by its ID, or None if not found."""
        return self.items.get(item_id)
    
    def restock_item(self, item_id: str, amount: int):
        """Restocks a specific item."""
        item = self.find_item(item_id)
        if not item:
            raise ValueError(f"Item with ID '{item_id}' not found.")
        item.restock(amount)
        self.save_data()
    
    def list_all_items(self):
        """Lists details of all items in the inventory."""
        if not self.items:
            print("Inventory is empty.")
            return
        print("\n--- Current Inventory Items ---")
        for item_id, item in self.items.items():
            item.display_details()
        print("-----------------------------\n")

    def list_items_by_type(self, item_type: str):
        """Lists items of a specific type (e.g., 'CPU', 'Monitor')."""
        found_items = [item for item in self.items.values() if item.__class__.__name__.lower() == item_type.lower()]
        if not found_items:
            print(f"No {item_type} items found.")
            return
        print(f"\n--- {item_type} Items ---")
        for item in found_items:
            item.display_details()
        print("---------------------------\n")

    def sell_item(self, item_id: str, amount: int):
        """Sells a specific item."""
        item = self.find_item(item_id)
        if not item:
            raise ValueError(f"Item with ID '{item_id}' not found.")
        item.sell(amount)
        self.save_data()
    
    def get_total_inventory_value(self) -> float:
        """Calculates the total monetary value of all items in inventory."""
        total_value = sum(item.get_total_value() for item in self.items.values())
        print(f"Total inventory value: ${total_value:.2f}")
        return total_value
    
    def save_data(self):
        """Saves current inventory data to a JSON file."""
        data_to_save = {
            "items": [item.to_dict() for item in self.items.values()]
        }
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data_to_save, f, indent=4)
            print(f"Inventory data saved to {self.data_file}")
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def load_data(self):
        """Loads inventory data from a JSON file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.items.clear()

                for item_data in data.get("items", []):
                    try:
                        item = item_from_dict(item_data)
                        self.items[item.item_id] = item
                    except ValueError as e:
                        print(f"Warning: Could not load item '{item_data.get('item_id', 'unknown')}' due to: {e}")

            print(f"Inventory data loaded from {self.data_file}")
        except FileNotFoundError:
            print(f"No existing data file '{self.data_file}' found. Starting with empty inventory.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {self.data_file}: {e}. Starting with empty inventory.")
        except Exception as e:
            print(f"An unexpected error occurred during data loading: {e}. Starting with empty inventory.")