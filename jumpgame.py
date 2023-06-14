"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

class Solution:
    def canJump(self, nums):
        max_reach = 0 # initialize the maximum index that can be reached to 0

        for i in range(len(nums)): # iterate over each index in the list
            if i > max_reach: # if the current index is greater than the maximum index that can be reached
                return False  # return False, as it is not possible to reach the current index

            max_reach = max(max_reach, i + nums[i]) # update the maximum index that can be reached

            if max_reach >= len(nums) - 1: # if the maximum index that can be reached is greater than or equal to the last index
                return True # return True, as it is possible to reach the last index

        return False # return False, as it is not possible to reach the last index

if __name__ == "__main__":
    test = Solution()
    input = test.canJump([2,3,1,1,4])
    print(input)
