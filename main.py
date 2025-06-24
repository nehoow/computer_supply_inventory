import argparse
from inventory import Inventory
from items import CPU, RAM, Monitor, Storage, Peripheral


inventory_manager = Inventory()
def main():
    parser = argparse.ArgumentParser(description="Simplified Computer Supplies Inventory Management System.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    

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