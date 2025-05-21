class Stack:
    def __init__(self, items=None, capacity=None):
        self.items = items if items is not None else []
        self.capacity = capacity  # Optional max size

    def push(self, item):
        if self.capacity is not None and len(self.items) >= self.capacity:
            return  # Optionally raise an error
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return self.capacity is not None and len(self.items) >= self.capacity

    def search(self, target):
        # Returns distance from the top of the stack (last index)
        try:
            index_from_bottom = self.items.index(target)
            return len(self.items) - 1 - index_from_bottom
        except ValueError:
            return -1
