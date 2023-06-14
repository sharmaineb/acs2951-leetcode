"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

class Solution:
    def wordBreak(self, s: str, wordDict):
        word_set = set(wordDict) # convert the wordDict list into a set for efficient word lookup

        dp = [False] * (len(s) + 1) # create a dynamic programming list of size len(s) + 1
        dp[0] = True # set the first element as True, indicating that an empty string can be segmented

        for i in range(1, len(s) + 1):# iterate over the string s from the second character to the last character
            for j in range(i): # iterate over j from 0 to i-1
                if dp[j] and s[j:i] in word_set: # if dp[j] is True (indicating substring s[:j] can be segmented) and s[j:i] exists in the wordDict
                    dp[i] = True # set dp[i] as True, indicating that substring s[:i] can be segmented
                    break # break out of the inner loop

        return dp[-1] # return the last element of dp, which indicates whether the entire string s can be segmented



if __name__ == "__main__":
    test = Solution()
    input = test.wordBreak("leetcode", wordDict = ["leet","code"])
    print(input)