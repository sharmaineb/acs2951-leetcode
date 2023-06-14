"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1 # initialize the left and right pointers to the start and end of the list

        while left <= right: # loop until the left pointer is less than or equal to the right pointer
            mid = (left + right) // 2 # calculate the middle index of the list

            if nums[mid] == target: # if the value at the middle index is equal to the target
                return mid # return the middle index

            elif nums[mid] < target: # if the value at the middle index is less than the target
                left = mid + 1 # update the left pointer to mid + 1

            else: # if the value at the middle index is greater than the target
                right = mid - 1 # update the right pointer to mid - 1

        return left # return the left pointer, representing the index where the target should be inserted





if __name__ == "__main__":
    test = Solution()
    input = test.searchInsert([1,3,5,6], 5)
    print(input)