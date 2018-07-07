import unittest

def sort_scores(scores_list, highest):
    count={}
    for i in scores_list:
        count[i]=1
    l=[]
    for i in range(highest+1):
        if i in count:
            temp=[i]*count[i]
            l.extend(temp)
    return list(reversed(l))

# Test Cases

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)