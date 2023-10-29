class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, ans = head, None
        while cur != None:
            head = head.next
            cur.next = ans
            ans = cur
            cur = head
        return ans
