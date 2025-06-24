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

    
    # --- Remove Item Command ---
    remove_parser = subparsers.add_parser("remove", help="Remove an item by ID.")
    remove_parser.add_argument("item_id", help="ID of the item to remove.")

    # --- View Item Command ---
    view_parser = subparsers.add_parser("view", help="View details of a specific item.")
    view_parser.add_argument("item_id", help="ID of the item to view.")

    # --- Restock Item Command ---
    restock_parser = subparsers.add_parser("restock", help="Restock an item's quantity.")
    restock_parser.add_argument("item_id", help="ID of the item to restock.")
    restock_parser.add_argument("amount", type=int, help="Amount to restock.")

    # --- Sell Item Command ---
    sell_parser = subparsers.add_parser("sell", help="Sell items and decrease quantity.")
    sell_parser.add_argument("item_id", help="ID of the item to sell.")
    sell_parser.add_argument("amount", type=int, help="Amount to sell.")

    # --- List Commands ---
    list_parser = subparsers.add_parser("list", help="List inventory items.")
    list_subparsers = list_parser.add_subparsers(dest="list_type", required=True, help="Type of listing")

    list_subparsers.add_parser("all", help="List all items in inventory.")
    list_items_type_parser = list_subparsers.add_parser("type", help="List items by a specific type.")
    list_items_type_parser.add_argument("--item_type", required=True, choices=['cpu', 'ram', 'monitor', 'storage', 'peripheral'], help="The type of item to list.")

    # --- Total Value Command ---
    total_value_parser = subparsers.add_parser("total-value", help="Calculate total inventory value.")

    args = parser.parse_args()

    try:
        if args.command == "add":
            common_args = {
                "item_id": args.id,
                "name": args.name,
                "quantity": args.qty,
                "price": args.price,
            }
            if args.item_type == "cpu":
                item = CPU(**common_args, socket_type=args.socket)
            elif args.item_type == "ram":
                item = RAM(**common_args, capacity_gb=args.capacity_gb)
            elif args.item_type == "monitor":
                item = Monitor(**common_args, screen_size_inches=args.size_inch)
            elif args.item_type == "storage":
                item = Storage(**common_args, capacity_gb=args.capacity_gb)
            elif args.item_type == "peripheral":
                item = Peripheral(**common_args, device_type=args.dev_type)
            else:
                print(f"Error: Unknown item type '{args.item_type}'")
                return
            
            inventory_manager.add_item(item)

        elif args.command == "remove":
            inventory_manager.remove_item(args.item_id)

        elif args.command == "view":
            item = inventory_manager.find_item(args.item_id)
            if item:
                item.display_details()
            else:
                print(f"Item with ID '{args.item_id}' not found.")

        elif args.command == "restock":
            inventory_manager.restock_item(args.item_id, args.amount)

        elif args.command == "sell":
            inventory_manager.sell_item(args.item_id, args.amount)

        elif args.command == "list":
            if args.list_type == "all":
                inventory_manager.list_all_items()
            elif args.list_type == "type":
                inventory_manager.list_items_by_type(args.item_type)

        elif args.command == "total-value":
            inventory_manager.get_total_inventory_value()

        elif args.command is None: # If no command is given, print help
            parser.print_help()
        

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()