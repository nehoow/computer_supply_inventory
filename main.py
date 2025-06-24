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

    # CPU
    cpu_parser = add_subparsers.add_parser("cpu", help="Add a CPU.")
    add_common_args(cpu_parser)
    cpu_parser.add_argument("--socket", required=True, help="CPU Socket Type (e.g., AM5, LGA1700)")

    # RAM
    ram_parser = add_subparsers.add_parser("ram", help="Add RAM.")
    add_common_args(ram_parser)
    ram_parser.add_argument("--capacity_gb", type=int, required=True, help="Capacity in GB")

    # Monitor
    monitor_parser = add_subparsers.add_parser("monitor", help="Add a Monitor.")
    add_common_args(monitor_parser)
    monitor_parser.add_argument("--size_inch", type=float, required=True, help="Screen size in inches")

    # Storage
    storage_parser = add_subparsers.add_parser("storage", help="Add Storage.")
    add_common_args(storage_parser)
    storage_parser.add_argument("--capacity_gb", type=int, required=True, help="Capacity in GB")

    # Peripheral
    peripheral_parser = add_subparsers.add_parser("peripheral", help="Add a Peripheral (Keyboard, Mouse, etc.).")
    add_common_args(peripheral_parser)
    peripheral_parser.add_argument("--dev_type", required=True, help="Device type (e.g., Keyboard, Mouse, Webcam)")
    
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