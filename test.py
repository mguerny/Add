import unittest
from add import Add


class TestFizzBuzz(unittest.TestCase):

    def test_empty_should_return_0(self):
        self.assertEqual(Add.add(""), '0')

    def test_should_return_sum_of_3_args(self):
        self.assertEqual(Add.add("1"), '1.0')
        self.assertEqual(Add.add("1.5,2"), '3.5')
        self.assertEqual(Add.add("1,2,3"), '6.0')

    def test_more_than_3_arguments(self):
        self.assertEqual(Add.add("1,2,3,1"), '7.0')

    def test_newline_as_separator(self):
        self.assertEqual(Add.add(r"1\n2,3,1"), '7.0')

    def test_no_separator_as_end(self):
        self.assertEqual(Add.add("1,2,3,1,"), 'Number expected but EOF found')

    def test_custom_separator(self):
        self.assertEqual(Add.add(r"//?\n1?2?3?1"), '7.0')


if __name__ == '__main__':
    unittest.main()
