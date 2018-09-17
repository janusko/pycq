import unittest
from typing import cast, Iterable

from q import Q


class SelectMany(unittest.TestCase):
    def test_select_many(self):
        data = [1, 2, 3], [4, 5, 6]
        ret = Q(data).select_many(lambda x: cast(Iterable[int], x)).to_list()
        
        self.assertSequenceEqual(ret, [1, 2, 3, 4, 5, 6])