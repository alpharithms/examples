from typing import Any, NoReturn


class Queue:

    def __init__(self):
        self._items = []

    def add(self, item: Any) -> NoReturn:
        """Adds an item to the back of the queue"""
        self._items.append(item)

    def pop(self) -> Any:
        """Removes the first item of the queue"""
        return self._items.pop(0)

    def is_empty(self) -> bool:
        """Checks if any items are in the queue"""
        return len(self._items) == 0

    def __str__(self):
        return str(self._items)


if __name__ == '__main__':

    # Create a new Queue object
    q = Queue()

    # Have some items
    people = ['bob', 'alice', 'pat']

    # View starting queue
    print("Initial Queue:", q)

    # Add everyone to the queue
    for person in people:

        print("\tAdding:", person)
        q.add(person)

    # View full queue
    print("Filled Queue:", q)

    # Remove People, one-by-one
    while not q.is_empty():

        next_person = q.pop()

        print("\tNext Person:", next_person)

    # Print resulting queue
    print("Final Queue:", q)
