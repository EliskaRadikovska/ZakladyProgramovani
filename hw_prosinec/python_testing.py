import unittest

def positive_sum(in_list):
    """Adds together the members of a list.
    Args:
    in_list (list): List of positive numbers.

    Returns:
    int, float: Depending on the input numbers, returns the sum of them.

    Raises:
    TypeError: In case the in_list is not a list.
    ValueError: In case the any number in the list is negative.
    """
    if not type(in_list) == list:
        raise TypeError("The input is supposed to be list.")
    if any([x < 0 for x in in_list]):
        raise ValueError("The list members are supposed to be non-negative.")
    return sum(in_list)

class TestSum(unittest.TestCase):

    def test_int(self):
        self.assertEqual(positive_sum([1, 2, 3]), 6, "Should be 6")

    def test_int_fail(self):
        self.assertNotEqual(positive_sum([1, 2, 2]), 6, "Should be 6")

    def test_float(self):
        self.assertEqual(positive_sum([1.1, 2.2, 3.3]), 6.6, "Should be 6.6")

    def test_float_fail(self):
        self.assertNotEqual(positive_sum([1.1, 2.2, 3.3]), 6, "Should be 6")

    def test_list(self):
        with self.assertRaises(TypeError):
            positive_sum(6)

    def test_negative(self):
        with self.assertRaises(ValueError):
            positive_sum([1, -2])

if __name__ == '__main__':
    unittest.main()

