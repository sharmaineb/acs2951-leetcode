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
        max_reach = 0                  # Initialize the maximum index that can be reached to 0

        for i in range(len(nums)):    # Iterate over each index in the list
            if i > max_reach:         # If the current index is greater than the maximum index that can be reached
                return False          # Return False, as it is not possible to reach the current index

            max_reach = max(max_reach, i + nums[i])  # Update the maximum index that can be reached

            if max_reach >= len(nums) - 1:  # If the maximum index that can be reached is greater than or equal to the last index
                return True                # Return True, as it is possible to reach the last index

        return False  # Return False, as it is not possible to reach the last index

if __name__ == "__main__":
    test = Solution()
    input = test.canJump([2,3,1,1,4])
    print(input)
