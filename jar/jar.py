class Jar:
    def __init__(self, capacity=12,size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        res = ""
        for _ in range(self.size):
            res += "🍪"
        return res

    def deposit(self, n):
        if self.size+n>self.capacity:
            raise ValueError("Exceeded capacity")
        self.size+=n

    def withdraw(self, n):
        if self.size-n<0:
            raise ValueError("Exceeded capacity")
        self.size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        """"""
        if not int(capacity) > 0:
            raise ValueError("Not a non-negative integer.")
        self._capacity = capacity

    @size.setter
    def size(self, size):
        """"""
        if int(size) < 0:
            raise ValueError
        else:
            self._size = size
