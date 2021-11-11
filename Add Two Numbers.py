# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        created = False
        carry = False
        while l1 or l2:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            if carry:
                num+=1
                carry = False
            if num>9:
                num %= 10
                carry = True
            l3.next = ListNode(num)
            l3 = l3.next
                   
            if not created: 
                created = True
                head = l3
        if carry:
            l3.next = ListNode(1)
        return head
                
