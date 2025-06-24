import json
from items import item_from_dict, SupplyItem, CPU, RAM, Monitor, Storage, Peripheral

class Inventory:
    def __init__(self, data_file="inventory_data.json"):
        self.items: dict[str, SupplyItem] = {} # item_id -> SupplyItem object
        self.data_file = data_file
        self.load_data() # Load data automatically on initialization
    
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