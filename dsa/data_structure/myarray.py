from operator import index


class MyArray:

    def __init__(self, size):
        self.size = size
        self.array = []
        self.capacity = size
        self.is_empty = False

    def isEmpty(self):
        if len(self.array) == 0:
            return True


    def isFull(self):
        if self.size == self.capacity:
            return True

    def add(self, value):
        if len(self.array) <= self.size:
            self.array.append(value)
        # raise ValueError ("Array is full")

    def remove(self, value):
        if value in self.array:
            self.array.remove(value)
            self.size -= 1
            return "Value {value} removed".format(value=value)
        return "Value {value} is not present in array".format(value=value)


    def contains(self, value):
        if value in self.array:
            return True
        return False


    def pop(self, index):
        if index < 0 or index >= len(self.array):
            return "Index out of range"
        else:
            self.size -= 1
            return self.array[index]


    def insert(self, index, value):
        if index < 0 or index >= len(self.array):
            return "Index out of range"
        self.array.insert(index, value)
        return "Value {value} inserted".format(value=value)