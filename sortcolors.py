"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0 # initialize the low pointer to the first index of the list
        mid = 0 # initialize the mid pointer to the first index of the list
        high = len(nums) - 1 # initialize the high pointer to the last index of the list

        while mid <= high: # loop until the mid pointer crosses the high pointer
            if nums[mid] == 0: # if the value at the mid index is 0
                swap(nums[low], nums[mid]) # swap the values at the low and mid indices
                low += 1 # increment the low pointer
                mid += 1 # increment the mid pointer
            elif nums[mid] == 1: # if the value at the mid index is 1
                mid += 1 # increment the mid pointer
            else: # if the value at the mid index is 2
                swap(nums[mid], nums[high]) # swap the values at the mid and high indices
                high -= 1 # decrement the high pointer

if __name__ == "__main__":
    test = Solution()
    input = test.sortColors([2,0,2,1,1,0])
    print(input)