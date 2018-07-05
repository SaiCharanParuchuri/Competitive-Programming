import unittest

def get_closing_paren(sentence, index):

    # Find the position of the matching closing parenthesis
    l = []
    a=0
    if sentence[index] != '(':
        return -1
    for i in range(len(sentence)):
        if sentence[i] == "(":
            l.append(sentence[i])
            if i == index:
                a = len(l)
        elif sentence[i] == ")":
            if len(l) == a:
                return i
            l.pop()
    raise Exception("")

# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)