import unittest
from add import Add


class TestFizzBuzz(unittest.TestCase):

    def test_empty_should_return_0(self):
        self.assertEqual(Add.add(""), 0)


if __name__ == '__main__':
    unittest.main()

