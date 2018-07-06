import unittest
from itertools import permutations

def has_palindrome_permutation(string):
    
    l=list(string)
    all_permutations=permutations(l)
    permutations_list=list(all_permutations)
    for i in permutations_list:
        temp=i[:]
        if i==temp[::-1]:
            return True
    return False
#   """  # Check if any permutation of the input is a palindrome
#     freq = {}
#     for ch in string:
#         if ch in freq:
#             del freq[ch]
#         else:
#             freq[ch] = True
#     return len(freq) <= 1

# """
# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)