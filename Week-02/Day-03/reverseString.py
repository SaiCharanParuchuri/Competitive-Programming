import unittest

def reverse(list_of_chars):

    # Reverse the input list of chars in place
    l = len(list_of_chars)             
    high = l - 1
    mid = l/2                
    for i in range(0, mid):    
        temp = list_of_chars[high]     
        list_of_chars[high] = list_of_chars[i]
        list_of_chars[i] = temp
        high-=1

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)