class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        if not capacity or not int(capacity) == capacity:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size == "" or not int(size) == size:
            raise ValueError("invalid size; size should be an integer")
        if not 0 <= size <= self.capacity:
            raise ValueError(
                "Size of jar must be greater than zero and smaller than capacity"
            )
        self._size = size
