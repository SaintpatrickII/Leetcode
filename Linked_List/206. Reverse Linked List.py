class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        # prev is node behind the head

        # loop executes while current is still in linked list
        while curr:
            tmp = curr.next
            # tmp needed as we are reversing so curr.next points towards prev
            curr.next = prev 
            # prev moves to curr and curr moves to next node
            prev = curr
            curr = tmp
        return prev
        # at end of loop prev = curr which is new head
