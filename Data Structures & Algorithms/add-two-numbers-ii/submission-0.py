# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #reverse both linked lists, and then do Add Two Numbers,
        #where you add two numbers like basic addition and keep track of carrys and 0s (edge cases)

        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        res = None
        while stack1 or stack2 or carry:
            summ = 0
            summ += carry
            if stack1:
                summ += stack1.pop()
            if stack2:
                summ += stack2.pop()

            node = ListNode(summ % 10)
            node.next = res
            res = node
            
            carry = summ // 10

        return res




        
            






        