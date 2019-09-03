# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#两种方法 参见C版本
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代
        # prev = None
        # p = head
        # while p:
        #     tmp = p.next
        #     p.next = prev
        #     prev = p
        #     p = tmp
        # return prev
        
        #递归
        if not head or not head.next: 
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead