
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # set both pointers at head

        while fast and fast.next:
            # while fast node is in bounds, hare & tortoise, if they ever match nodes then has to be cyclic :)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False