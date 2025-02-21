class MyQueue:

    def __init__(self):
        self.queue = []
        self.size = 0
        self.capacity = 5



    def isEmpty(self):
        if len(self.queue) == 0:
            return True

    def isFull(self):
        if len(self.queue) == self.size:
            return True


    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.pop(0)
        else:
            return "Index out of range"

    def qsize(self):
        return len(self.queue)


    def peek(self):
        if self.size > 0:
            return self.queue[0]
        else:
            return "Index out of range"


