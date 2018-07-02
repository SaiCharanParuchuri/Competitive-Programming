import unittest


class QueueTwoStacks(object):
    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def enqueue(self,element):
      self.Stack1.append(element)
 
    def dequeue(self):
      if len(self.Stack2) == 0:
        if len(self.Stack1) == 0:
          raise Exception('')
        while len(self.Stack1) > 0:
          p = self.Stack1.pop()
          self.Stack2.append(p)
      return self.Stack2.pop()


class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)