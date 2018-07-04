import unittest

def afterNode(head):

    # afterNode the linked list in place
    current = head
    afterNode = None
    while current:
        beforeNode = current.next
        current.next = afterNode
        afterNode = current
        current = beforeNode
    return afterNode


# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def test_short_linked_list(self):
        beforeNode = Test.LinkedListNode(2)
        current = Test.LinkedListNode(1, beforeNode)

        result = afterNode(current)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [2, 1]
        self.assertEqual(actual, expected)

    def test_long_linked_list(self):
        sixth = Test.LinkedListNode(6)
        fifth = Test.LinkedListNode(5, sixth)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        beforeNode = Test.LinkedListNode(2, third)
        current = Test.LinkedListNode(1, beforeNode)

        result = afterNode(current)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [6, 5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)

    def test_one_element_linked_list(self):
        current = Test.LinkedListNode(1)

        result = afterNode(current)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [1]
        self.assertEqual(actual, expected)

    def test_empty_linked_list(self):
        result = afterNode(None)
        self.assertIsNone(result)


unittest.main(verbosity=2)