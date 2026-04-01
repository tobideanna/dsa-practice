# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we need to reverse the linked list:
        # [0 -> 1 -> 2 -> 3]
        # now points to nothing, so let's have 0 point to null
        #and make it the new tail
        curr = head
        prev = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


