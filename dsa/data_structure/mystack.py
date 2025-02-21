class MyStack:

    def __init__(self):
        self.stackList = []


    def is_empty(self):
        return len(self.stackList) == 0


    def push(self, item):
        return self.stackList.append(item)


    def pop(self):
        if not self.is_empty():
            return self.stackList.pop()
        else:
            raise IndexError("Stack is empty")