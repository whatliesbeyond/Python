# Solution to Problem 1
# This script has the method to find repeating numbers in a given array and 4 unit tests to test that method.
# Please use "python findRepeatingNumbers.py" command from the terminal to execute this script. All 4 unittests will be executed as a test suite. If any of the
# test fails, unittest library will point to the test where it failed.
# With the input arrays in the script, all tests PASS.
# Revision            Author              Comment
# 1.0                 Dewang              Initial Design


from array import *
import unittest
#


# List of Input arrays to test our method -  The array elements can be changed to test find_repeating_nums(input_array) functionality and performance
myarray = array('i',[10,6,3,1,3,4,9,10,7,0,0])
myarray1 = array('c',['s','g','s','h','f','r','h'])
myarray2 = array('i',[40000000,6235,3345,179,369,40000000,91245,15770,77889,34098,3409575,439057,32723,23975,91245,91245,77889,91245])
myarray3 = array('i',[-40000000,6235,3345,179,369,-40000000,91245,15770,77889,34098,3409575,439057,32723,23975,-91245,-91245,77889])
list1 = ["asf","dfdaf","asf"]
myarray4 = array('i',[1,2,3,4,5,6,7,8,9,10])
myarray5 = []

# Method to find repeating numbers in an array
def find_repeating_nums(input_array):
    nums = set([]) # Final set that stores "unique" repeated elements
    count_repeating_nums = set([]) # a counter set for repeated numbers
    if input_array == []:
        return False
    else:
        for i in input_array:
            if i in count_repeating_nums: #if an element is already stored in coun_repeating_nums, this means it was repeated, add it to final set
                nums.add(i)
            else:
                count_repeating_nums.add(i) #else add it to element appeared for the first time, add it to count_repeating_nums
    if list(nums) == []:
        return False         # return false if no repeated elements
    else:
        return list(nums)    # else return the list of repeated elements


# Test Suite to cover all the test cases
class UnitTestSuite(unittest.TestCase):

    #Test to check functionality
    def testRepeatingNumbers(self):
        self.assertEqual(find_repeating_nums(myarray),[0,10,3],'Test Failed: The output of method does not match expected output.')
        self.assertEqual(find_repeating_nums(myarray1),['h','s'],'Test Failed: The output of method does not match expected output.')
        self.assertEqual(find_repeating_nums(list1),['asf'],'Test Failed: The output of method does not match expected output.')
        self.assertEqual(find_repeating_nums(myarray2),[40000000, 77889, 91245],'Test Failed: The output of method does not match expected output.')
        self.assertEqual(find_repeating_nums(myarray3),[-40000000, 77889, -91245],'Test Failed: The output of method does not match expected output.')

    #Test to check if the array has no repeating numbers
    def testNoRepeatingNumbers(self):
        self.assertFalse(find_repeating_nums(myarray4),'The array has no repeating numbers')

    #Test to check if our knowledge of Input domain is correct
    def testFail(self):
        self.assertNotEqual(find_repeating_nums(myarray),[10,3],'Test Failed: The output of method does not match expected output, probably a bug in Test Case Output')

    #Test to check if given array is empty
    def testBadInput(self):
        self.assertFalse(find_repeating_nums(myarray5))

if __name__ == '__main__':
    unittest.main()
