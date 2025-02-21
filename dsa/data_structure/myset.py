class MySet(set):

    def __init__(self, size):
        self.size = size
        self.elements = []

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def add(self, value):
        if len(self.elements) < self.size:
            if value in self.elements:
                self.elements.append(value)
            return "Value {value} already present in set".format(value=value)

    def remove(self, value):
        if value in self.elements:
            self.elements.remove(value)
        return "Value {value} not found".format(value=value)



    def contains(self, value):
        if value in self.elements:
            return True
        else:
            return False


    def sort(self):
        if self.size > 1:
            self.elements.sort()

    def index(self, value):
        if value in self.elements:
            return self.elements.index(value)

    def clear(self):
        self.elements.clear()








