# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        runner = result
        while l1 != None and l2 != None:
            new = ListNode()
            
            if l1.val > l2.val:
                new.val = l2.val
                l2 = l2.next
            else:
                new.val = l1.val
                l1 = l1.next
            runner.next = new
            runner = runner.next

        while l1 != None:
            new = ListNode()
            new.val = l1.val
            l1 = l1.next
            runner.next = new
            runner = runner.next

        while l2 != None:
            new = ListNode()
            new.val = l2.val
            l2 = l2.next
            runner.next = new
            runner = runner.next

        return result.next
        