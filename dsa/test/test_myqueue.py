import unittest
from data_structure.myqueue import MyQueue
# from myqueue import MyQueue


class TestMySet(unittest.TestCase):

    def test_that_my_queue_isEmpty(self):
        myqueue = MyQueue()
        self.assertTrue(myqueue.isEmpty())

    def test_that_my_queue_isFull(self):
        myqueue = MyQueue()
        self.assertTrue(myqueue.isFull())

    def test_that_my_queue_enqueue(self):
        myqueue = MyQueue()
        myqueue.enqueue(1)
        myqueue.enqueue(2)
        myqueue.enqueue(3)
        self.assertEqual(myqueue.size, 3)
        self.assertEqual(myqueue.queue, [1, 2, 3])

    def test_that_my_queue_dequeue(self):
        myqueue = MyQueue()
        myqueue.enqueue(1)
        myqueue.enqueue(2)
        myqueue.enqueue(3)
        # self.assertEqual(myqueue.size(), 3)
        self.assertEqual(myqueue.dequeue(), 1)
        self.assertEqual(myqueue.queue, [2, 3])

    def test_size(self):
        myqueue = MyQueue()
        myqueue.enqueue(1)
        myqueue.enqueue(2)
        self.assertEqual(myqueue.size, 2)

    def test_peek(self):
        myqueue = MyQueue()
        myqueue.enqueue(1)
        myqueue.enqueue(2)
        myqueue.enqueue(3)
        self.assertEqual(myqueue.peek(), 1)




