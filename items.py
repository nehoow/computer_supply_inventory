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