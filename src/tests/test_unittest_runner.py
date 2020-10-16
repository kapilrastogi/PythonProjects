import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum([1, 2, 3]) == 6, "should be 6"

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


# python test_unittest_runner.py
# python -m nose2 -- unittest based tests are compatible with nose
if __name__ == "__main__":
    unittest.main()
