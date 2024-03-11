# Approach 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head=head.next
        left , right =0, len(arr)-1
        while left <= right:
            if arr[left] != arr[right]:
                return False
            left +=1
            right-=1
        return arr


--------------------------------------------------------------------------------------------------
# Approach 2 (Two Pointer)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # this loop is for traversing the linkedlist and finding the middle node (slow pointer)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reveresing second half of the linkdelist
        prev = None
        while slow:
            temp= slow.next
            slow.next=prev
            prev = slow
            slow = temp
        # checking the pallindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left =left.next
            right =right.next
        return True
