# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        i, j = 0,0
        
        ans = ListNode(-1)
        res = ans
        
        while l1  and l2:
            
            if l1.val == l2.val:
                ans.next = ListNode(l1.val)
                ans = ans.next 
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next
                l2 = l2.next
            elif l1.val < l2.val:
                ans.next = ListNode(l1.val)
                ans = ans.next 
                l1 = l1.next
            else:
                ans.next = ListNode(l2.val)
                ans = ans.next 
                l2 = l2.next
        
        while l1:
            ans.next = ListNode(l1.val)
            ans = ans.next 
            l1 = l1.next
        while l2:
            ans.next = ListNode(l2.val)
            ans = ans.next 
            l2 = l2.next
        
        print(res.next)
        # return ans
        return res.next
            
  
            
            
        