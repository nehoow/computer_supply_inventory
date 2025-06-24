import argparse
from inventory import Inventory
from items import CPU, RAM, Monitor, Storage, Peripheral


inventory_manager = Inventory()
def main():
    parser = argparse.ArgumentParser(description="Simplified Computer Supplies Inventory Management System.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

     # --- Add Item Command ---
    add_parser = subparsers.add_parser("add", help="Add a new supply item.")
    add_subparsers = add_parser.add_subparsers(dest="item_type", required=True, help="Type of item to add")

    # Common arguments for all items
    def add_common_args(item_parser):
        item_parser.add_argument("--id", required=True, help="Unique Item ID")
        item_parser.add_argument("--name", required=True, help="Name of the item")
        item_parser.add_argument("--qty", type=int, required=True, help="Initial quantity")
        item_parser.add_argument("--price", type=float, required=True, help="Price per unit")

    args = parser.parse_args()

    try:
        
        if args.command is None: # If no command is given, print help
            parser.print_help()
        

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()