
from heapq import heappush,heappop,heapify
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = []
        heapify(h)
        
        for curr in lists:
            while curr is not None:
                heappush(h,curr.val)
                curr = curr.next
        
        print(h)
        
        res = ListNode()
        ans = res
        
        while h:
            res.next = ListNode(heappop(h))
            res = res.next
        
        return ans.next
        
        
        
        
        