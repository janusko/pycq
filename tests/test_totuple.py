import unittest

from q import Q


class ToTuple(unittest.TestCase):
    def test_list(self):
        data = [1, 2, 3]
        ret = Q(data).to_tuple()

        self.assertIsInstance(ret, tuple)
        self.assertSequenceEqual(ret, data)
