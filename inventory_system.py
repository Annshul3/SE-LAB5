"""
Inventory Management System.

This module provides basic functions to manage a simple stock inventory,
including adding, removing, loading, and saving data.
"""
import json
from datetime import datetime
# Removed: Unused import logging

# Global variable
stock_data = {}


def add_item(item: str = "default", qty: int = 0, logs: list = None):
    """
    Adds a quantity of an item to the inventory.

    Args:
        item (str): The name of the item.
        qty (int/float): The quantity to add.
        logs (list, optional): List to track operation logs. Defaults to None.
    """
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str):
        print(f"Error: Item name must be a string. Received: {item}")
        return
    if not isinstance(qty, (int, float)):
        print(f"Error: Quantity must be a number. Received: {qty}")
        return

    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty

    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: int):
    """
    Removes a quantity of an item from the inventory.

    Args:
        item (str): The name of the item to remove.
        qty (int/float): The quantity to remove.
    """
    try:
        if not isinstance(qty, (int, float)):
            print(f"Error: Quantity must be a number to remove item: {item}")
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Item not found
        print(f"Warning: Attempted to remove non-existent item: {item}")
        # pass is acceptable here because the warning is informative
    except TypeError:
        # Handle unexpected type issues during subtraction
        print(f"Error: Type issue during removal of item: {item}")


def get_qty(item: str) -> int:
    """
    Returns the current quantity of an item.

    Args:
        item (str): The name of the item.

    Returns:
        int: The quantity of the item, or 0 if not found.
    """
    # Use .get() for safe dictionary access (prevents KeyError)
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json"):
    """
    Loads inventory data from a JSON file.

    Args:
        file (str, optional): The path to the JSON file. 
                              Defaults to "inventory.json".
    """
    global stock_data  # W0603: Using the global statement is necessary here

    try:
        # Use 'with open' and explicitly set encoding (W1514)
        with open(file, "r", encoding="utf-8") as f:
            data = f.read()
            if data:
                stock_data = json.loads(data)
            else:
                stock_data = {}
                print(f"Warning: Data file '{file}' is empty.")
    except FileNotFoundError:
        print(f"Warning: Data file '{file}' not found. Initializing empty "
              "inventory.")
    except json.JSONDecodeError as e:
        print(f"Error: Could not decode JSON from '{file}': {e}. Inventory "
              "may be corrupted.")


def save_data(file: str = "inventory.json"):
    """
    Saves current inventory data to a JSON file.

    Args:
        file (str, optional): The path to the JSON file. 
                              Defaults to "inventory.json".
    """
    try:
        # Use 'with open' and explicitly set encoding (W1514)
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
    except IOError as e:
        print(f"Error saving data to '{file}': {e}")


def print_data():
    """Prints a formatted report of all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5) -> list:
    """
    Identifies and returns a list of items with quantity below the threshold.

    Args:
        threshold (int, optional): The low stock limit. Defaults to 5.

    Returns:
        list: A list of item names below the threshold.
    """
    result = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """Main execution function for the inventory system demonstration."""
    load_data()

    print("--- Running Inventory Operations ---")

    add_item("apple", 10)
    add_item("banana", 5)

    # Test cases for validation/error handling (no longer crash)
    add_item(123, "ten")

    remove_item("apple", 3)
    remove_item("orange", 1)

    apple_qty = get_qty("apple")
    print(f"Apple stock: {apple_qty}")

    print(f"Low items (threshold 5): {check_low_items()}")

    # Removed the dangerous eval() call

    save_data()
    print("--- Operations Complete. Data Saved. ---")


if __name__ == "__main__":
    main()