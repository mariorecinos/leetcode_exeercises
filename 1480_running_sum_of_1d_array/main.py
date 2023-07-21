# to run the test from replit go to tools on the bottom left and then click on unit test then click on run test

# replit Link https://replit.com/@maritochapin/Leetcode-1480-Running-Sum-of-1D-Array#main.py



def calculate_results(nums):
 # list that stores our appended results
  results = []

  # add the first item in the list to the results array after
  # iterate over each value in the nums list and add the previous index with the next index
  # example
  # results.append(nums[0])  # Append the first element of nums to results [2]
  # results.append(nums[0] + nums[1])  # Append the sum of the first two elements of nums to results [2, 4]
  # results.append(nums[0] + nums[1] + nums[2])  # Append the sum of the first three elements of nums to results [2, 4, 6]
  # results.append(nums[0] + nums[1] + nums[2] + nums[3])  # Append the sum of the first four elments of nums to results [2, 4, 6, 8]
   # results.append(nums[0] + nums[1] + nums[2] + nums[3] + nums[4])  # Append the sum of all elements of nums to results [2, 4, 6, 8]

  for i in range(len(nums)):
   if i == 0:
    results.append(nums[i])
   else:
    currentTotal = results[i -1] + nums[i]
    results.append(currentTotal)

  return results

# function to test our calculate_results() function if expected matches our result

# Function test_repeated_value() tests the calculate_results() function by passing a predefined input list [2, 2, 2, 2, 2].
# The expected output for this input list is [2, 4, 6, 8, 10].
# The test function then compares the expected output with the actual output obtained from calculate_results(nums).
# If the expected and actual outputs match, it prints "Test Passed ✓" in green color using the ANSI escape code '\033[32m'.
# If the outputs do not match, it prints "Test failed ✗" in red color using the ANSI escape code '\033[31m'.
# The expected and actual outputs are also displayed in the output message.
# After printing the test result, the function returns the printed message.

def test_repeated_value():

  nums = [2, 2, 2, 2, 2]
  expected = [2, 4, 6, 8, 10,]
  results = calculate_results(nums)

  if expected != results:
    test_result = print(f"\033[31mTest failed ✗ Expected {expected}, but got {results} \033[0m")
    return test_result
  else:
    test_result = print("\033[32mTest Passed ✓\033[0m")
    return test_result

# Uncomment the following line to run the test_repeated_value() function and see the test result.
# test_repeated_value()
