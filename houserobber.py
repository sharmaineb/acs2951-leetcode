"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

class Solution:
    def rob(self, nums):
        if not nums: # if the list is empty
            return 0 # return 0, as no money can be robbed

        n = len(nums) # get the length of the list
        if n == 1: # if there is only one house
            return nums[0] # return the amount of money in that house

        dp = [0] * n # create a list of size n to store the maximum amount of money that can be robbed
        dp[0] = nums[0] # set the value for the first house to the amount of money in that house
        dp[1] = max(nums[0], nums[1]) # set the value for the second house as the maximum of the amounts in the first two houses

        for i in range(2, n): # iterate over the houses starting from the third house
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) # calculate the maximum amount of money that can be robbed by either robbing the current house or skipping it

        return dp[-1] # return the maximum amount of money that can be robbed, which is stored in the last element of the list

if __name__ == "__main__":
    test = Solution()
    input = test.rob([1,2,3,1])
    print(input)