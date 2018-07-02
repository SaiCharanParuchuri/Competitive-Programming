import unittest


class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    max = 0
    def __init__(self):
        self.s = s()
        self.s2 = s()

    def push(self, item):
        if(len(self.s.items)==0):
            self.s2.push(item)
            self.s.push(item)
            self.max = item
        
        else:
            if(item>self.max):
                self.max = item
            self.s.push(item)
            self.s2.push(self.max)
    def pop(self):
        self.s2.pop()
        return self.s.pop()

    def get_max(self):
        return self.s2.peek()


# Tests

class Test(unittest.TestCase):

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)