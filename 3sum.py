"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

"""
def threeSum(nums):
    n = len(nums)
    nums.sort()  # Sort the array in non-decreasing order
    triplets = []

    for i in range(n - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return triplets
"""

class Solution:
    def threeSum(self, nums):
        results = []  # create an empty list to store the results
        nums.sort()  # sort the input list in ascending order

        for i in range(len(nums) - 2):  # iterate over the sorted list with index
            if i > 0 and nums[i] == nums[i - 1]:  # check if the current number is a duplicate
                continue  # if duplicate, skip to the next iteration

            j, k = i + 1, len(nums) - 1  # set two pointers, j and k

            while j < k:  # loop until the two pointers meet or cross each other
                three_sum = nums[i] + nums[j] + nums[k]  # calculate the sum of three numbers

                if three_sum < 0:  # if the sum is less than 0
                    j += 1  # increment j (move the left pointer to the right)
                elif three_sum > 0:  # if the sum is greater than 0
                    k -= 1  # decrement k (move the right pointer to the left)
                else:  # if the sum is equal to 0 (a valid triplet is found)
                    results.append([nums[i], nums[j], nums[k]])  # add the triplet to the results list

                    while j < k and nums[j] == nums[j + 1]:  # skip duplicates for j
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:  # skip duplicates for k
                        k -= 1

                    j += 1  # increment j (move the left pointer to the right)
                    k -= 1  # decrement k (move the right pointer to the left)

        return results  # return the list of triplets


    
if __name__ == "__main__":
    test = Solution()
    input = test.threeSum([-1,0,1,2,-1,-4])
    print(input)
