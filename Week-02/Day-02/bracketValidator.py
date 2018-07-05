import unittest

def is_valid(code):

    l = []
    for i in code:
        if i == "(" or i == "{" or i == "[":
            l.append(i)
        elif len(l) == 0:
            return False
        elif i == ")" and l[len(l)-1] == "(":
            l.pop()
        elif i == "}" and l[len(l)-1] == "{":
            l.pop()
        elif i == "]" and l[len(l)-1] == "[":
            l.pop()
        else:
            return False
    if len(l) == 0:
        return True
    return False

# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)