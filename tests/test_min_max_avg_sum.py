import unittest

from pycq.q import Q


class MinMaxAvgSum(unittest.TestCase):
    def test_min(self):
        data = [1, 2, 3]
        ret = Q(data).min()

        self.assertEqual(1, ret)

    def test_min_with_selector(self):
        data = [1, 2, 3]
        ret = Q(data).min(lambda x: -x)

        self.assertEqual(-3, ret)

    def test_max(self):
        data = [1, 2, 3]
        ret = Q(data).max()

        self.assertEqual(3, ret)

    def test_max_with_selector(self):
        data = [1, 2, 3]
        ret = Q(data).max(lambda x: -x)

        self.assertEqual(-1, ret)

    def test_sum(self):
        data = [1, 2, 3]
        ret = Q(data).sum()

        self.assertEqual(6, ret)

    def test_sum_with_selector(self):
        data = [1, 2, 3]
        ret = Q(data).sum(lambda x: -x)

        self.assertEqual(-6, ret)

    def test_average(self):
        data = [1, 2, 3]
        ret = Q(data).average()

        self.assertEqual(2, ret)

    def test_average_with_selector(self):
        data = [1, 2, 3]
        ret = Q(data).average(lambda x: -x)

        self.assertEqual(-2, ret)
