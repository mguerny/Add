import unittest
from add import Add


class TestFizzBuzz(unittest.TestCase):

    def test_empty_should_return_0(self):
        self.assertEqual(Add.add(""), 0)

    def test_should_return_sum_of_3_args(self):
        self.assertEqual(Add.add("1"), 1)
        self.assertEqual(Add.add("1,2"), 3)
        self.assertEqual(Add.add("1,2,3"), 6)


if __name__ == '__main__':
    unittest.main()

