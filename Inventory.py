import Item
from Item import *

class Inventory():
    items = []

    def add_random_item(self):
        item = create_item()
        self.items.append(item)

    def print_items(self):
        for item in self.items:
            item.print()