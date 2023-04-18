class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        # create new linked list, assign dummynode just before beginning of linked list

        # condition for both lists still existing, compare & add smallest value
        while l1 and l2:
            if l1.val < l2.val:
                # ensure that tail and list move up 1 element for next comparison
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # condition for if only one list remains, here we only need to keep moving dummy tail forward
        if l1:
            tail.next = l1
                
        if l2:
            tail.next = l2
        
        # dummy is null as outside linkedlist so we return dummy.next
        return dummy.next