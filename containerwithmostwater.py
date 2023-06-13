"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104"""

"""
class Solution:
    def maxArea(self, height):
        result = 0
        for i in range(len(height)):
            for n in range(i + 1, len(height)):
                area = (n - i) * min(height[i], height[n])
                result = max(result, area)
"""
# O(n)

class Solution:
    def maxArea(self, height):
        result = 0  # initialize the variable to store the maximum area
        i, n = 0, len(height) - 1  # initialize two pointers, i and n

        while i < n:  # loop until the two pointers meet or cross each other
            area = (n - i) * min(height[i], height[n])  # calculate the area using the minimum height

            result = max(result, area)  # update the maximum area if necessary

            if height[i] < height[n]:  # if the height at pointer i is smaller
                i += 1  # increment i (move the left pointer to the right)
            else:
                n -= 1  # decrement n (move the right pointer to the left)

        return result  # return the maximum area


if __name__ == "__main__":
    test = Solution()
    input = test.maxArea([1,1])
    print(input)
