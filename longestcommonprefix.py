"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""  # If the list is empty, return an empty string

        min_len = min(len(s) for s in strs)  # Find the minimum length among the strings

        # Iterate over the characters up to the minimum length
        for i in range(min_len):
            char = strs[0][i]  # Get the character at the i-th position of the first string

            # Check if the character matches with the corresponding position in other strings
            if not all(s[i] == char for s in strs):
                return strs[0][:i]  # Return the prefix up to the i-th position

        return strs[0][:min_len]  # Return the entire minimum length prefix

if __name__ == "__main__":
    test = Solution()
    input = test.longestCommonPrefix(["flower","flow","flight"])
    print(input)