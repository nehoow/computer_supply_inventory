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