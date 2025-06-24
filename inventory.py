import json
from items import item_from_dict, SupplyItem, CPU, RAM, Monitor, Storage, Peripheral

class Inventory:
    def __init__(self, data_file="inventory_data.json"):
        self.items: dict[str, SupplyItem] = {} # item_id -> SupplyItem object
        self.data_file = data_file
        self.load_data() # Load data automatically on initialization