import unittest
from .main import calculate_results

# This file contains the unit tests for the calculate_results function in the main.py module.
# To run this file, enter the command 'python3 -m unittest testing.py' in the shell.

# Test Case for a specific case where input list contains [3, 1, 2, 10, 1]
# The expected output list should be [3, 4, 6, 16, 17]
class Test_Case1(unittest.TestCase):
    def test_case1(self):
        nums = [3, 1, 2, 10, 1]
        expected = [3, 4, 6, 16, 12]
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# Test Case for a large list with elements from 1 to 1000
# The expected output list should be cumulative sum of 1 to 1000
class Test_Large_List(unittest.TestCase):
    def test_large_list(self):
        nums = list(range(1, 1001))
        expected = []
        cumulative_sum = 0
        for i in range(1, 1001):
            cumulative_sum += i
            expected.append(cumulative_sum)
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# Test Case for a list containing negative values
# The expected output list should be cumulative sum of [-1, 2, -3, 4, -5]
class Test_Negative_Values(unittest.TestCase):
    def test_negative_values(self):
        nums = [-1, 2, -3, 4, -5]
        expected = [-1, 1, -2, 2, -3]
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# Test Case for a list containing floating-point values
# The expected output list should be cumulative sum of [1.5, 2.25, 3.75, 4.2]
class Test_Float_Values(unittest.TestCase):
    def test_float_values(self):
        nums = [1.5, 2.25, 3.75, 4.2]
        expected = [1.5, 3.75, 7.5, 11.7]
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# Test Case for a list containing repeated value 2
# The expected output list should be [2, 4, 6, 8, 10]
class Test_Repeated_Values(unittest.TestCase):
    def test_repeated_value(self):
        nums = [2, 2, 2, 2, 2]
        expected = [2, 4, 6, 8, 10]
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# Test Case for an empty list
# The expected output list should also be an empty list
class Test_Empty_List(unittest.TestCase):
    def test_empty_list(self):
        nums = []
        expected = []
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# Test Case for a list containing a single value 5
# The expected output list should also be [5]
class Test_single_value(unittest.TestCase):
    def test_single_value(self):
        nums = [5]
        expected = [5]
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# Test Case for a list containing all negative values
# The expected output list should be cumulative sum of [-1, -2, -3, -4, -5]
class Test_All_Negative_Values(unittest.TestCase):
    def test_all_negative_values(self):
        nums = [-1, -2, -3, -4, -5]
        expected = [-1, -3, -6, -10, -15]
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# Test Case for a list containing all zero values
# The expected output list should be a list of zeros with the same length
class Test_All_Zero_Values(unittest.TestCase):
    def test_all_zero_values(self):
        nums = [0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0]
        results = calculate_results(nums)
        self.assertEqual(results, expected)

# The following code will execute all the test cases when running this file.
if __name__ == "__main__":
    unittest.main()
