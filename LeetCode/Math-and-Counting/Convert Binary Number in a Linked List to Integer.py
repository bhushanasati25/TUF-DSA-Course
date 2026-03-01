"""
🔗 Problem: Convert Binary Number in a Linked List to Integer
📂 Category: Math-and-Counting
🎯 Difficulty: Easy
🔗 URL: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

📝 Description:
   Convert binary number stored in linked list to decimal.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        result = 0
        current = head
        while current:
            result = (result << 1) | current.val
            current = current.next
        return result
