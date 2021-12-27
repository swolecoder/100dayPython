# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return  None
        
        curr = head
        ans = curr
        
        while curr:
            
            if curr and curr.next and curr.val == curr.next.val:
                nextE = curr.next
                
                while curr.val == nextE.val:
                    nextE = nextE.next
                    if not nextE:
                        break
                
                curr.next = nextE
            
            
            else:
                curr = curr.next
        
        return ans
        