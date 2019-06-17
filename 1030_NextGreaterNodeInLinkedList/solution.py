# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        res = [0] * 10000
        nums = 0
        curnode = head
        while curnode:
            while stack and stack[-1][0] < curnode.val:
                _, idx = stack.pop()
                res[idx] = curnode.val
            stack.append((curnode.val, nums))
            nums += 1
            curnode = curnode.next
        return res[:nums]
