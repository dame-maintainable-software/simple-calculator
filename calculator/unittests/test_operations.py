import unittest
from calculator import operations
from calculator import parse_input


class TestOperations(unittest.TestCase):
    """Standard tests for the operations"""
    def test_add_int(self):
        """Test if the add operation returns the correct result for a test case"""
        self.assertEqual(operations.add(3,4), 7)

    def test_devide_int(self):
        """Test if the devide operation returns the correct result for a test case"""
        self.assertEqual(operations.devide(8,4), 2)

    def test_substract_int(self):
        self.assertEqual(operations.substract(5,2), 3)

    def test_multiply_int(self):
        self.assertEqual(operations.multiply(4,7), 28)


class TestParser(unittest.TestCase):
    """Tests for the parser"""
    def test_parse_add(self):
        """Test if the equation 1 + 2 is parsed and calculated correctly"""
        self.assertEqual(parse_input.parse(["1", "+", "2"]), 3)

    def test_parse_devide(self):
        """Test if the equation 3 / 2 is parsed and calculated correctly"""
        self.assertEqual(parse_input.parse(["8", "/", "4"]), 2)

    def test_parse_substract(self):
        self.assertEqual(parse_input.parse(["7", "-", "12"]), -5)

    def test_parse_multiply(self):
        self.assertEqual(parse_input.parse(["2", "*", "9"]), 18)


if __name__ == '__main__':
    unittest.main()
