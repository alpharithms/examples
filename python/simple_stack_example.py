from typing import Any, NoReturn


class Stack:
    """A custom implementation of the Stack ADT"""

    def __init__(self):
        """Initializes the Stack with an empty list"""
        self._items = []

    def push(self, item: Any) -> NoReturn:
        """Add an item to the Stack"""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove the most recently-added item from the Stack"""
        return self._items.pop()

    def is_emtpy(self) -> bool:
        """Checks if there are any items in the Stack"""
        return len(self._items) == 0

    def __str__(self):
        return str(self._items)


if __name__ == '__main__':

    # Define some items
    pets = ['dog', 'cat', 'bird']

    # Create a new Stack object
    s = Stack()

    # Display stack before adding items
    print("Initial Stack Items:", s)
    for pet in pets:

        # Add item to the stack
        s.push(pet)

    # Display stack after removing items
    print("New Stack Items:", s)

    # Remove items until none left
    while not s.is_emtpy():

        # Remove next item
        item = s.pop()

        # Print what was removed
        print('\t', item, "removed from Stack.")

    # Print final Stack State
    print("Final Stack State:", s)


