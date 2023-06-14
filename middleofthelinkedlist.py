"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        slow = fast = head # initialize two pointers, slow and fast, both pointing to the head of the linked list
        
        while fast and fast.next: # traverse the linked list until the fast pointer reaches the end or the second-to-last node
            slow = slow.next # move the slow pointer one step at a time
            fast = fast.next.next # move the fast pointer two steps at a time
        
        return slow # when the fast pointer reaches the end, the slow pointer will be at the middle node (or the first middle node in the case of an even-length list)

if __name__ == "__main__":
    test = Solution()
    input = test.middleNode([1,2,3,4,5])
    print(input)