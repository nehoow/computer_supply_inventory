from abc import ABC, abstractmethod

class SupplyItem(ABC):
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        if not item_id or not name:
            raise ValueError("Item ID and Name cannot be empty.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")

        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def restock(self, amount: int):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Restock amount must be a positive integer.")
        self.quantity += amount
        print(f"Restocked {self.name} by {amount}. New quantity: {self.quantity}")
    
    def sell(self, amount: int):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Sell amount must be a positive integer.")
        if self.quantity < amount:
            raise ValueError(f"Insufficient stock for {self.name}. Available: {self.quantity}, Requested: {amount}")
        self.quantity -= amount
        print(f"Sold {amount} of {self.name}. New quantity: {self.quantity}")
    
    def get_total_value(self) -> float:
        return self.quantity * self.price
    
    @abstractmethod
    def display_details(self):
        """Abstract method to print specific details of the item type."""
        pass

    @abstractmethod
    def to_dict(self):
        """Convert the item to a dictionary representation."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(ID: {self.item_id}, Name: {self.name}, Qty: {self.quantity})"

    def __repr__(self):
        return self.__str__()
    
class CPU(SupplyItem):
    def __init__(self, item_id: str, name: str, quantity: int, price: float,socket_type: str):
        
        super().__init__(item_id, name, quantity, price)
        self.socket_type = socket_type
    
    def display_details(self):
        print(f"--- CPU Details (ID: {self.item_id}) ---")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ${self.price:.2f}")
        print(f"Total Value: ${self.get_total_value():.2f}")
        print(f"Socket Type: {self.socket_type}")
        print("-" * 30)

    def to_dict(self):
        return {
            "type": "CPU",
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "socket_type": self.socket_type
        }
    
class RAM(SupplyItem):
    def __init__(self, item_id: str, name: str, quantity: int, price: float,
                 capacity_gb: int):
        super().__init__(item_id, name, quantity, price)
        self.capacity_gb = capacity_gb

    def display_details(self):
        print(f"--- RAM Details (ID: {self.item_id}) ---")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ${self.price:.2f}")
        print(f"Total Value: ${self.get_total_value():.2f}")
        print(f"Capacity: {self.capacity_gb} GB")
        print("-" * 30)

    def to_dict(self):
        return {
            "type": "RAM",
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "capacity_gb": self.capacity_gb
        }
class Monitor(SupplyItem):
    def __init__(self, item_id: str, name: str, quantity: int, price: float,
                 screen_size_inches: float): 
        super().__init__(item_id, name, quantity, price)
        self.screen_size_inches = screen_size_inches

    def display_details(self):
        print(f"--- Monitor Details (ID: {self.item_id}) ---")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ${self.price:.2f}")
        print(f"Total Value: ${self.get_total_value():.2f}")
        print(f"Screen Size: {self.screen_size_inches} inches")
        print("-" * 30)

    def to_dict(self):
        return {
            "type": "Monitor",
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "screen_size_inches": self.screen_size_inches
        }

class Storage(SupplyItem):
    def __init__(self, item_id: str, name: str, quantity: int, price: float,
                 capacity_gb: int):
        super().__init__(item_id, name, quantity, price)
        self.capacity_gb = capacity_gb

    def display_details(self):
        print(f"--- Storage Details (ID: {self.item_id}) ---")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ${self.price:.2f}")
        print(f"Total Value: ${self.get_total_value():.2f}")
        print(f"Capacity: {self.capacity_gb} GB")
        print("-" * 30)

    def to_dict(self):
        return {
            "type": "Storage",
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "capacity_gb": self.capacity_gb
        }