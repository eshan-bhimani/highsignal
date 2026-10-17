# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head #initialize slow pointer
        fast = head #initialize slow pointer

        while fast and fast.next: #ensuring the linked list isnt at the end(therefore no loop)
            slow = slow.next # moving slow pointer by 1
            fast = fast.next.next # moving fast pointer by 2
            if slow == fast: # if its cycle, slow and fast will eventually land on same node, therefore True it is a cycle
                return True
        return False #else false
        
