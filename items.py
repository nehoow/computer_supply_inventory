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